from fastapi import FastAPI,HTTPException,status
import uvicorn
from dbClass import *
from datetime import datetime
from bson import ObjectId
from pymongo.errors import PyMongoError
from bson import ObjectId
from typing import Dict
from pydantic import BaseModel

class Item(BaseModel):
    marca: str
    modelo:str
    soId:str
    estadoId:str

app = FastAPI()
objDb = Db()

#update
@app.put("/data/{id}")
async def updateData(id:str,item:Item):
    try:
        item.soId = ObjectId(item.soId)
        item.estadoId = ObjectId(item.estadoId)
        res = objDb.updateData(id,item.dict())
        if res:
            return {"message":"Registro actualizado con exito"}
        else:
            raise HTTPException(status_code=404, detail="registro no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


#ingresar datos
@app.post('/data')
async def insertData(item:Item):
    #print(data)
    try:
        #campos especiales
        item.soId = ObjectId(item.soId)
        item.estadoId = ObjectId(item.estadoId)

        inserted = objDb.insertOne(item.dict())
        if inserted:
            return {"message":f"Registro con id {inserted} Ingresado Correctamente"}
        else:
            raise HTTPException(status_code=500,detail="Error al ingresar Registro")
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

#obten 1 dato
@app.get('/data/{id}')
async def getOne(id:str):
   try:
       data = objDb.getPc(id) 
       #if isinstance(data,dict):
       #    data['_id'] = str(data['_id'])
       #    return {"data":data}
       if data:
            for d in data:
                d['_id'] = str(d['_id'])
            return {"data":d}
       else:
           raise HTTPException(status_code=404,detail="Data no encontrada")
   except Exception as e:
       raise HTTPException(status_code=500, detail="Internal Server Error")

#obten todos los datos
@app.get('/data')
async def getAllPcData():
    try:
        datos = objDb.getAllPc()

        for dato in datos:
            dato['_id'] = str(dato['_id'])

    except PyMongoError as error :
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Error en Mongodb {error}")
    
    except Exception as error:
        # Manejar cualquier otro error  
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        detail=f"Error interno: {error}"
    )

    return {"data":datos}

#eliminar un pc
@app.delete("/data/{id}")
async def deletePc(id:str):
    try:
        res = objDb.deletePcData(id)
        if res :
            return {"message":f"Registro {id} elimninado"}
        else:
            raise HTTPException(status_code=404, detail=f"registro {id} no encontrado")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8002)