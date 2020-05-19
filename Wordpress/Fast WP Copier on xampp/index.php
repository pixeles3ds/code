<?php

function get_databases(){
	
	$servername = "localhost";
	$username = "root";
	$password = "";
	
	// Create connection
	$conn = new mysqli($servername, $username, $password, "flores");
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	} 

	$sql = "SHOW DATABASES";
	$result = $conn->query($sql);

	while($row = $result->fetch_row()) {
	  print_r ($row[0]." <a href='/wp_creator.php?delete=".$row[0]."'>Del</a><br>");
	}

	$conn->close();	


}

?>

<style>
body{
	background: whitesmoke;
}

textarea:focus, input:focus{
    outline: none;
}

*:focus {
    outline: none;
}

::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
  color: #b3b3b3;
  text-align: center;
  opacity: 1; /* Firefox */
}



form div + div {
  margin-top: 1em;
}

label {
  /* To make sure that all labels have the same size and are properly aligned */
  display: inline-block;
  width: auto;
  text-align: right;
  font-size: 16px;
}

input, textarea {
    font: 1em sans-serif;
    width: 100%;
    box-sizing: border-box;
    border: 1px solid #f2f2f2;
    background-color: #eceded;
    border-radius: 10px;
    margin-top: 10px;
    padding: 5px 20px;
    color: dimgrey;
}
input:focus, textarea:focus {
	border-color: #d9d9d9 !important;
}

input:focus, textarea:focus {
  /* To give a little highlight on active elements */
  border-color: #000;
}

textarea {
  /* To properly align multiline text fields with their labels */
  vertical-align: top;

  /* To give enough room to type some text */
  height: 5em;
}

button {
    background-color: #3f4347;
    border: none;
    padding: 10px 20px;
    width: 100%;
    color: white;
    cursor: pointer;
    border-radius: 50px;
	margin-top:20px;
}

.lista,form, #procesando {  
	top: 20px;
	right: 20px;
    width: 45%;
	position:absolute;
    padding: 1em;
    border: 1px solid #f6f6f6;
    border-radius: 1em;
    background-color: white;
    font-family: monospace;
    box-shadow: 0px 3px 9px #0000001c;
}

.lista{
	top: 20px;
	left: 20px;
    width: 45%;
}


ul{
    padding: 0px;
    list-style: none;
    margin: 20px;
}

li{
    margin-bottom: 4px;
}
a{
	font-size: 16px;
}

#procesando{
	display:none;
	left: 0;
    right: 0;
    margin: auto;
    text-align: center;
    padding: 40px;
	
}

a.delProj{
	margin-right: 30px;
    color: white;
    text-decoration: none;
    font-weight: 600;
    font-size: 12px;
    display: inline-block;
    width: 12px;
    height: 12px;
    line-height: 11px;
    background: #bb1212;
    text-align: center;
    border-radius: 50px;
}

</style>

<form id="form" action="wp_creator.php" method="get" onsubmit="return validate(this);">
	<div>
		<input type="text" id="name" name="create" placeholder="Nombre DB" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Nombre DB'">
		<button type="submit">Crear DB</button>
	</div>
  <?php get_databases(); ?>
</form>

<div id="procesando">
	Creando Wordpress....
</div>

<div id="lista" class="lista">
<form id="form" action="wp_creator.php" method="get" onsubmit="return validate(this);">
	<div>
		<input type="text" id="name" name="name" placeholder="Nombre Folder Wordpress" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Nombre Folder Wordpress'">
		<button type="submit">Crear Wordpress</button>
	</div>
</form>

	<ul>	

<?php

	$d = dir(".");

	while (false !== ($entry = $d->read()))
	{
		if (is_dir($entry) && ($entry != '.') && ($entry != '..'))
			if( $entry != "w498"){
				echo "<li>";
				echo "<a class='delProj' title='Delete' href='javascript:deleteProject(\"{$entry}\")'>-</a>";
				echo "<a href='{$entry}'>{$entry}</a>";				
				echo "</li>";
			}
	}	

	$d->close();
?>

	</ul>
</div>

<script>
function validate(form) {

    // validation code here ...
	document.getElementById('form').style.display = "none";
	document.getElementById('lista').style.display = "none";
	document.getElementById('procesando').style.display = "block";
   
    return true;
    
}

function deleteProject( folderName ){
	
	conf = confirm( "Desea elminar (" + folderName + ")?" );
	if ( conf == true) {
	  conf2 = confirm("ELIMINAR ("+folderName + ")!");
	  if ( conf2 == true) {
		window.location.replace("/wp_creator.php?deleteProject="+folderName);
	  }
	}

}


</script>