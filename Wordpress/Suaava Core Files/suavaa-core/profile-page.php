<?php 

/*

Functions on this page:

	
	profile_style_scripts()
	suavaa_bp_get_avatar()
	suavaa_bp_get_cover()
	suavaa_bp_get_link()
	suavaa_bp_get_second_cover()
	suavaa_bp_get_about_image()
	suavaa_bp_get_images()

	
*/









//---------------------------------------------------------------------------
//							****    ACTION    ****
//---------------------------------------------------------------------------
/**
 * 	Load and Unload css and js for the profile custom page
 *
 *///-------------------------------------------------------------------------
function profile_style_scripts() {

	if( bp_is_user_profile() && bp_current_action() == "public" ){
		
		
		// Dequeue CSS 

		wp_dequeue_style('pmpro_frontend');
		wp_dequeue_style('pmpro_print');
		wp_dequeue_style('gmw-frontend');
		wp_dequeue_style('bpxp_image_field-css');
		wp_dequeue_style('boss-main-global');
		wp_dequeue_style('boss-main-desktop');
		wp_dequeue_style('boss-main-mobile');
		wp_dequeue_style('buddypress-global-search'); 
		wp_dequeue_style('fontawesome'); 
		wp_deregister_style('boss-child-custom'); 

		// Dequeue JS 

		wp_dequeue_script( 'bp-confirm' );
		wp_dequeue_script( 'bp-livestamp' );
		wp_dequeue_script( 'bp-legacy-js' );
		wp_dequeue_script( 'bp-widget-members' );
		wp_dequeue_script( 'version_compare-js' );
		wp_dequeue_script( 'bpxp_image_field-js' );
		wp_dequeue_script( 'idangerous-swiper' );
		wp_dequeue_script( 'heartbeat' );
		wp_dequeue_script( 'buddyboss-modernizr' );
		wp_dequeue_script( 'selectboxes' );
		wp_dequeue_script( 'fitvids' );
		wp_dequeue_script( 'superfish' );
		wp_dequeue_script( 'hoverIntent' );
		wp_dequeue_script( 'resize' );
		wp_dequeue_script( 'growl' );
		wp_dequeue_script( 'buddyboss-slider' );
		wp_dequeue_script( 'buddypress-global-search' );

		
		// Queue NEW CSS
		
		wp_enqueue_style( 'animatecss', get_stylesheet_directory_uri() . '/css/animate.min.css' ); 
		wp_enqueue_style( 'bootstrapcss', get_stylesheet_directory_uri() . '/css/bootstrap.min.css' );
		wp_enqueue_style( 'fontawesom', get_stylesheet_directory_uri() . '/css/all.css' ); 
		wp_enqueue_style( 'tooltip', get_stylesheet_directory_uri() . '/css/simptip.min.css' ); 
		wp_register_style( 'boss-child-custom',  get_stylesheet_directory_uri() . '/css/custom.css', array(), ver()  );
		wp_enqueue_style( 'boss-child-custom');


		// Queue NEW JS
		
		wp_enqueue_script( 'easingmin', get_stylesheet_directory_uri() . '/js/easing.min.js', array( 'jquery' ) );
		wp_enqueue_script( 'wow', get_stylesheet_directory_uri() . '/js/wow.min.js', array( 'jquery' ) );
		wp_enqueue_script( 'bootstrapjs', get_stylesheet_directory_uri() . '/js/bootstrap.min.js', array( 'jquery' ) );
		wp_enqueue_script( 'hammerjs', get_stylesheet_directory_uri() . '/js/hammer.min.js', array( 'jquery' ) );

		
		wp_register_script( 'webapp', get_stylesheet_directory_uri() . '/js/webApp.js', array( 'jquery' ), ver(), true );
		wp_register_script( 'youtubeapp', get_stylesheet_directory_uri() . '/js/youtube.js', array( 'jquery' ), ver(), true );
		wp_enqueue_script('webapp'); 
		wp_enqueue_script('youtubeapp'); 

		
	}
	
}
    




//---------------------------------------------------------------------------
/**
 * 	Get the value of custom profile fields by the name of the field and id user.
 *
 *///-------------------------------------------------------------------------

function suavaa_bp_get_name( $id ) { return xprofile_get_field_data("First Name", $id ); }
function suavaa_bp_get_lastname( $id ) { return xprofile_get_field_data("Last Name", $id ); }
function suavaa_bp_get_self_description( $id ) { return xprofile_get_field_data("Brief Self Description", $id ); }
function suavaa_bp_get_about( $id ) { return xprofile_get_field_data("About Me", $id ); }
function suavaa_bp_get_about_desc( $id ) { return xprofile_get_field_data("Second Cover Photo Tag Line", $id ); }







//---------------------------------------------------------------------------
/**
 * get social urls
 *
 *///-------------------------------------------------------------------------
function bp_get_social_media($id) {

	global $wpdb;


	// SQL query to get activation key for the new user id

	$sql_query = $wpdb->prepare(
		"
			SELECT  meta_key as name, meta_value as val
			FROM {$wpdb->prefix}usermeta
			WHERE user_id = $id
			AND ( 
				meta_key = 'Youtube'
				OR meta_key = 'Facebook'
				OR meta_key = 'Instagram'
				OR meta_key = 'Twitter'
			) ORDER BY name
		"
		,1
	);

	//  Getting the activation key from the database
	$data = $wpdb->get_results($sql_query);


	$total = 0;

	foreach ( $data as $item) {
		if( $item->val != ""){ 
			$total++;
		}
	}


	$result = array( 
        'facebook' => $data[0]->val,
        'instagram' => $data[1]->val,
        'twitter' => $data[2]->val,
        'youtube' => $data[3]->val,
        'total' => $total
    ) ;

    return $result;

}






//---------------------------------------------------------------------------
/**
 * Get avatar image url by user id
 *
 * @param Int $id - ID of user
 * @return String - URL of avatar full size 
 *
 *///-------------------------------------------------------------------------

function suavaa_bp_get_avatar( $id ) {

	$args = array(  
            'item_id' => $id, // id of user for desired avatar
            'type'    => 'full',
            'html'   => FALSE     // FALSE = return url, TRUE (default) = return img html
        ) ;

	return bp_core_fetch_avatar( $args )."?".ver();

}





//---------------------------------------------------------------------------
/**
 * Get the youtube link by id.
 *
 * @param Int $id - ID of user
 * @return String   URL of youtube link video
 *
 *///------------------------------------------------------------------------
function suavaa_bp_get_link( $id ) { 

	$link = xprofile_get_field_data( "Video Bio", $id );  // Video Bio is the name of the field, if the name change, change this line

	if (strpos($link, '?v=') !== false) {    

		$link = get_string_between($link,"?v=",'" rel');

		return $link;

	}else{
		return "";  
	}
}






//---------------------------------------------------------------------------
/**
 * Get cover image by id.
 *
 * @param Int $id - ID of user
 * @return String   URL of cover image or a svg background if not exist image
 *
 *///------------------------------------------------------------------------
function suavaa_bp_get_cover( $id ) {

	$args = array(  
		'object_dir' => 'members',
		'item_id' => $id,
	) ;

	$data = bp_attachments_get_attachment( 'url', $args );

	if( $data ){
		return $data."?".ver();
	}else{
		return get_stylesheet_directory_uri()."/images/logoFullMainBackground.svg?".ver();
	}


}







//---------------------------------------------------------------------------
/**
 * Get second cover image by id.
 *
 * @param Int $id - ID of user
 * @return String   URL of second  cover image or a svg background if not exist image
 *
 *///------------------------------------------------------------------------
function suavaa_bp_get_second_cover( $id ) { 

	global $wpdb;

    // Get groups used by an user
	$sql_query = $wpdb->prepare(
		"
		SELECT d.value val
		FROM {$wpdb->prefix}bp_xprofile_data d
		INNER JOIN {$wpdb->prefix}bp_xprofile_fields f  ON d.field_id = f.id
		WHERE d.user_id = $id AND f.name LIKE '%Second Cover Photo%'
		"
		,1
	);

	$data = $wpdb->get_results($sql_query);
        // if there is an image
	if( count($data) ){
		return get_home_url()."/wp-content".$data[0]->val."?".ver(); 
	}else{
		return get_stylesheet_directory_uri()."/images/logoFullSecondBackground.svg?".ver();
	}

}





//---------------------------------------------------------------------------
/**
 * Get about image by id.
 *
 * @param Int $id - ID of user
 * @return String - URL of about image or a svg background if not exist image
 *
 *///------------------------------------------------------------------------
function suavaa_bp_get_about_image( $id ) { 

	global $wpdb;

    // Get groups used by an user
	$sql_query = $wpdb->prepare(
		"
		SELECT d.value val
		FROM {$wpdb->prefix}bp_xprofile_data d
		INNER JOIN {$wpdb->prefix}bp_xprofile_fields f  ON d.field_id = f.id
		WHERE d.user_id = $id AND f.name LIKE '%about me photo%'
		"
		,1
	);
		

	$data = $wpdb->get_results($sql_query);
        // if there is images
	if( count($data) ){
		return get_home_url()."/wp-content".$data[0]->val."?".ver(); 
	}else{
		return get_stylesheet_directory_uri()."/images/logoImageBackground.svg?".ver();
	}

}






//---------------------------------------------------------------------------
/**
 * Get extra images by id.
 *
 * @param Int $id - ID of user
 * @return Array - Array with URL's of extra images or a svg background if not exist images
 *
 *///------------------------------------------------------------------------

function suavaa_bp_get_images( $id ) { 

	global $wpdb;

    // Get groups used by an user
	$sql_query = $wpdb->prepare(
		"
		SELECT d.value as val, d.field_id as id
		FROM {$wpdb->prefix}bp_xprofile_data d
		INNER JOIN {$wpdb->prefix}bp_xprofile_fields f  ON d.field_id = f.id
		WHERE d.user_id = $id AND (f.name LIKE '%gallery%' OR f.name LIKE '%extra photo%')
		"
		,1
	);


	$data = $wpdb->get_results( $sql_query );

	foreach ( $data as $key=>$val) {
		$data[$key]->val = get_home_url()."/wp-content".$data[$key]->val; 
	}

    // if there are images
	if( count($data) ){
		return $data;   
	}else{

        // preview images

		$newObj = array();

		for ($x = 0; $x <= 7; $x++) {
			$img = new stdClass;
			$img->val = get_stylesheet_directory_uri()."/images/logoImageBackground.svg?".ver();
			$img->id = $x;  
			$newObj[] = $img;
		} 

		return $newObj;
	}

}






//---------------------------------------------------------------------------
/**
 * Get basic data information of user by id. Fields = location, occupation, gender, ethnicity, age, birthdate
 *
 * @param Int $id - ID of user
 * @return Array 
 *
 *///------------------------------------------------------------------------
function suavaa_get_base_fields( $id ){

	global $wpdb;


	// If the user is inactive, fo not show the location
	$location = " OR f.name LIKE '%location%' ";	
	if( get_role_user() == "admin" || bp_displayed_user_id() == bp_loggedin_user_id()) {
		// do not change location tense	
	}else{
		if( get_level() == "inactive" ){
			$location = "";
		}
	}




	$sql_query = $wpdb->prepare(
		"
		SELECT d.field_id id, f.name name, d.value val
		FROM {$wpdb->prefix}bp_xprofile_data d
		INNER JOIN {$wpdb->prefix}bp_xprofile_fields f  ON d.field_id = f.id
		WHERE d.user_id = $id 
		AND (		
		f.name LIKE '%occupation%'
		OR f.name LIKE '%gender%'
		OR f.name LIKE '%ethnicity%'
		OR f.name LIKE '%age%' 
		OR f.name LIKE '%birthdate%' 
		OR f.name LIKE '%phone%' 
		OR f.name LIKE '%interest%' 
		OR f.name LIKE '%meeting%' 
		$location
		)
		ORDER BY f.field_order ASC
		"
		,1
	);

	$data = $wpdb->get_results($sql_query);


	foreach ( $data as $key=>$val) {

		if( $val->name == "Age" || $val->name == "Birthdate"){

			$raw_date = $data[$key]->val;


			date_default_timezone_set('America/New_York');
			$today = date('m/d/Y h:i:s a', time());

			$birth_obj = new DateTime( $raw_date );
			$today_obj = new DateTime( $today );
			$diff = $today_obj->diff( $birth_obj );



            //$allGroups[0]->data[$key]->val = date('F d',strtotime( $raw_date ));

			$data[$key]->val = $diff->y." Years old";
			$data[$key]->name = "Age";
		}


		if( $val->name == "Meeting"){

			$resutl = array(); 

			$eth = $data[$key]->val;
			$arrayItems = explode('";', $eth);
            unset( $arrayItems[count($arrayItems)-1]); // delete last item
            
            // extract item between "" on each value separated by ;
            foreach ( $arrayItems as $each_data) {
            	$resutl[] = explode('"', $each_data)[1];
            }

            

            $data[$key]->val = implode(" - ", $resutl ); // save result unified by " - "
            
        }

		
		// Disbaling number display on inactive users
		if( get_level( bp_displayed_user_id() ) == "inactive" ){
			if( $val->name == "Phone"){				
				unset( $data[$key] );	
			}			
		}
	

    }

    return $data;

}






//---------------------------------------------------------------------------
/**
 * Modify the default menu and print it.  This is visible Only on MOBILE VERSION and PROFILE page
 *
 * @return String
 *
 *///------------------------------------------------------------------------
function suavaa_get_profile_menu(){

	$items = "";

	$alerts = get_alerts();


	if(is_user_logged_in()){

		$menu_name = 'left-panel-menu';
		$locations = get_nav_menu_locations();
		$menu = wp_get_nav_menu_object( $locations[ $menu_name ] );
		$menuitems = wp_get_nav_menu_items( $menu->term_id, array( 'order' => 'DESC' ) );


        // If we are admin, ad button to left menu to admin users
        // Custom link Manage Users
		if( get_role_user () == "admin")
			$items .= '           <li class="menu-item-profile sv-nav-manage"><a href="'.get_home_url().'/members/" class="fa">Manage Users</a></li>';

        // Custom link Profile
		$items .= '           <li class="menu-item-profile sv-nav-profile"><a href="'.get_member_domain().'profile/edit/" class="fa">Profile</a></li>';

        //get sub menu items first
		$submenus = array();
		foreach( $menuitems as $item){
			if( $item->menu_item_parent != 0){
				$submenus[ $item->menu_item_parent ] .= '<li><a href="'.$item->url.'">'.$item->title.'</a></li>'; 
			}
		}

        // Wordpress links
		foreach( $menuitems as $item){

          // if we do not have a parent item
			if( $item->menu_item_parent == 0){


            // Add wordpress classes to the item
				$classes = "";
				foreach( $item->classes as $class){
					$classes .= $class." ";
				}


				$submenu_item = "";
				$submenu_class = "";

            // If actual item has childrens
				if( array_key_exists($item->ID, $submenus) ){ 
					$submenu_class = 'has_submenu';
					$submenu_item = '<div class="mobile-sub-menu"><ul>'.$submenus[ $item->ID].'</ul></div>';
					$item->url = 'javascript:switch_submenu_mobile(\'mobile-sub-menu-item-'.$item->ID.'\');';
				}


				$items .= '           <li class="'.$classes.' '.$submenu_class.' mobile-sub-menu-item-'.$item->ID.'"><a href="'.$item->url.'" class="fa">'.$item->title.' '.$alerts[$item->title].'</a>'.$submenu_item.'</li>';

			}
		}

        // Logout
		$items .= '           <li class="menu-item-logout sv-nav-logout"><a href="'.wp_logout_url().'" class="fa">Log Out</a></li>';


	}else{
		$items .= '           <li class="menu-item-login sv-nav-login"><a href="'.get_home_url().'/wp-login.php" class="fa">Login</a></li>';
		$items .= '           <li class="menu-item-register sv-nav-register"><a href="'.get_home_url().'/register/" class="fa">Register</a></li>';
	}

	echo $items; 
}










//---------------------------------------------------------------------------
/**
 * Modify the default menu and print it.  This is the left side menu, Only visible on the  PROFILE page
 *
 * @return String
 *
 *///------------------------------------------------------------------------
function suavaa_get_profile_sidebar_menu(){

	$items = "";

	$alerts = get_alerts();

	if(is_user_logged_in()){

		$menu_name = 'left-panel-menu';
		$locations = get_nav_menu_locations();
		$menu = wp_get_nav_menu_object( $locations[ $menu_name ] );
		$menuitems = wp_get_nav_menu_items( $menu->term_id, array( 'order' => 'DESC' ) );



        // If we are admin, ad button to left menu to admin users
        // Custom link Manage Users
		if( get_role_user () == "admin")        
			$items .= '           <li class="s-item menu-item-profile sv-nav-manage"><a href="'.get_home_url().'/members/" class="s-icon fa">Manage Users</a><div class="s-submenu"><a href="'.get_member_domain().'members/">Manage Users</a></div></li>';


        // Custom link Profile
		$items .= '           <li class="s-item menu-item-profile sv-nav-profile"><a href="'.get_member_domain().'profile/edit/" class="s-icon fa">Profile</a><div class="s-submenu"><a href="'.get_member_domain().'profile/edit/">Profile</a></div></li>';

        //get sub menu items first
		$submenus = array();
		foreach( $menuitems as $item){
			if( $item->menu_item_parent != 0){
				$submenus[ $item->menu_item_parent ] .= '<li><a href="'.$item->url.'">'.$item->title.'</a></li>'; 
			}
		}


        // Wordpress links
		foreach( $menuitems as $item){

			if( $item->menu_item_parent == 0){


            // Add wordpress classes to the item
				$classes = "";
				foreach( $item->classes as $class){
					$classes .= $class." ";
				}

				$submenu_item = '<a href="'.$item->url.'">'.$item->title.'</a>';
				$submenu_class = "";


            // If actual item has childrens  
				if( array_key_exists($item->ID, $submenus) ){ 
					$submenu_class = 'has_submenu';
					$submenu_item = '<a class="submenu-title" href="'.$item->url.'">'.$item->title.'</a><ul>'.$submenus[ $item->ID].'</ul>';
					$item->url = "javascript:void(0);";
				}


				$items .= '           <li class="s-item '.$classes.' '.$submenu_class.' menu-item-'.$item->ID.'"><a href="'.$item->url.'" class="s-icon fa">'.$item->title.' '.$alerts[$item->title].'</a><div class="s-submenu">'.$submenu_item.'</div></li>';

			}
		}

        // Logout
		$items .= '           <li class="s-item menu-item-logout sv-nav-logout"><a href="'.wp_logout_url().'" class="s-icon fa">Log Out</a><div class="s-submenu"><a href="'.wp_logout_url().'">Log Out</a></div></li>';;


	}

	echo $items; 
}









//---------------------------------------------------------------------------
/**
 * Get the link to message an user. This link going on Message Me Button on profile page
 *
 * @param Int - User Id
 * @return String
 *
 *///------------------------------------------------------------------------
function suavaa_get_message_link( $user_id ) {

	if(is_user_logged_in()){
		return wp_nonce_url( bp_loggedin_user_domain() . bp_get_messages_slug() . '/compose/?r=' . bp_core_get_username( $user_id ) );
	}else{
		return get_home_url()."/wp-login.php"; 
	}
}





//---------------------------------------------------------------------------
/**
 * Get the alerts counter notifications, for subscriber users, ONLY PROFILE PAGE
 *
 * @return Array - Counter notifications
 *
 *///-------------------------------------------------------------------------
function get_alerts(){

	$result = array();

	// Show alerts if we are a subscriber, Do not need it for admin users
	if( get_role_user() == "bpuser" ){

		$Notifications = bp_notifications_get_unread_notification_count( bp_loggedin_user_id() );
		$messages = bp_get_total_unread_messages_count( bp_loggedin_user_id() );

		if( $Notifications ) $result["Notifications"] = '<span class="count">'.$Notifications.'</span>';
		if( $messages ) $result["Messages"] = '<span class="count">'.$messages.'</span>';

	}

	return $result;

}

?>