<?php

// URL de la API de FastAPI
$apiUrl = 'http://localhost:8001/data';

// Inicializar una sesión cURL
$ch = curl_init($apiUrl);

// Establecer opciones para la solicitud cURL
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Realizar una solicitud GET
$response = curl_exec($ch);

// Verificar si hubo algún error en la solicitud
if (curl_errno($ch)) {
    echo 'Error en la solicitud cURL: ' . curl_error($ch);
}

// Cerrar la sesión cURL
curl_close($ch);

// Procesar la respuesta de la API (puede variar según la estructura de datos de la API)
if ($response) {
    // Decodificar la respuesta JSON
    $responseData = json_decode($response, true);

    // Verificar si se obtuvieron datos válidos
    if (isset($responseData['data']) && is_array($responseData['data']) && count($responseData['data']) > 0) {
        echo '<table border="1" width="75%">';
        echo '<tr><th>ID</th><th>Name</th><th>Age</th><th>Department</th><th>Date</th></tr>';
        
	$counter =0 ;
        foreach ($responseData['data'] as $item) {
            echo '<tr>';
            echo '<td>' . ($counter+1) . '</td>';
            echo '<td>' . $item['name'] . '</td>';
            echo '<td>' . $item['age'] . '</td>';
            echo '<td>' . $item['departament'] . '</td>';
            echo '<td>' . $item['date'] . '</td>';
	    echo '</tr>';
	    $counter++;
        }

        echo '</table>';
    } else {
        echo 'No se recibieron datos válidos de la API.';
    }
} else {
    echo 'No se recibió una respuesta válida de la API.';
}
?>
