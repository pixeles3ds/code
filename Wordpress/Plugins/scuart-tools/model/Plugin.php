<?php

class ScuartPlugin{

    
    static function scuart_create_table_product(){
        global  $wpdb;
        $table_name = $wpdb->prefix . 'scuart_product';

            
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

    static function scuart_create_table_filterQty(){
        global  $wpdb;
        $table_name = $wpdb->prefix . 'scuart_filterQty';
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

    static function scuart_create_table_filterSqf(){
        global  $wpdb;
        $table_name = $wpdb->prefix . 'scuart_filterSqf';
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

    static function scuart_create_table_filterPcs(){
        global  $wpdb;
        $table_name = $wpdb->prefix . 'scuart_filterPcs';
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


    function scuart_install(){        
        
        self::scuart_create_table_product();
        self::scuart_create_table_filterQty();
        self::scuart_create_table_filterSqf();
        self::scuart_create_table_filterPcs();
    }

    function scuart_uninstall(){

    }


}

?>