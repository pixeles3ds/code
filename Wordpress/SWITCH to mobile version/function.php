<?php

function mobile_page_template( $template ) {
	if ( is_front_page() && wp_is_mobile() ) {
		$new_template = locate_template( array( 'mobile.php' ) );
		if ( '' != $new_template ) {
		return $new_template ;
		}
	}	
	return $template;
}
add_filter( 'template_include', 'mobile_page_template', 99 );

?>