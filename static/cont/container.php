<?php
$json_string = json_encode($_POST);

$file_handle = fopen('container.json', 'w');
fwrite($file_handle, $json_string);
fclose($file_handle);
?>

