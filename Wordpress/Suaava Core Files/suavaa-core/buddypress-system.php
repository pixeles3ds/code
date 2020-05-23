<?php 



//---------------------------------------------------------------------------
/**
 * 	Get the value of the referrer field
 *
 *///-------------------------------------------------------------------------

function suavaa_bp_get_refer( $id ) { return xprofile_get_field_data("refer", $id ); }






//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Change http to https on scripts
 *
 * @return String 
 *
 *///-------------------------------------------------------------------------
function agnostic_script_loader_src($src, $handle) {
    return preg_replace('/^(http|https):/', '', $src);
}




//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Change http to https on styles
 *
 * @return String 
 *
 *///-------------------------------------------------------------------------
function agnostic_style_loader_src($src, $handle) {
    return preg_replace('/^(http|https):/', '', $src);
}




//---------------------------------------------------------------------------
//		   ****    Remove the marging from html by admin bar    ****
//---------------------------------------------------------------------------

function remove_admin_login_header() {
    remove_action('wp_head', '_admin_bar_bump_cb');
}
add_action('get_header', 'remove_admin_login_header');







//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Redirect to suavaa profile user AFTER LOGIN
 *
 * @return String - new menu obj
 *
 *///-------------------------------------------------------------------------
function admin_default_page() {
	return get_home_url()."";
}








//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * FULL HD Cover Upload FIX
 *
 * @return Array - Image resolutions
 *
 *///-------------------------------------------------------------------------
function bb_cover_image_settings( $settings = array() ) {
	//$settings['callback'] = 'buddyboss_cover_image_callback';
	// $settings['theme_handle'] = 'buddyboss-bp-frontend';
	$settings['width'] = 3840;
	$settings['height'] = 2160;

	return $settings;
}


//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Set default avatar image if user does't has
 *
 * @return String - default url Image
 *
 *///-------------------------------------------------------------------------
function myavatar_add_default_avatar( $url ){
	return $img_url = wp_upload_dir()["baseurl"].'/gravatar.jpg';
}



//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Add the new logo by code on login page
 *
 * @param String - default messages on login form
 * @return String - URL of avatar full size 
 *
 *///-------------------------------------------------------------------------
function add_logo_login_form( $message ) {
	$root = (!empty($_SERVER['HTTPS']) ? 'https' : 'http') . '://' . $_SERVER['HTTP_HOST'] . '/';
	return '<div id="logo-container"><span class="s-icon-logoFull s-icon-white logo-login-form" onclick="location.href = \''. $root .'\';" ></span></div>'.$message;    
}






//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Add custom classes to body
 *
 * @param String - Classes comming from system
 * @return String - URL of avatar full size 
 *
 *///-------------------------------------------------------------------------
function add_body_class($classes) {

	global $post;
	$component = $post->post_name;

	// Add class ladies if we are on register and the type is ladies
	if( $component == "register" ){
		$params = $_GET;
		if( $params["type"] == "ladies" ){
			$classes[] = 'ladies_signup';
		}
	}

	if( $component == "members" && bp_loggedin_user_id() == 21 ){ $classes[] = 'supera'; }

	// Add class to body according to the level 
	$classes[] = 'suavaa_lvl_'.get_level();

	return $classes;
}






//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Add custom classes to all items on menus and Remove friends item
 *
 * @return Array - new menu obj
 *
 *///-------------------------------------------------------------------------
function fix_nav_menu_classes($items, $menu, $args) {


	if( $menu->taxonomy == 'nav_menu' ){
		foreach ( $items as $key => $item ) {         

        // If is not a submenu
			if( $item->menu_item_parent == "0"){

            // Add classes to each item
				$class = "sv-nav-".strtolower(str_replace(' ', '-', trim($item->title) ) );
				$item->classes[] = $class;


            //Remove friends item
				if ( $item->post_title == "Friends" ) unset( $items[$key] );
			}
		}
	}

	return $items;
}







//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 * Add admin members, profile and logout items for the left menu on all pages
 *
 * @return String - new menu obj
 *
 *///-------------------------------------------------------------------------
function add_admin_link($items, $args){

	$member_url = get_member_domain();

	if( $args->theme_location == 'left-panel-menu' ){

        // Select as visited the icons on menu left side if is the current page
		$current_profile = "";
		$current_members = "";
		if(  in_array( bp_current_action() , array( 'edit' , 'change-avatar' , 'change-cover-image')) ){ $current_profile = "current-menu-item"; }
		if(  in_array( bp_current_component() , array( 'members' )) ){ $current_members = "current-menu-item"; }


        // If we are admin, ad button to left menu to admin users
		$manage_users = '';
		if( get_role_user () == "admin")
			$manage_users = '<li class="bp-menu sv-nav-manage suavaa-profile-icon menu-item '.$current_members.' menu-item-type-custom menu-item-object-custom"><a href="' . get_home_url(). '/members/" class="fa-file">Manage Users</a></li>';


		$profile = '<li class="bp-menu sv-nav-profile suavaa-profile-icon menu-item '.$current_profile.' menu-item-type-custom menu-item-object-custom"><a href="' . $member_url. 'profile/edit/" class="fa-file">Profile</a></li>';
		$logout = '<li class="bp-menu sv-nav-logout suavaa-out-icon menu-item menu-item-type-custom menu-item-object-custom"><a href="'. wp_logout_url() .'" class="fa-file">Log Out</a></li>';

		$result = $manage_users."".$profile."".$items."".$logout;

	}

	return $result;
}







//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Disabling GeoMyWP location if free user !!!!!!
 *
 * @return Boolean 
 *
 *///-------------------------------------------------------------------------
function geomygp_disbale_location_free_user( $form ) {
	
	if( get_level() == "inactive" ){

		// Disbale Search Form 
		$form['search_form']['form_template'] = "";

		// Disbale Map
		$form['search_results']['display_map'] = 'na';
		$form['page_load_results']['display_map'] = 'na';
		$form['form_submission']['display_map'] = 'na';
		$form['map_usage'] = 'na';

		// Delete location from card user
		add_filter( 'gmw_location_address', create_function('','return "";') );

		return $form;

	}else{

		return $form;		

	}
	

}







//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Disabling GeoMyWP Caching !!!!!!
 *
 * @return Boolean 
 *
 *///-------------------------------------------------------------------------
function delete_geomywp_caching() {
	return false;
}





//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Disabling zoom scrolling on GeoMyWP Maps 
 *
 * @return Boolean 
 *
 *///-------------------------------------------------------------------------
function gmw_disable_scroll_zoom( $args ) {

	$args['map_options']['gestureHandling'] = 'cooperative';
  	$args['map_options']['scrollwheel'] = 0;
	$args['map_options']['mapTypeControl'] = 0;
	$args['map_options']['maxZoom'] = 16;

	return $args;
}




//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  If user is not premum, hide him
 *
 * @return Array 
 *
 *///-------------------------------------------------------------------------

 function filtering_memberpress( $sql, $query ) {
 	return $sql;
    // If we are superadmin users, we can explore users
  	if( bp_current_component() != "members" && get_role_user() != "admin" ){

        // if not premium user
  		if( get_level(bp_loggedin_user_id()) != "premium"){

            // Geo my WP Select, table wp_users
  			if( $sql['select'] == 'SELECT u.ID as id FROM wp_users u' ){
  				$sql['where'][] = "u.ID NOT IN (".bp_loggedin_user_id().") ";  
  			}

            // BuddyPress Search Select, table wp_bp_activity
  			if( $sql['select'] == 'SELECT u.user_id as id FROM wp_bp_activity u' ){
  				$sql['where'][] = "u.user_id NOT IN (".bp_loggedin_user_id().") ";  
  			}        

  			return $sql; 

  		}else{
  			return $sql;
  		}
  	}else{
  		return $sql;
  	}
}






//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Hide referrer field on xprofile edit form page to make it uneditable
 *
 * @return Array 
 *
 *///-------------------------------------------------------------------------
function xprofile_hide_fields( $retval ) {	
	
	if( bp_is_profile_edit() ) {	
		$retval['exclude_fields'] = '99';	// field id's example: "15,16,17"	
	} 
	return $retval;
	
}









//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * Fixing order and link on menu profile
 * Set profile as default component instead of activity
 *
 *///-------------------------------------------------------------------------
function bbg_change_profile_tab_order() {

  	global $bp;

  	$bp->bp_nav['activity']['position'] = 20;
  	$bp->bp_nav['profile']['position'] = 10;

    // If own profile or logged user is admin, redirect to edit on profile tab
  	if( bp_displayed_user_id() == bp_loggedin_user_id() || get_role_user() == "admin"){
  		$bp->bp_nav['profile']['link'] .= "edit";
  	}


}








//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * ACTIVATE ACCOUNT On user SingUp
 *
 *///-------------------------------------------------------------------------
function bp_auto_activate($id) {

	global $wpdb;


	// SQL query to get activation key for the new user id

	$sql_query = $wpdb->prepare(
		"
		SELECT  meta_value
		FROM {$wpdb->prefix}usermeta
		WHERE meta_key = 'activation_key' and user_id = $id
		"
		,1
	);

	//  Getting the activation key from the database
	$activation_key = $wpdb->get_var($sql_query);

	// Activate User
	bp_core_activate_signup( $activation_key );

}








//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * autologin, On user Activation
 *
 *///-------------------------------------------------------------------------
 function bp_auto_login(  $user_id, $key, $user ) {

  	global $bp, $wpdb;

    //simulate Bp activation

  	/* Check for an uploaded avatar and move that to the correct user folder, just do what bp does */
  	if ( is_multisite() )
  		$hashed_key = wp_hash( $key );

  	else
  		$hashed_key = wp_hash( $user_id );

  	/* Check if the avatar folder exists. If it does, rename it, move it and delete the signup avatar dir */
  	if ( file_exists( BP_AVATAR_UPLOAD_PATH . '/avatars/signups/' . $hashed_key ) )
  		@rename( BP_AVATAR_UPLOAD_PATH . '/avatars/signups/' . $hashed_key, BP_AVATAR_UPLOAD_PATH . '/avatars/' . $user_id );

  	bp_core_add_message( __( 'Your account is now active!', 'buddypress' ) );

  	$bp->activation_complete = true;

    //now login and redirect
  	wp_set_auth_cookie( $user_id, true, false );
  	bp_core_redirect( apply_filters ( "bpdev_autoactivate_redirect_url", bp_core_get_user_domain( $user_id ), $user_id ) );


}





//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * If not admin, not acces to dashboard
 *
 *///-------------------------------------------------------------------------
function redirect_non_admin_user(){
    if ( is_user_logged_in() ) {
        if ( !defined( 'DOING_AJAX' ) && !current_user_can('administrator') ){
            wp_redirect( get_member_domain() );  exit;
        }
    }
}







//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * REDIRECT TO REGISTER FORM, FROM LADIES SLUG
 *
 *///-------------------------------------------------------------------------
function register_ladies() {

	global $post;
	$component = $post->post_name;

	if( $component == "ladies" ){

		$type = "type=ladies";
		$refer = "&refer=".$_GET['refer'];

		// disable ladies page
    	/*if ( wp_redirect( get_home_url()."/register/?".$type."".$refer ) ) {
    		exit;
    	}*/

    	if ( wp_redirect( get_home_url()."/register/" ) ) {
    		exit;
    	}
	}

}






//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * GET REFER
 * AND ACTION ON REGISTER FORM BY TYPE OF USER, MEN'S OR LADIES
 *
 *///-------------------------------------------------------------------------
function register_get_params() {

	global $post;
	$component = $post->post_name;

	if( $component == "register" ){

		$params = $_GET;

		
		//disbling ladies registration method
		/*if( $params["type"] == "ladies" ){

			// If the numbers of free users ladies is less than the limit
			if( get_first_ladies_total() < get_first_ladies_limit_number() ){

				echo "<script> var ladies_registration = 1;</script>";

				wp_register_script( 'ladies', get_stylesheet_directory_uri() . '/js/ladies.js', array( 'jquery' ), ver(), true );
				wp_enqueue_script('ladies'); 				
			}


		}*/
		
		if( $params["refer"] != "" ){
			echo "<script> 
				
				var refer = '". $params["refer"] ."';

				window.onload = function() { 
					setTimeout(function(){ $('.field_refer fieldset > input').val(window.refer); },10)
				};

			</script>";
		}
		

	}

}








/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------


                                 ***  DROPDOWN DYNAMIC COUNTRY STATE AND CITY  *** 
                                 		***  AND LADIES REGISTRATION  *** 


----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/



//---------------------------------------------------------------------------
/**
 * Get ALL DATA JSON for countries, states and cities
 *
 * @return String - json obj
 *
 *///------------------------------------------------------------------------
function get_json_locations($id,$type){

	global $wpdb;

	$sql = "";
	if( $type == "Countries" ) $sql = " SELECT id, name FROM wp_bp_locations_countries ORDER BY name ASC";
	else if( $type == "States" ) $sql = " SELECT id, name FROM wp_bp_locations_states WHERE country_id = ". $id. " ORDER BY name ASC";
	else if( $type == "Cities" ) $sql = "SELECT id, name FROM wp_bp_locations_cities WHERE state_id = ". $id. " ORDER BY name ASC";


	$result = $wpdb->get_results( $sql );

	$res = array();
	foreach( $result as $d) {
		$res[$d->id] = $d->name;
	}

	$msg = $type." fetched successfully.";

	return json_encode( array('status'=>'success', 'tp'=>1, 'msg'=>$msg, 'result'=>$res) );  
}





//---------------------------------------------------------------------------
/**
 * Get the SAVED ID's of countries, states and cities
 *
 * @return String - json obj
 *
 *///------------------------------------------------------------------------
function get_saved_location($id){
	global $wpdb;

	$sql = $wpdb->prepare(" SELECT meta_value as val FROM wp_usermeta WHERE user_id = $id AND meta_key = 'suavaa_user_location' ",1);
	$val = $wpdb->get_var( $sql );
	return $val;
}







//---------------------------------------------------------------------------
/**
 * SAVE ID's of countries, states and cities
 *
 *///------------------------------------------------------------------------

function save_location($data,$id){	

	global $wpdb;

	if( $id != 0){

		$sql = $wpdb->prepare(" SELECT umeta_id as id FROM wp_usermeta WHERE user_id = $id AND meta_key = 'suavaa_user_location' ",1);
		$val = $wpdb->get_var( $sql );	


		if($val){	// UPDATE
			
			$wpdb->update( $wpdb->prefix.'usermeta', array('meta_value'=>$data), array('umeta_id'=>$val));	

		}else{ 	// INSERT

			$wpdb->insert($wpdb->prefix.'usermeta', array(
			    'user_id' => $id,
			    'meta_key' => 'suavaa_user_location',
			    'meta_value' => $data
			));

		}
	}

}




/*-----------------------------------------------------------------------
	
  On REGISTER and EDIT forms
  ENQUEUE javscript to ADD AJAX DROPDOWN for country, state and city fields 

  -----------------------------------------------------------------------*/

// Add locations dropdowns JAVASCRIPT to forms
  function locations_form_js(){



    // If we are on buddypres xprofile forms, register and profile edit fields
  	if( bp_current_component() == "register" || bp_current_action() == "edit" ){

  		$saved_location = get_saved_location( bp_displayed_user_id() ) ;
  		//$saved_location = get_saved_location( 14 ) ;

  		// If there is nothing saved
  		if( $saved_location == "" ){
  			
  			echo "<script> 
  					var root_url = '". get_home_url()  ."/';
  					var json_location_saved = false;

  				</script>";

  		}else{
  			
  			// Convert JSON to Obj
  			$saved_location_obj = json_decode($saved_location);

  			echo "<script> 
  						var root_url = '". get_home_url()  ."/';
  						var json_location_saved = true;
  						var json_location = ". $saved_location .";

  						var json_countries = ". get_json_locations( 0 ,"Countries")  .";
  						var json_states = ". get_json_locations( $saved_location_obj->country ,"States")  .";
  						var json_cities = ". get_json_locations( $saved_location_obj->state ,"Cities")  .";

  				</script>";
  		}

  		if( bp_current_component() == "register" ){
			wp_deregister_style('boss-child-custom'); 
			wp_register_style( 'boss-child-custom',  get_stylesheet_directory_uri() . '/css/custom.css', array(), ver()  );
			wp_enqueue_style( 'boss-child-custom');
  		}

		wp_register_script( 'locations', get_stylesheet_directory_uri() . '/js/locations.js', array( 'jquery' ), ver(), true );
		wp_enqueue_script('locations'); 

  	}
}








/*-----------------------------------------------------------------------
	
  On EDIT forms
  ENQUEUE javscript to disbale the edition of refer field  

  -----------------------------------------------------------------------*/

// Add locations dropdowns JAVASCRIPT to forms
  function refer_field_js(){

    // If we are on buddypres xprofile forms, register and profile edit fields
  	if( bp_current_action() == "edit" ){

		wp_register_script( 'refer_field', get_stylesheet_directory_uri() . '/js/refer_field.js', array( 'jquery' ), ver(), true );
		wp_enqueue_script('refer_field'); 

  	}
}






//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * GET FIELDS FROM REGISTER AND PROFILE FORM
 *
 *///-------------------------------------------------------------------------
function get_form_location_fields( $id ){


	$save_data = $_POST["location"];
	$save_data = str_replace("\\","",$save_data);

	/*pr($id);
	pr($save_data);
	die;*/
	
	if( $save_data != "")
		save_location($save_data, $id); // Saving data location
	else
		save_location("", $id);

}




//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * CHANGE LEVEL TO INACTIVE ELSE FIRST LADY 
 *
 *///-------------------------------------------------------------------------
function change_level_on_registration( $id ){


	//$first_lady_registering = $_POST["first_lady_register"];
	$gender = $_POST["field_2"];


	if ( !function_exists( 'pmpro_changeMembershipLevel' ) ) { 
	    require_once '/includes/functions.php'; 
	} 


	//disbling ladies registration method
	/*if( $first_lady_registering == "1"){

		// If the numbers of free users ladies is less than the limit
		if( get_first_ladies_total() < get_first_ladies_limit_number() ){
		
			$level = 6; // 6, First ladies level
			$user_id = $id; // ID of the user to change levels for 
			$old_level_status = 'inactive'; 			  			
			$cancel_level = NULL; // The cancel level. 

			// NOTICE! Understand what this does before running. 
			$result = pmpro_changeMembershipLevel( $level, $user_id ); 

		}

	}*/
	

	if( free_user_available( $id, $gender ) ){

		$level = 6; // 6, First free users level
		$user_id = $id; // ID of the user to change levels for 
		$old_level_status = 'inactive'; 			  			
		$cancel_level = NULL; // The cancel level. 

		// NOTICE! Understand what this does before running. 
		$result = pmpro_changeMembershipLevel( $level, $user_id ); 

	}else{
		
		$level = 3; // 3, INACTIVE LEVEL
		$user_id = $id; // ID of the user to change levels for 
		$old_level_status = 'inactive'; 			  			
		$cancel_level = NULL; // The cancel level. 

		// NOTICE! Understand what this does before running. 
		$result = pmpro_changeMembershipLevel( $level, $user_id ); 

	}

}





//---------------------------------------------------------------------------
/**
 * Get total free user by male and female - Total 150 each gender
 *
 *///-------------------------------------------------------------------------
function free_user_available( $id, $gender ){

	global $wpdb;

	$limitUser = 150;


	if( $gender == "Male") $gender = "m";
	else $gender = "f";


	$sql = $wpdb->prepare(" SELECT COUNT(id) as total FROM wp_bp_free_users WHERE gender = '$gender' ",1);
	$val = $wpdb->get_var( $sql );


	if( $val < $limitUser ){
		
	    $wpdb->insert("{$wpdb->base_prefix}bp_free_users", [
	        'id_user' => $id,
	        'gender' => $gender
	    ]);

		return true;

	}else{
		return false;
	}

}


/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------


                                 ***  HIDDING AND DISABLING LEVELS SIGNUP  *** 


----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/



//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Hide level from list level web
 *
 * @return Array - list of objects levels
 *
 *///-------------------------------------------------------------------------
function levels_hide_list($levels){

	$hidden_levels = get_hidden_levels();

	foreach( $levels as $key => $level ){		
		// If current level is in the hidden levels list
		if( in_array( $level->id, $hidden_levels ) ){
			unset( $levels[$key] ); // Delete level from list !!!
		}
	}   

    return $levels;
}




//---------------------------------------------------------------------------
//							****    FILTER    ****
//---------------------------------------------------------------------------
/**
 *  Disable level from checkout
 *
 * @return Obj - level obj
 *
 *///-------------------------------------------------------------------------
function levels_disable_checkout($data){
	
	$hidden_levels = get_hidden_levels();

	// If current level is in the hidden levels list
	if( in_array( $data->id, $hidden_levels ) ){
    	if ( wp_redirect( get_home_url()."/membership-account/membership-levels/") ) { // Redirecting the disabled level !!!
    		exit;
    	}
	}else{
		return $data;	
	}
	
}





//---------------------------------------------------------------------------
/**
 * Get list of referrals
 *
 * @return obj
 *
 *///------------------------------------------------------------------------
function get_referrals($id){

	global $wpdb;

	$nickname = bp_core_get_username($id);

	$sql = $wpdb->prepare("

		SELECT u.ID as id
		FROM {$wpdb->prefix}bp_xprofile_data AS d 
		INNER JOIN {$wpdb->prefix}bp_xprofile_fields AS f ON d.field_id =  f.id
		INNER JOIN {$wpdb->prefix}users AS u ON d.user_id =  u.ID
		WHERE f.name LIKE '%refer%'
		AND d.value = '$nickname'

		",1);

	$val = $wpdb->get_results( $sql );
	return $val;
}










//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * CHECK USER LEVEL STATUS and REDIRECT
 *
 *///-------------------------------------------------------------------------

function member_level() {


	global $post;	

/*
	pr( bp_current_component() );
	pr( "---------------------" );
	pr( bp_current_action() );
	pr( "---------------------" );

*/


  	// If user is loggined
	if( is_user_logged_in() ){

		$component = bp_current_component();

      	// If we are superadmin users, we can explore users
		if( $component == "members"){
			if ( get_role_user() != "admin" ) {
				if ( wp_redirect( get_home_url()."/browse-members/" ) ) {
					exit;
				}
			}
		}



      	// If we do not have a membership type assigned
		if( get_level() == "none" ){      

	        if( $component == "") $component = $post->post_name; // If not buddypress component get page slug

	        $exclude = array("membership-levels","membership-checkout","register","ladies"); // exclude pages of the redirection

	        // Go to membership levels
	        if( !in_array( $component, $exclude) ){
	        	if ( wp_redirect( get_home_url()."/membership-account/membership-levels/" ) ) {
	        		exit;
	        	}
	        }

      	}else if( get_level() == "inactive" ){ // disable features of a free member

      		/*
			//$disable = array("notifications","messages","activity","friends","groups"); // exclude pages of the redirection
			$disable = array("messages"); // exclude pages of the redirection

			// Go to membership levels
			if( in_array( $component, $disable) ){
				if ( wp_redirect( get_home_url()."/membership-account/membership-levels/" ) ) {
					exit;
				}
			}
			*/
      	}

  	}else{ // Not loggined

  		$component = $post->post_name;
        $exclude = array("register","locations","ladies","disabled-ladies"); // exclude pages of the redirection

        // Go to membership levels
        if( !in_array( $component, $exclude) ){
        	if ( wp_redirect( get_home_url()."/wp-login.php" ) ) {
        		exit;
        	}
        }


        // If ladies free registrations is limit exceded
        //disbling ladies registration method
        /*if( $component == "register" ){

			$params = $_GET;

			if( $params["type"] == "ladies" ){
				// If the numbers of free users ladies is less than the limit
				if( get_first_ladies_total() >= get_first_ladies_limit_number() ){
			    	if ( wp_redirect( get_home_url()."/disabled-ladies/") ) { // Redirecting the disabled level !!!
			    		exit;
			    	}
				}
			}
		}*/


    }
}






?>