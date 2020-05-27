<?php /* Template Name: json */
	
 $resultados = $wpdb->get_results( " SELECT post_title t, post_date d FROM wp_posts WHERE post_type = 'post'  AND post_status <> 'auto-draft' order by d DESC LIMIT 3 " );
 
 $json = json_encode( (array)$resultados );
  
 print_r(  $json );
 
?>