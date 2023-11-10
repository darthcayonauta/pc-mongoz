from pymongo import MongoClient
from datetime import datetime
from pymongo.errors import PyMongoError
from bson import ObjectId

class Db:
    def __init__(self):
        CONNECTION_STRING="mongodb://127.0.0.1:27017/pcTest"
        self.client = MongoClient(CONNECTION_STRING)

    #update de pc ...
        #actualizar un registro
    def updateData(self,id,update_data):
        pcCollection = self.client['pcTest']['pc']
        try:
            result = pcCollection.update_one({"_id":ObjectId(id)},{"$set":update_data})
            if result.modified_count > 0:
                return True
            else:
                return False
        except PyMongoError as e:
            print(f"Error al actualizar el registro: {e}")
            return False


    #ingresar datos (1 registro)
    def insertOne(self, data):
        pcCollection = self.client['pcTest']['pc']
        try:
            res = pcCollection.insert_one(data)
            return res.inserted_id
        except PyMongoError as e:
            print(f"Error a tratar de ingresar registro: {e}")
            return False


    # obtiene 1 registro de la coleccion pc y el nombre de sus campos asociados
    def getPc(self,id):
        pcCollection = self.client['pcTest']['pc']

        data = list(pcCollection.aggregate([
            {
                '$match':{
                    '_id':ObjectId(id)
                }
            },
            {
                '$lookup': {
                        'from': "sistema_operativo",
                        'localField': "soId", 
                        'foreignField': "_id",
                        'as': "sistema_operativo"
                        }
            },
                    {  
                '$lookup': {
                        'from': "estado",
                        'localField': "estadoId",
                        'foreignField': "_id",
                        'as': "estado"
                        }
                    }  ,
                    {
                '$project': 
                        {
                            "nombre": 1,  
                            "marca": 1,
                            "modelo": 1,                            
                            "sistema_operativo.descripcion": 1,                               
                            "estado.descripcion": 1 
                        }
                    } 
            ]))
        
        if data:
            print(data)
            return data
        else:
            return {}

    # obtiene todos los registros de pc y campos relacionados
    def getAllPc(self):
        pcCollection = self.client['pcTest']['pc']
        
        data = list(pcCollection.aggregate([
                    {
                        '$lookup': {
                        'from': "sistema_operativo",
                        'localField': "soId", 
                        'foreignField': "_id",
                        'as': "sistema_operativo"
                        }
                    },
                    {  
                        '$lookup': {
                        'from': "estado",
                        'localField': "estadoId",
                        'foreignField': "_id",
                        'as': "estado"
                        }
                    }  ,
                    {
                    '$project': 
                        {
                            "nombre": 1,  
                            "marca": 1,
                            "modelo": 1,
                            "sistema_operativo.descripcion": 1,  
                            "estado.descripcion": 1 
                        }
                    } 
             ]))
        
        return data
    
    def deletePcData(self,id):
        try:
            pcCollection = self.client['pcTest']['pc']
            res = pcCollection.delete_one({"_id":ObjectId(id)})

            if res.deleted_count > 0:
                return True
            else :
                return False

        except PyMongoError:
            print("Error al eliminar registro")
            return False

#probando
if __name__ == '__main__':
    ob = Db()
    print(ob.getAllPc())


