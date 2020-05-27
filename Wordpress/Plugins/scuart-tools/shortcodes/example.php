public function shortcode_example( $attributes ) {
	ob_start();
	require_once( dirname( __DIR__ ) . '/views/shortcode-example.php' );
	$output = ob_get_clean();
	
	return $output;
}