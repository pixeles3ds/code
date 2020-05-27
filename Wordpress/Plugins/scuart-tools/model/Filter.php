<?php

class Filter{

    
    static function get($table, $id){
        global $wpdb;

        $table  = trim($table, ' ');

        if (!strpos($table, 'filter'))
            throw new Exception('SQL Injection attack detected. name changed! '. $table, 1);

        $table = $wpdb->prefix . $table;
        $queryStr = 'SELECT * FROM '. $table .' WHERE id=%d';
        $query = $wpdb->prepare($queryStr, array($id));

        return $wpdb->get_results($query, ARRAY_A);
    }

    static function getAllExtended($table){
        global $wpdb;

        $table  = trim($table, ' ');

        if (!strpos($table, 'filter') || strpos($table, ' '))
            throw new Exception('SQL Injection attack detected. param=! '. $table, 1);

        $table = $wpdb->prefix . $table;
        $productTable = $wpdb->prefix . Product::TABLE;
        
        $queryStr = 'SELECT * FROM ' .$table;
        $queryStr.= ' LEFT JOIN ' .$productTable;
        $queryStr.= ' ON '.$table. '.id='.$productTable.'.filter_id';
        
        return $wpdb->get_results($queryStr, ARRAY_A);
    }
    
    static function add($table, $data){
        global $wpdb;

        $table  = trim($table, ' ');
        if (!strpos($table, 'filter'))
            throw new Exception('SQL Injection attack detected. name changed! '. $table, 1);

        $table = $wpdb->prefix . $table;
        
        return $wpdb->insert($table, $data) ? $wpdb->insert_id : false;
    }

}
?>