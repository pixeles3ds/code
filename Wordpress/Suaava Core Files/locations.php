<?php /* Template Name: locations */

error_reporting(0);
ob_start();
header("Access-Control-Allow-Origin: *");
header('Content-Type: application/json');

try {

	if (!isset($_GET['type']) || empty($_GET['type'])) {throw new exception("Type is not set.");}
	$type = $_GET['type'];

	if ($type == 'getCountries') {
		$data = get_json_locations("0", "Countries");
	}

	if ($type == 'getStates') {
		if (!isset($_GET['countryId']) || empty($_GET['countryId'])) {throw new exception("Country Id is not set.");}
		$countryId = $_GET['countryId'];
		$data      = get_json_locations($countryId, "States");
	}

	if ($type == 'getCities') {
		if (!isset($_GET['stateId']) || empty($_GET['stateId'])) {throw new exception("State Id is not set.");}
		$stateId = $_GET['stateId'];
		$data    = get_json_locations($stateId, "Cities");
	}

	/*
	// Save Location ID's
	if( $type == 'save'){
		$save_data = $_POST["data"];
		
		$id = bp_displayed_user_id();
		
		if( $save_data != "")
			save_location(json_encode($save_data), $id); // Saving data location
		else
			save_location("", $id);

		$data = json_encode( array('status'=>'success', 'tp'=>1, 'msg'=>'Saved', 'result'=>$save_data, 'id'=>$id) );  
	}
	*/

	if( $type == 'locations'){
		// get all location tags, debugging purpose
		$sql = " 
			SELECT m.user_id, u.user_login, m.meta_value FROM wp_usermeta as m 
			INNER JOIN wp_users as u ON m.user_id = u.ID
			WHERE meta_key = 'suavaa_user_location'
		";
		pr( query_sql( $sql ) );
		die;
	}
	
	if( $type == 'custom'){
		// debugging purpose
		$sql = " 

		";
		query_sql( $sql );
		pr( "done" );
		die;
	}


} catch (Exception $e) {
	$data = json_encode( array('status' => 'error', 'tp' => 0, 'msg' => $e->getMessage()) );
} finally {
	echo $data;
}



ob_flush();
