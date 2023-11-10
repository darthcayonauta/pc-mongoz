<?php

$pc_id_to_delete = $_GET['id'];  // Reemplaza esto con el ID de la PC que deseas eliminar
$api_url = 'http://localhost:8002/data/' . $pc_id_to_delete;

// Inicializar la sesión cURL
$ch = curl_init($api_url);

// Configurar opciones de cURL
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Realizar la solicitud
$response = curl_exec($ch);

// Verificar si la solicitud fue exitosa
if ($response !== false) {
    // Decodificar la respuesta JSON
    $data = json_decode($response, true);

    // Verificar si la eliminación fue exitosa
    if (isset($data['message'])) {
        echo 'Registro eliminado exitosamente: ' . $data['message'];
    } else {
        echo 'Error al eliminar el registro';
    }
} else {
    echo 'Error al realizar la solicitud DELETE';
}

// Cerrar la sesión cURL
curl_close($ch);

echo '<p><a href="lista-pc.php">Volver</a></p>';

?>
