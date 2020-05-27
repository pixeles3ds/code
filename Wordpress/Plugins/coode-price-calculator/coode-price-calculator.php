<?php

/**
 * @package Coode
 */

/*
Plugin Name: Coode Price Calculator
Description: Plugin para el cálculo de precios basados en filtros
Version: 1.0
Author: Coodesoft Team
Author URI: https://www.coodesoft.com.ar
License: GPLv2 or later
Text Domain: coode coode_pc
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


function coode_pc_create_table_product(){
    global  $wpdb;
    $table_name = $wpdb->prefix . 'coode_pc_product';

        
    if( $wpdb->get_var( "SHOW TABLES LIKE '$table_name'") != $table_name ) {
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $table_name (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            product_id int(10) NOT NULL,
            attribute varchar(100) NOT NULL,
            value varchar(100) NOT NULL,
            filter varchar(100) NOT NULL,
            filter_id bigint(20) NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        dbDelta( $sql );
    }
     
}

function coode_pc_create_table_filterQty(){
    global  $wpdb;
    $table_name = $wpdb->prefix . 'coode_pc_filterQty';
    if( $wpdb->get_var("SHOW TABLES LIKE '$table_name'") != $table_name ) {
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $table_name (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            a250 varchar(100) NOT NULL,
            a500 varchar(100) NOT NULL,
            a1000 varchar(100) NOT NULL,
            a2500 varchar(100) NOT NULL,
            a5000 varchar(100) NOT NULL,
            a10000 varchar(100) NOT NULL,
            a20000 varchar(100) NOT NULL,
            a250000 varchar(100) NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        dbDelta( $sql );
    }
     
}

function coode_pc_create_table_filterSqf(){
    global  $wpdb;
    $table_name = $wpdb->prefix . 'coode_pc_filterSqf';
    if( $wpdb->get_var("SHOW TABLES LIKE '$table_name'") != $table_name ) {
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $table_name (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            a25 varchar(30) NOT NULL,
            a50 varchar(30) NOT NULL,
            a100 varchar(30) NOT NULL,
            a150 varchar(30) NOT NULL,
            a200 varchar(30) NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        dbDelta( $sql );
    } 
}

function coode_pc_create_table_filterPcs(){
    global  $wpdb;
    $table_name = $wpdb->prefix . 'coode_pc_filterPcs';
    if( $wpdb->get_var("SHOW TABLES LIKE '$table_name'") != $table_name ) {
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE $table_name (
            id bigint(20) NOT NULL AUTO_INCREMENT,
            1a3 varchar(30) NOT NULL,
            4a7 varchar(30) NOT NULL,
            8a15 varchar(30) NOT NULL,
            16a30 varchar(30) NOT NULL,
            31a50 varchar(30) NOT NULL,
            51a100 varchar(30) NOT NULL,
            PRIMARY KEY (id)
        ) $charset_collate;";

        dbDelta( $sql );
    }     
}

register_activation_hook( __FILE__, 'coode_pc_install' );
function coode_pc_install(){
    
	coode_pc_create_table_product();
    coode_pc_create_table_filterQty();
    coode_pc_create_table_filterSqf();
    coode_pc_create_table_filterPcs();
}

/*
add_action('admin_enqueue_scripts', 'cu_load_stylesheet' );
function cu_load_stylesheet($hook){
	if($hook != 'toplevel_page_global_custom_upload')
  	return;
	wp_enqueue_style( 'customUploadPanelCSS',  plugins_url('/css/uploadPanel.css', __FILE__) );
}

*/


require_once 'db/Product.php';
require_once 'db/Filter.php';
require_once 'filters/FilterQty.php';
require_once 'filters/FilterSqf.php';
require_once 'filters/FilterPcs.php';
require_once 'PriceCalculator.php';
require_once 'admin/index.php';
