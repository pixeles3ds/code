<?php 
/*

Functions on this page:

	
	get_role_user()
	get_level()
	get_member_domain()
	get_username_logged_in

	
*/



//---------------------------------------------------------------------------
/**
 * Get role of an user by id
 * 
 * @param id user
 * @return String - roles => admin, bpuser and unlogged
 *
 *///-------------------------------------------------------------------------
function get_role_user( $id = "" ){

	if( $id == "" )
		$id = bp_loggedin_user_id();

	if(is_user_logged_in()){

		if ( is_super_admin( $id ) ) {
			return "admin";
		}else{
			return "bpuser";
		}
		
	}else{
		return "unlogged";
	}

}





//---------------------------------------------------------------------------
/**
 * Get level of user by id
 *
 * @param Int $id - User Id
 * @param Int $id_return - If 0 return just the name level, if is 1, return array with the id and name of the level
 * @return String, Array 
 *
 *///-------------------------------------------------------------------------
function get_level( $id = "", $id_return = 0 ){

	if( $id == "" )
		$id = bp_loggedin_user_id();

	$pmpro_level_obj = pmpro_getMembershipLevelForUser( $id );

	$level = $pmpro_level_obj->id;
	$name = $pmpro_level_obj->name;

	if( $level == "2" || $level == "4" || $level == "5" || $level == "6" ){ $result = "premium"; }
	if( $level == "3"){ $result = "inactive"; }
	if( $level == ""){ $result = "none"; }

	// executed only from members panel when return the id level
	if( $id_return == 1 ){
		
		// if no level assigned
		if( $level == "" ){
			$level = "0"; 
			$name = "No Plan";
		}
	
		// If level is testing
		if( $level == "5" ){
			$result = "testing"; // Change premium to testing, to correctly css render at /members/
			$name = "Testing";
		}

		// If level is free users
		if( $level == "6" ){
			$name = "Free User";
		}
		
		$result = array("id" => $level, "val" => $result, "name" => $name );

	}

	return $result;

}



//---------------------------------------------------------------------------
/**
 * Get the url of the buddypress logged user
 * 
 * @return String - http://localhost/suavaapp/members/username/
 *
 *///-------------------------------------------------------------------------
function get_member_domain(){
	return bp_core_get_user_domain( bp_loggedin_user_id() );
}






//---------------------------------------------------------------------------
/**
 * Get the username of the buddypress logged user
 * 
 * @return String - "username"
 *
 *///-------------------------------------------------------------------------
function get_username_logged_in(){
	return bp_core_get_username( bp_loggedin_user_id() );
}





//---------------------------------------------------------------------------
/**
 * Return list of hidden levels and signup levels disabled
 * 
 * @return array - id levels
 *
 *///-------------------------------------------------------------------------
function get_hidden_levels(){

	$hidden = array(
		"5", // Premium Testing
		"6" // First Lady registered
	);

	return $hidden;
}






//---------------------------------------------------------------------------
/**
 * Return users with level 6, first ladies registerd
 * 
 * @return string - total number of users
 *
 *///-------------------------------------------------------------------------
function get_first_ladies_total(){

	global $wpdb;


	// SQL query to get total user with level, first ladies registered
	$sql_query = $wpdb->prepare(
		"
		SELECT count(user_id) AS total
		FROM {$wpdb->prefix}pmpro_memberships_users
		WHERE membership_id = 6
		AND status = 'active'
		"
		,1
	);

	//  Getting the activation key from the database
	$total = $wpdb->get_var($sql_query);

	return $total;
}





//---------------------------------------------------------------------------
/**
 * Return limit number of first ladies registration
 * 
 * @return int - limit number of users
 *
 *///-------------------------------------------------------------------------
function get_first_ladies_limit_number(){

	return 150;
}






//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Combine the name and last name fields when the name of a user is called 
 * The ID of the last name field is (15) on this DATABASE
 * 
 * @return String - "full name"
 *
 *///-------------------------------------------------------------------------
function get_completed_name($data){ 

    // The ID of the last name field is (15) on this DATABASE
	$lastname = xprofile_get_field_data( 15, bp_get_member_user_id() );
	return $data." ".$lastname;
}





?>