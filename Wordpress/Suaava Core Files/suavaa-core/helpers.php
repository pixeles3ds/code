<?php 

/*

Functions on this page:

	
	pr()
	get_string_between()

	
*/


//---------------------------------------------------------------------------
// Debug Purpose, print obj's and arrays as a tree
//---------------------------------------------------------------------------
function pr( $data){
	echo "<pre>";
	print_r($data);
	echo "</pre>";
}




//---------------------------------------------------------------------------
// Format string
//---------------------------------------------------------------------------
function trim_str( $data){
	$data = str_replace("\t", '', $data); // remove tabs
	$data = str_replace("\n", '', $data); // remove new lines
	$data = str_replace("\r", '', $data); // remove carriage returns
	$data = trim($data); // trim
	return $data;
}




//---------------------------------------------------------------------------
/**
 * Get the string between two strings
 *
 * @return String
 *
 *///-------------------------------------------------------------------------
function get_string_between($string, $start, $end){
	$string = ' ' . $string;
	$ini = strpos($string, $start);
	if ($ini == 0) return '';
	$ini += strlen($start);
	$len = strpos($string, $end, $ini) - $ini;
	return substr($string, $ini, $len);
}






//---------------------------------------------------------------------------
/**
 * Execute SQL Code
 *
 *///------------------------------------------------------------------------
function execute_sql( $sql ) {
	global $wpdb;

	$array = explode(";", $sql);

	foreach ($array as $query) {
		$wpdb->query( 
			$wpdb->prepare( $query, 1 )
		);
	}

}






//---------------------------------------------------------------------------
/**
 * Execute SQL Code
 *
 * @return Array - Array of the query
 *
 *///------------------------------------------------------------------------
function query_sql( $sql ) {

	global $wpdb;
	
	$result = $wpdb->get_results( 
		$wpdb->prepare( $sql, 1 )
	);

	return $result;

}


?>