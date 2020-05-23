<?php
ob_start();

	if ( is_user_logged_in() ) {	
		if ( wp_redirect( get_member_domain()."/profile" ) ) {
			exit;
		}

	}else{
		if ( wp_redirect( get_home_url()."/wp-login.php" ) ) {
			exit;
		}
	}

ob_end_flush();

?>