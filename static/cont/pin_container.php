<?php
$json_string = json_encode($_POST);

$file_handle = fopen('pin_container.json', 'w');
fwrite($file_handle, $json_string);
fclose($file_handle);
?>

