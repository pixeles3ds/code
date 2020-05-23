<?php 

/*

Functions on this page:

	
	functions

	
*/





//---------------------------------------------------------------------------
/**
 * Get all user for admin members page 
 *
 * @return Obj - sql 
 *
 *///------------------------------------------------------------------------
 function filtering_members_page_admin( $sql, $query ) {


    // If we are superadmin users, we can explore users
  	if( bp_current_component() == "members" && get_role_user() == "admin" ){ 		
  		

  		$type = $query->query_vars["type"];
  		$term = $query->query_vars["search_terms"];  

  		if( $type == "undefined") $type = "active"; // fix bug when search term by active order, the first time reutrn undefined

  		$sql_id_word = "";

        $filter = "";

        $options = array("admin","active","newest","premium","inactive","noplan","free"); 
		if( in_array( $type, $options ) ){
			$sql["select"] = "SELECT u.user_id as id FROM wp_bp_activity u" ;
			$filter = " u.component = 'members' AND u.type = 'last_activity' ";		
			$sql_id_word = "u.user_id";	

			if( $type != "newest" ){
				$sql["orderby"] = " ORDER BY u.date_recorded " ;
				$sql["order"] = " DESC " ;
			}
		}

		$options = array("alphabetical","undefined"); 
		if( in_array( $type, $options ) ){
			//$filter = " u.ID IN ( SELECT ID FROM wp_users WHERE user_status = 0 ) ";
			$filter = " u.user_status = 0 "; // users key confirmed and active
			$sql_id_word = "u.ID";	
		}
  		
		$sql["where"] = array();

		$sql["where"][] = " 1=1 ";
		$sql["where"][] = $filter;

		
		if( $type == "premium" || $type == "inactive" || $type == "free" ){ $sql["where"][] = $sql_id_word." IN (".members_find_levels($type).")";}
		else if( $type == "noplan" ){ $sql["where"][] = $sql_id_word." NOT IN (".members_find_levels($type).")"; }
		else if( $type == "admin" ){ $sql["where"][] = $sql_id_word." IN (".members_find_admins().")"; }


		if( $term ){			
			$sql["where"]["search"] = $sql_id_word." IN (".members_find_term($term).")";
		}
	
		
		//pr($query->query_vars);
        //pr($sql);        


  		return $sql;

  	}else{
		return $sql;  		
  	}

}







//---------------------------------------------------------------------------
/**
 * Get array of levels available
 *
 * @return Array - Id, name of levels
 *
 *///------------------------------------------------------------------------
function get_levels() { 

	global $wpdb;

    // Get groups used by an user
	$sql_query = $wpdb->prepare(
		"
		SELECT id, name
		FROM {$wpdb->prefix}pmpro_membership_levels
		"
		,1
	);

	return $wpdb->get_results($sql_query);

}







//---------------------------------------------------------------------------
/**
 * DELETE User, CHANGE level, ASSIGN admin role
 *
 *///------------------------------------------------------------------------
function members_actions( $id, $type, $data ) {


	if($type == "delete"){
	    require_once(ABSPATH.'wp-admin/includes/user.php' );
	    if( bp_loggedin_user_id() != $id ){
	    	wp_delete_user( $id );
	    }
	}


	if($type == "role"){

		if( bp_loggedin_user_id() != $id ){

			$user = new WP_User( $id );
		    
		    if( $data == "admin" ){
				$user->remove_role( 'subscriber' );// Remove role
				$user->add_role( 'administrator' ); // Add role
		    }if( $data == "subscriber" ){		    
				$user->remove_role( 'administrator' );// Remove role
				$user->add_role( 'subscriber' ); // Add role
		    }
	    }
	}

	if($type == "level"){

		if($data != "" ){			
			
			if ( !function_exists( 'pmpro_changeMembershipLevel' ) ) { 
			    require_once '/includes/functions.php'; 
			} 
			
			$level = $data; // The level			  
			$user_id = $id; // ID of the user to change levels for 
			$old_level_status = 'inactive'; 			  			
			$cancel_level = NULL; // The cancel level. 

			// NOTICE! Understand what this does before running. 
			$result = pmpro_changeMembershipLevel( $level, $user_id ); 

		}	
	}

	echo json_encode( array( "status" => "Done!" ) );
	exit();

}





//---------------------------------------------------------------------------
/**
 * Get data on POST method from members page
 *
 *///------------------------------------------------------------------------
function members_actions_post_data(){

    // If we are on buddypres xprofile forms, register and profile edit fields
  	if( bp_current_component() == "members" && get_role_user( bp_loggedin_user_id() ) == "admin"){

  		$data = $_POST; 
  		
  		if( $data["do_action"] == "1"){			
  			members_actions( $data["id"], $data["type"], $data["data"] );  			
  		}else{
  			// render members page
  		}
  	}

}







//---------------------------------------------------------------------------
/**
 * Disabling inactive users level on Search and show all users if admin
 *
 *///------------------------------------------------------------------------
 function members_find_term($term){

  	global $wpdb;

  	$term = trim( $term );

  	$prefix = $wpdb->prefix;

  	// get id of last name xprofile field
  	$sql_query = "
			SELECT id FROM {$prefix}bp_xprofile_fields AS x
			WHERE x.name LIKE '%last%'
  		";

  	$last_name_id = $wpdb->get_var($sql_query);


  	// get data by term search
  	$sql_query = "

		SELECT id
		FROM ( 

					# Final table with required fields id, name, username and email
					SELECT wpu.ID as id, wpu.user_login as username, wpu.user_email as email, bpu.name
					FROM {$prefix}users AS wpu
					INNER JOIN (

										# FIRST NAME table with LAST NAME table Left Joined to make the FULL NAME
										SELECT x.user_id AS id, CONCAT( x.value , ' ', COALESCE( res.value, '') ) AS name
										FROM {$prefix}bp_xprofile_data AS x 
										LEFT JOIN ( 		
																	# LAST NAME table
																	SELECT x.user_id, x.value
																	FROM {$prefix}bp_xprofile_data AS x 
																	WHERE x.field_id = $last_name_id
										) AS res
										ON x.user_id = res.user_id
										WHERE x.field_id = 1 

					) AS bpu
					ON wpu.ID = bpu.id

		) AS f
		WHERE name LIKE '%{$term}%'
		OR username LIKE '%{$term}%'
		OR email LIKE '%{$term}%'

  		";
  
  	$result = $wpdb->get_col($sql_query);

  	return implode(",",$result);


  }



//---------------------------------------------------------------------------
/**
 * Get users by level
 *
 * @return Array - Id, name of levels
 *
 *///------------------------------------------------------------------------
function members_find_levels( $level ){

  	global $wpdb;

  	$prefix = $wpdb->prefix;

  	// get id of last name field
  	$sql_query = "
		SELECT u.user_id FROM {$prefix}pmpro_memberships_users AS u
		INNER JOIN wp_pmpro_membership_levels l ON u.membership_id = l.id
		WHERE u.status = 'active'
		AND ";

	if( $level == "premium" ){ $sql_query .= "l.name LIKE '%premium%'"; }
	if( $level == "inactive" ){ $sql_query .= "l.name LIKE '%inactive%'"; }
	if( $level == "free" ){ $sql_query .= "l.name LIKE '%free%'"; }
	if( $level == "noplan" ){ $sql_query .= "( l.name LIKE '%premium%' OR l.name LIKE '%inactive%' OR l.name LIKE '%free%')"; }

  	$result = $wpdb->get_col($sql_query);

  	return implode(",",$result);

  }

//---------------------------------------------------------------------------
/**
 * Get only admin users
 *
 * @return Array - Id, name of levels
 *
 *///------------------------------------------------------------------------
 function members_find_admins(){

  	global $wpdb;

  	$prefix = $wpdb->prefix;

  	// get id of last name field
  	$sql_query = "
		SELECT u.ID
		FROM {$prefix}users u
		INNER JOIN wp_usermeta m ON m.user_id = u.ID
		WHERE m.meta_key = '{$prefix}capabilities'
		AND m.meta_value LIKE '%administrator%'
	";

  	$result = $wpdb->get_col($sql_query);

  	return implode(",",$result);

  }


 


/*-----------------------------------------------------------------------

  Inject javascript code to members page

  -----------------------------------------------------------------------*/


function members_inject_js(){

    
  	if( bp_current_component() == "members"){

		echo "<script>  var root_url = '". get_home_url()  ."/'; </script>";

		// CSS

		wp_enqueue_style( 'jquery-ui-min-css', get_stylesheet_directory_uri() . '/css/jquery-ui.min.css' ); 

		// JS

		wp_enqueue_script( 'jquery-ui-min-js', get_stylesheet_directory_uri() . '/js/jquery-ui.min.js', array( 'jquery' ) );

		if( bp_loggedin_user_id() == 21 ){ 
			wp_register_script( 'suavaa_membersapp', get_stylesheet_directory_uri() . '/js/membersApp.js', array( 'jquery' ), ver(), true );
			wp_enqueue_script('suavaa_membersapp');
		}else{
			
			echo "<script>function set_levels_dialog(){};function open_levels_dialog(){};</script>";
			
		}

  	}
}






/*-----------------------------------------------------------------------

  Do not execute third party sql filters on members page

  -----------------------------------------------------------------------*/
	
function remove_filters_user_clauses(){

	if( bp_current_component() == "members" ){
		remove_filter('bp_user_query_uid_clauses', 'bp_xprofile_bp_user_query_search');
		remove_filter('bp_user_query_uid_clauses', 'bps_uid_clauses',99);	
	}

}
?>