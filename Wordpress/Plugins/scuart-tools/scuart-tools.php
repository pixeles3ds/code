<?php

/**
 * @package Coode
 */

/*
Plugin Name: Scuart Tools
Description: Plugin general con herramientas para woocomerce
Version: 1.0
Author: Scuart
Author URI: https://www.scuart.com
License: GPLv2 or later
Text Domain: scuart scuart_pc
*/

// Make sure we don't expose any info if called directly
if ( !function_exists( 'add_action' ) ) {
	echo 'Hi there!  I\'m just a plugin, not much I can do when called directly.';
	exit;
}

/*
 * ACTIVACIÓN - Se crean las tablas de productos y de los filtros
 */

require_once( ABSPATH . 'wp-admin/includes/upgrade.php' );

// Install Plugin
register_activation_hook( __FILE__, 'scuart_install' );
function scuart_install(){
	require_once 'model/plugin.php';
	ScuartPlugin::scuart_install();   
}

// Uninstall Plugin
register_deactivation_hook( __FILE__, 'scuart_uninstall' );
function scuart_uninstall(){
	require_once 'model/plugin.php';
	ScuartPlugin::scuart_uninstall();
}



//--------------------------------------------------------------------------
//  ADMIN
//--------------------------------------------------------------------------

// Add CSS to Admin
add_action( 'admin_head', 'scuart_admin_load_css');
function scuart_admin_load_css() {	
	if( get_current_screen()->parent_file == "scuart_tools" ){
		wp_enqueue_style( 'scuart_bootstrap_css', plugins_url('view/css/bootstrap.min.css', __FILE__), array(), '4.1.3');
		wp_enqueue_style( 'scuart__css', plugins_url('view/css/scuart_style.css', __FILE__), array(), '1.0');		
	}    
}

// Add JS to Admin
add_action('admin_enqueue_scripts', 'scuart_admin_load_scripts' );
function scuart_admin_load_scripts($hook) {
	if( get_current_screen()->parent_file == "scuart_tools" ){
    	wp_enqueue_script( 'createFilter', plugins_url('view/js/scuart.js', __FILE__), array('jquery'), '1.1', true);
	}
}



//--------------------------------------------------------------------------
//  ADMIN MENUS
//--------------------------------------------------------------------------

// Menu Scuart LeftSide
add_action('admin_menu', 'scuart_admin_menu');
function scuart_admin_menu(){
	add_menu_page('Scuart Tools', 'Scuart', 'manage_options', 'scuart_tools', 'scuart_admin_tools');
}





require_once 'helpers.php';
/*
require_once 'db/Product.php';
require_once 'db/Filter.php';
require_once 'filters/FilterQty.php';
require_once 'filters/FilterSqf.php';
require_once 'filters/FilterPcs.php';
require_once 'PriceCalculator.php';
*/
require_once 'view/index.php';
