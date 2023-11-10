<?php

echo "<p><h2>Lista de Elementos Relacionados usando MongoDB, FastAPI y PHP</h2></p>";

$id = $_GET['id'];
$api_url = 'http://localhost:8002/data/'.$id;

$response = file_get_contents($api_url);

// Decodificar la respuesta JSON
$data = json_decode($response, true);

// Verificar la estructura de datos
var_dump($data);

// Verificar si la solicitud fue exitosa
if ($data !== null && isset($data['data'])) {
    $pcData = $data['data'];

        echo '
            <strong>id:</strong>' . $pcData['_id'] . '<br />
            <strong>marca:</strong> ' . $pcData['marca'] . '<br />
            <strong>modelo:</strong> ' . $pcData['modelo'] . '<br />
            <strong>Sistema Operativo:</strong> ' . $pcData['sistema_operativo'][0]['descripcion'] . '<br />
            <strong>Estado:</strong> ' . $pcData['estado'][0]['descripcion'] . '<br />
        ';
    

    echo '<strong>Tablas Relacionadas MongoDb</strong>: pc,estado, sistema_operativo';
} else {
    // Manejar errores de la solicitud a la API
    echo 'Error al obtener datos de la API';
}
echo '<p><a href="lista-pc.php">Volver</a></p>';

?>
