<?php


$servername = "localhost";
$username = "root";
$password = "";

//--------------------------------------------------
// DATABASES
//--------------------------------------------------

function delete_database($dbname){
	
	global $servername;
	global $username;
	global $password;

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

function create_database($namefolder){

	global $servername;
	global $username;
	global $password;

	$namefolder = str_replace('-', '_', $namefolder);
	$dbname = $namefolder;

	
	
	// Create connection
	$conn = new mysqli($servername, $username, $password);

	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 
	

	// Create Database
	$sql = "
		DROP DATABASE IF EXISTS $dbname;
		CREATE DATABASE $dbname CHARACTER SET utf8 COLLATE utf8_general_ci;
	";

	if ($conn->multi_query($sql) === TRUE) { echo "Database created successfully!"."<br>"; }
	else { echo "Error creating database: " . $conn->error."<br>";	}

	$conn->close();	
	
	return $dbname;
	
}


function executeSQL( $file, $db_name ){

	if( file_exists( $file ) ){

		$sql = file_get_contents( $file );

		global $servername;
		global $username;
		global $password;	
		
		// Create connection
		$conn = new mysqli($servername, $username, $password);

		// Check connection
		if ( $conn->connect_error ){
			die("Connection failed: " . $conn->connect_error);
		} 

		
		// Set Database first
		if ( $conn->query("USE $db_name;") === TRUE){ echo "DB ($db_name) Selected!<br>"; }
		else { echo "Error Selecting DB: " . $conn->error."<br>"; }
		
		// Execute query
		if ( $conn->multi_query($sql) === TRUE){ echo "<br>Query Executed!<br>"; }
		else { echo "Error Executing Query: " . $conn->error."<br>"; }

		$conn->close();	

	}


}

function findAndReplaceLine( $find, $file ){

	
	if( file_exists( $file )){

		$file_lines  = file( $file );					

		foreach ( $file_lines as $key => $line ) {				

			foreach ( $find as $findTerm => $lineReplace ) {					

			    $exist = strpos( $line, $findTerm );
			    if( $exist ){		    						
					
					// Replace term in file
					$file_lines[$key] = $lineReplace."\n";
					//Delete term from list of terms
					unset($find[ $findTerm ]); 

			    	break;
			    }
			}

			// if no more term to find, exit
			if( !count($find) ) break;			

		}

		file_put_contents( $file, $file_lines );
			
	}

}



//--------------------------------------------------
//		APP
//--------------------------------------------------



echo "<br>Instalando CI...<br>";

$fullPath = getcwd();
$folderName = explode('\\', $fullPath);
$folderName = end( $folderName );

//Creando DB...
$dbname = create_database( $folderName );


//Creating tables with query
executeSQL( $fullPath."/DB.sql", $dbname );



//Actualizando .htaccess con el folder actual
$data = array();		
$data["RewriteBase"] = "	RewriteBase /$folderName";
findAndReplaceLine( $data, $fullPath."/.htaccess" );

//Actualizando Base URL en config.php...
$data = array();		
$data["config['base_url']"] = "\$config['base_url'] = (isset(\$_SERVER['HTTPS']) ? 'https://' : 'http://') . \$_SERVER['HTTP_HOST'] . preg_replace('@/+$@', '', dirname(\$_SERVER['SCRIPT_NAME'])) . '/';";
findAndReplaceLine( $data, $fullPath."/application/config/config.php" );

//Actualizando Daros de Conexion en database.php...
$data = array();				
$data["'hostname' => "] = "	'hostname' => '$servername',";
$data["'username' => "] = "	'username' => '$username',";
$data["'password' => "] = "	'password' => '$password',";
$data["'database' => "] = "	'database' => '$dbname',";
findAndReplaceLine( $data, $fullPath."/application/config/database.php" );


echo "<br>Instalado!<br>";








?>