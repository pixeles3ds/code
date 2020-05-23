<?php
/**
 * @package Boss Child Theme
 * The parent theme functions are located at /boss/buddyboss-inc/theme-functions.php
 * Add your own functions in this file.
 */

/**
 * Sets up theme defaults
 *
 * @since Boss Child Theme 1.0.2
 */
function boss_child_theme_setup()
{
  /**
   * Makes child theme available for translation.
   * Translations can be added into the /languages/ directory.
   * Read more at: http://www.buddyboss.com/tutorials/language-translations/
   */

  // Translate text from the PARENT theme.
  load_theme_textdomain( 'boss', get_stylesheet_directory() . '/languages' );

  // Translate text from the CHILD theme only.
  // Change 'boss' instances in all child theme files to 'boss_child_theme'.
  // load_theme_textdomain( 'boss_child_theme', get_stylesheet_directory() . '/languages' );

}
add_action( 'after_setup_theme', 'boss_child_theme_setup' );

/**
 * Enqueues scripts and styles for child theme front-end.
 *
 * @since Boss Child Theme  1.0.0
 */
function boss_child_theme_scripts_styles()
{
  /**
   * Scripts and Styles loaded by the parent theme can be unloaded if needed
   * using wp_deregister_script or wp_deregister_style.
   *
   * See the WordPress Codex for more information about those functions:
   * http://codex.wordpress.org/Function_Reference/wp_deregister_script
   * http://codex.wordpress.org/Function_Reference/wp_deregister_style
   **/

  /*
   * Styles
   */
  wp_deregister_style('boss-child-custom'); 
  wp_register_style( 'boss-child-custom',  get_stylesheet_directory_uri() . '/css/custom.css', array(), ver()  );
  wp_enqueue_style( 'boss-child-custom');
}
add_action( 'wp_enqueue_scripts', 'boss_child_theme_scripts_styles', 9999 );

function boss_child_theme_login_styles() {
	wp_deregister_style('boss-child-custom-login'); 
	wp_register_style( 'boss-child-custom-login',  get_stylesheet_directory_uri() . '/css/custom-login.css', array(), ver()  );
	wp_enqueue_style( 'boss-child-custom-login');
}
add_action( 'login_enqueue_scripts', 'boss_child_theme_login_styles', 9999 );



//---------------------------------------------------------------------------
//  Dequeue styles URL without SSL and reload with SSL 
//---------------------------------------------------------------------------
function custom_dequeue() {

    wp_dequeue_style('redux-google-fonts-boss-options');
	wp_deregister_style('redux-google-fonts-boss-options');

	wp_register_style( 'redux-google-fonts-boss-options',  'https://fonts.googleapis.com/css?family=Pacifico%3A400%7CLato%3A400%2C700%7CArimo%3A700%7CSource+Sans+Pro%3A700&subset=latin', array(), '1.0'  );
	wp_enqueue_style( 'redux-google-fonts-boss-options');

}

add_action( 'wp_head', 'custom_dequeue', 999999 );



/******************************************************************************/
/****************************** CUSTOM FUNCTIONS ******************************/
/******************************************************************************/





//---------------------------------------------------------------------------
// Force browser refresh img, js and css with new versions
//---------------------------------------------------------------------------
function ver(){
	return "2.1.367";
}




/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------

                                    		***  INIT CONFIGURATION  *** 

----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/


//---------------------------------------------------------------------------
// call id user logged variable
//---------------------------------------------------------------------------
wp_get_current_user();



//---------------------------------------------------------------------------
// Set avatar sizes
//---------------------------------------------------------------------------
define ( 'BP_AVATAR_FULL_WIDTH', 600 );
define ( 'BP_AVATAR_FULL_HEIGHT', 600 );
define ( 'BP_AVATAR_ORIGINAL_MAX_WIDTH', 600 );
define ( 'BP_AVATAR_ORIGINAL_MAX_HEIGTH', 600 );
define ( 'BP_AVATAR_ORIGINAL_MAX_FILESIZE', 1024 * 1024 * 5 );






/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------

                            		***  FUNCTIONS, ACTIONS, FILTERS Loaders  *** 

----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/

//---------------------------------------------------------------------------
// Load functions for BUDDYPRESS system and general web changes
//---------------------------------------------------------------------------
$bp_system = 'suavaa-core/buddypress-system.php';
include $bp_system;

add_action( 'template_redirect', 'member_level' );
add_action( 'template_redirect', 'register_ladies',99 );
add_action( 'wp_head', 'register_get_params',99 );
add_action( 'bp_setup_nav', 'bbg_change_profile_tab_order', 999 );
add_action( 'bp_core_signup_user', 'bp_auto_activate', 100, 1);
add_action( 'bp_core_activated_user', 'bp_auto_login', 20, 3 );
add_action( 'bp_core_signup_user', 'get_form_location_fields', 99, 1);
add_action( 'bp_core_signup_user', 'change_level_on_registration', 99, 1);
add_action( 'xprofile_updated_profile', 'get_form_location_fields', 99, 5);
add_action( 'wp_head', 'locations_form_js',999 );
add_action( 'wp_head', 'refer_field_js',999 );
add_action( 'admin_init', 'redirect_non_admin_user', 99 );

add_filter( 'script_loader_src', 'agnostic_script_loader_src', 20,2);
add_filter( 'style_loader_src', 'agnostic_style_loader_src', 20,2);
//add_filter( 'gmw_default_form_values', 'geomygp_disbale_location_free_user', 99 );
add_filter( 'gmw_internal_cache_enabled', 'delete_geomywp_caching', 99, 1); 
add_filter( 'gmw_map_element_1', 'gmw_disable_scroll_zoom', 99 );
add_filter( 'login_redirect', 'admin_default_page',99, 3 );
add_filter( 'login_message', 'add_logo_login_form', 99);
add_filter( 'body_class', 'add_body_class', 99);
add_filter( 'wp_get_nav_menu_items', 'fix_nav_menu_classes', 99, 3 );
add_filter( 'wp_nav_menu_items', 'add_admin_link', 99, 2);
add_filter( 'bp_user_query_uid_clauses', 'filtering_memberpress', 1, 2 );
add_filter( 'bp_core_signup_send_activation_key', create_function('','return false;') ); // Disable send activation Key
add_filter( 'pmpro_levels_array', 'levels_hide_list', 99);
add_filter( 'pmpro_checkout_level', 'levels_disable_checkout', 99 );
add_filter( 'bp_after_has_profile_parse_args', 'xprofile_hide_fields', 99 ); // Hide referrer field


// cover settings
remove_filter( 'bp_before_xprofile_cover_image_settings_parse_args', 'buddyboss_cover_image_settings', 10, 1 );
remove_filter( 'bp_before_groups_cover_image_settings_parse_args', 'buddyboss_cover_image_settings', 10, 1 );
add_filter( 'bp_before_xprofile_cover_image_settings_parse_args', 'bb_cover_image_settings', 10, 1 );
add_filter( 'bp_before_groups_cover_image_settings_parse_args', 'bb_cover_image_settings', 10, 1 );

// avatar
add_filter( 'bp_core_mysteryman_src', 'myavatar_add_default_avatar' );
add_filter( 'bp_core_default_avatar_user', 'myavatar_add_default_avatar' );
add_filter( 'bp_core_fetch_avatar_no_grav', '__return_true' );

// general JPEG quality
add_filter( 'jpeg_quality', create_function( '', 'return 95;' ) );




//---------------------------------------------------------------------------
// Load helpers functions
//---------------------------------------------------------------------------
$helpers = 'suavaa-core/helpers.php';
include $helpers;



//---------------------------------------------------------------------------
// Load users getters functions
//---------------------------------------------------------------------------
$users_getters = 'suavaa-core/user-getters.php';
include $users_getters;

add_filter( 'bp_get_member_name', 'get_completed_name', 99 );


//---------------------------------------------------------------------------
// Load functions for the NEW CUSTOM Profile page
//---------------------------------------------------------------------------
$profile_page = 'suavaa-core/profile-page.php';
include $profile_page;

add_action( 'wp_enqueue_scripts', 'profile_style_scripts',99);


//---------------------------------------------------------------------------
// Load functions for the MEMBERS PANEL ADMIN
//---------------------------------------------------------------------------
$members_page = 'suavaa-core/members-page.php';
include $members_page;

add_action( 'init', 'remove_filters_user_clauses' ,10 );
add_action( 'template_redirect', 'members_actions_post_data',9999 );
add_action( 'wp_head', 'members_inject_js',99 );

add_filter( 'bp_user_query_uid_clauses', 'filtering_members_page_admin', 99, 2 );









//---------------------------------------------------------------------------
// Define the default tab component according to user level
// If is an inactive user, the main component will be profile
//---------------------------------------------------------------------------
  
if( get_level() == "inactive" || get_level() == "premium"){
	define('BP_DEFAULT_COMPONENT', 'profile' );  
}





/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------

                            					***  REFFERALS   *** 

----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/


//---------------------------------------------------------------------------
// 	Setup referrals tab on buddypress 
//---------------------------------------------------------------------------
function add_refer_tabs() {
	
	global $bp;
  	
  	// If i am the owner profile or admin show referrals tab and page
  	if( bp_displayed_user_id() == bp_loggedin_user_id() || get_role_user() == "admin" ){
  	
		bp_core_new_nav_item( array(
			'name'                  => 'Referrals',
			'slug'                  => 'referral',
			'parent_url'            => $bp->displayed_user->domain,
			'parent_slug'           => $bp->profile->slug,
			'screen_function'       => 'refer_screen',			
			'position'              => 200,
		) );

	}

}
add_action( 'bp_setup_nav', 'add_refer_tabs', 100 );


//---------------------------------------------------------------------------
// 	Add referrals plugin
//---------------------------------------------------------------------------
function refer_screen() {
    add_action( 'bp_template_content', 'refer_screen_content' );
    bp_core_load_template( apply_filters( 'bp_core_template_plugin', 'members/single/plugins' ) );
}

//---------------------------------------------------------------------------
// 	Call template for referrals page
//---------------------------------------------------------------------------
function refer_screen_content() { 
	get_template_part( 'refer' );
}






/*
================================================================================================================

----------------------------------------------------------------------------------------------------------------

                            					***   MESSAGES   *** 

----------------------------------------------------------------------------------------------------------------

================================================================================================================
*/


//---------------------------------------------------------------------------
// 	Retrun array with the free system messages
//---------------------------------------------------------------------------
function free_messages(){

    $list = array(
    	"I am interested in you",
    	"I would like to talk to you"
    );

 	return $list;   

}

//---------------------------------------------------------------------------
// 	If the content of the message is a prewritten message (free)
//---------------------------------------------------------------------------
function is_free_message( $content ){

        $include = free_messages();

        if( in_array( $content, $include) ){
        	return true;
        }else{
        	return false;
        }

}

//---------------------------------------------------------------------------
// 	If the subject of the message is a system message
//---------------------------------------------------------------------------
function is_free_message_subject( $subject ){

        $subject = strtolower( $subject );
        if( $subject == "system message" || $subject == "re: system message" ){
	        return true;
        }else{
        	return false;
        }

}

//---------------------------------------------------------------------------
// 	Render HTML and Javascript code to add buttos of prewritten messages
//---------------------------------------------------------------------------
// render html tags for prewritten 
function prewritten_msg_html(){
			
	$class = " closed";
	$buttons = '';

	foreach ( free_messages() as $item ) {     
		$buttons.= '<div class="btn_msg">'.$item.'</div>';
	}



	if( get_level() == "inactive" ){

		$class = " inactive";		

		// Disbale textbox for messages
		echo '	
			<script type="text/javascript">
				$(function() {							    
			    	$("input[name=\'subject\']").attr("readonly",true);
			    	$("textarea[name=\'content\']").attr("readonly",true);
				});
			</script>	
		';

	}



	$html = '

	<div class="prewritten_msg_content'. $class .'">
		
		<span id="arrow" class="fa-custom arrow-up"></span>
		<span id="arrow" class="fa-custom arrow-down"></span>

		<div class="prewritten_info">System Messages! Free users can read and write prewritten messages</div>
		<div class="prewritten_buttons">
			'. $buttons .'
		</div>
	</div>
	
	<script type="text/javascript">

		$(function() {			
		    
		    $(".btn_msg").click(function(){
		    	$("input[name=\'subject\']").val("System Message");
		    	$("textarea[name=\'content\']").val($(this).html());
		    });


		    $(".prewritten_info, .fa-custom").click(function(){
				if( $( ".prewritten_msg_content" ).hasClass( "closed" ) ) { $( ".prewritten_msg_content" ).removeClass( "closed" ); }
				else{ $( ".prewritten_msg_content" ).addClass( "closed" ); }
		    });  	

		});

	</script>	

	';


	
	echo $html;


}


//---------------------------------------------------------------------------
// 	Before send any message filter inactive users messages
//---------------------------------------------------------------------------
function message_before_send( $msg ) { 
	
	//if( get_level() == "inactive" ){
	if( get_level() == "inactive" ){
		
		if( !is_free_message_subject( $msg->subject ) || !is_free_message( $msg->message )  ){

			// if message is a reply else a new compose
	        if( strtolower( $msg->subject ) == "re: system message" ){ // Reply

	        	echo '<div class="unabled_to_send"> <a class="unpaid_message" href="'.get_home_url().'/membership-account/membership-levels/' .'">Upgrade your account to send messages!</a> <br></div>';
		        die;

	        }else{ // Compose

				if ( wp_redirect( get_home_url()."/membership-account/membership-levels/" ) ) {
		    		exit;
		    	}

	        }



		}

	}
	
}; 
add_action( 'messages_message_before_save', 'message_before_send', 10, 1 ); 







?>