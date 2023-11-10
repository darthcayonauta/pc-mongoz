<?php

// URL de la API de FastAPI
$api_url = 'http://localhost:8002/data';

// Realizar la solicitud GET a la API
$response = file_get_contents($api_url);

// Decodificar la respuesta JSON
$data = json_decode($response, true);

// Verificar si la solicitud fue exitosa
if ($data !== null && isset($data['data'])) {
    $pcData = $data['data'];

    $counter =0 ;
    
    // Crear una tabla HTML
    echo '
    <p>
    <h2>Lista de Elementos Relacionados usando MongoDB, FastAPI y PHP</h2>
    </p>
    <table border="1" width="75%" cellspacing="0">
            <tr>
                <th>id</th>
                <th>Marca</th>
                <th>Modelo</th>
                <th>Sistema Operativo</th>
                <th colspan="2">Estado</th>
            </tr>';

    // Iterar sobre los datos y mostrar en la tabla
    foreach ($pcData as $pc) {

        $color = ($counter%2== 0) ?'#FFFFFF':'#EFEFEF';

        echo '<tr bgcolor="'.$color.'">
                <td>' . $pc['_id'] . '</td>
                <td>' . $pc['marca'] . '</td>
                <td>' . $pc['modelo'] . '</td>
                <td>' . $pc['sistema_operativo'][0]['descripcion'] . '</td>
                <td>' . $pc['estado'][0]['descripcion'] . '</td>
                <td>
                    <a href="eliminar.php?id='.$pc['_id'].'">Eliminar</a> |
                    <a href="detalle.php?id='.$pc['_id'].'">Detalle</a>
                </td>
              </tr>';

              $counter++;
    }

    echo '</table>
    <br><br>
    <strong>Tablas Relacionadas MongoDb</strong>: pc,estado, sistema_operativo
    
    ';
} else {
    // Manejar errores de la solicitud a la API
    echo 'Error al obtener datos de la API';
}

?>
