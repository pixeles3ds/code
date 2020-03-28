<?php

function delete_database($dbname){
	
	$servername = "localhost";
	$username = "root";
	$password = "";
	
	// Create connection
	$conn = new mysqli($servername, $username, $password);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	// Create database
	$sql = "DROP DATABASE ".$dbname;

	if ($conn->query($sql) === TRUE) {
		echo "Database created successfully";
	} else {
		echo "Error deleting database: " . $conn->error;
	}

	$conn->close();	

	echo "Base de datos Eliminada!";
	return $dbname;
	
}

function create_database($namefolder, $justDB = 0){
	
	$servername = "localhost";
	$username = "root";
	$password = "";
	
	$namefolder = str_replace('-', '_', $namefolder);
	
	if( $justDB ){
		$dbname = $namefolder;
	}else{
		$dbname = $namefolder."_".date('Ymdhis');
	}
	
	
	// Create connection
	$conn = new mysqli($servername, $username, $password);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	// Create database
	$sql = "CREATE DATABASE ".$dbname." CHARACTER SET utf8 COLLATE utf8_general_ci;";

	if ($conn->query($sql) === TRUE) {
		echo "Database created successfully";
	} else {
		echo "Error creating database: " . $conn->error;
	}

	$conn->close();	

	echo "Base de Datos Creada!";
	return $dbname;
	
}

function smartCopy($source, $dest, $options=array('folderPermission'=>0755,'filePermission'=>0755))
{
    $result=false;

    if (is_file($source)) {
        if ($dest[strlen($dest)-1]=='/') {
            if (!file_exists($dest)) {
                cmfcDirectory::makeAll($dest,$options['folderPermission'],true);
            }
            $__dest=$dest."/".basename($source);
        } else {
            $__dest=$dest;
        }
        $result=copy($source, $__dest);
        @chmod($__dest,$options['filePermission']);

    } elseif(is_dir($source)) {
        if ($dest[strlen($dest)-1]=='/') {
            if ($source[strlen($source)-1]=='/') {
                //Copy only contents
            } else {
                //Change parent itself and its contents
                $dest=$dest.basename($source);
                if(!file_exists($dest)) mkdir($dest);
                @chmod($dest,$options['filePermission']);
            }
        } else {
            if ($source[strlen($source)-1]=='/') {
                //Copy parent directory with new name and all its content
                if(!file_exists($dest)) mkdir($dest,$options['folderPermission']);
                @chmod($dest,$options['filePermission']);
            } else {
                //Copy parent directory with new name and all its content
                if(!file_exists($dest)) mkdir($dest,$options['folderPermission']);
                @chmod($dest,$options['filePermission']);
            }
        }

        $dirHandle=opendir($source);
        while($file=readdir($dirHandle))
        {
            if($file!="." && $file!="..")
            {
                 if(!is_dir($source."/".$file)) {
                    $__dest=$dest."/".$file;
                } else {
                    $__dest=$dest."/".$file;
                }
                //echo "$source/$file ||| $__dest<br />";
                $result=smartCopy($source."/".$file, $__dest, $options);
            }
        }
        closedir($dirHandle);

    } else {
        $result=false;
    }	
    return $result;
} 

function changeData( $dbname, $foldername ){

	$oldMessage = "define('DB_NAME', 'dbname');";
	$deletedFormat = "define('DB_NAME', '".$dbname."');";

	//read the entire string
	$str=file_get_contents( $foldername."/".'wp-config.php');

	//replace something in the file string - this is a VERY simple example
	$str=str_replace("$oldMessage", "$deletedFormat",$str);

	//write the entire string
	file_put_contents( $foldername."/".'wp-config.php', $str);
	echo "Conexion Establecida!";
}



if( isset($_GET["create"]) ){
	$db = $_GET["create"];
	create_database( $db, $justDB = 1 );
	header("Location: /" );
}

if( isset($_GET["delete"]) ){
	$db = $_GET["delete"];
	delete_database($db);
	header("Location: /" );
}

// Crear wordpress
if( isset($_GET["name"]) ){
	
	//Obtener todos los folders en un directorio
	$d = dir(".");
	while (false !== ($entry = $d->read())){
		if (is_dir($entry) && ($entry != '.') && ($entry != '..')){
			if( $entry == $_GET["name"]){
				echo "<script>alert('La carpeta ya existe!')</script>";
				echo "<script>window.location.href = '/';</script>";
				die();
			}
		}
	}	
	$d->close();
	
	
	echo "Copiado Wordpress...";
	smartCopy('w498/', $_GET["name"] );
	$dbname = create_database( $_GET["name"] );
	changeData( $dbname , $_GET["name"] );
	

	header("Location: /".$_GET["name"] );
	echo "<script>window.location.href = '/'".$_GET["name"].";</script>";
	die();
	
}else{
	echo "Parametro 'name' no existe!";
}




?>