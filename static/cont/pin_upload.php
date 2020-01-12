<?php
$target_dir = "/home/svabis/web/utils/pin_submit/pin_temp/";
//$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
$target_file = $target_dir . "train.xlsx";
$uploadOk = 1;

$fileType = strtolower(pathinfo( $target_dir . basename($_FILES["fileToUpload"]["name"]) ,PATHINFO_EXTENSION));

// Check if file already exists
//if (file_exists($target_file)) {
//    echo "Sorry, file already exists.";
//    $uploadOk = 0;
//}

// Allow certain file formats
if($fileType != "xlsx" && $fileType != "xls") {
    echo "Sorry, only Excel files are allowed.";
    $uploadOk = 0;
}

// Check if $uploadOk is set to 0 by an error
if ($uploadOk == 0) {
    echo "Sorry, your file was not uploaded.";

// if everything is ok, try to upload file
} else {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {
//        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
      header("Location: http://www.kuvalda.lv/container_pin/");
      die();
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
}
?>

