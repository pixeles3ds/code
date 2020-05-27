<?php

class Product{

    const TABLE = 'coode_pc_product';
    
    static function table(){
        global $wpdb;
        return $wpdb->prefix . self::TABLE;
    }
    
    static function getById($id){
        global $wpdb;

        $queryStr = 'SELECT * FROM '. self::table() .' WHERE product_id=%d';
        $query = $wpdb->prepare($queryStr, array($id));
      
        return $wpdb->get_results($query, ARRAY_A);
    }
    
    
    static function getAll(){
        global $wpdb;
        
        $queryStr = 'SELECT * FROM ' .self::table();
        return $wpdb->get_results($queryStr, ARRAY_A);
    }
    
    static function getAllExtended($pretty = true){
        global $wpdb;
        
        $queryStr = 'SELECT * FROM ' .self::table();
        $rows = $wpdb->get_results($queryStr, ARRAY_A);
        
        foreach($rows as $key => $row){

            $className = 'Filter'.ucfirst($row['filter']);
            $row['class'] = $className;
            
            $filter = new $className();
            $filterValues = Filter::get($filter->source, $row['filter_id']);
            $filterValues = $filterValues[0];
            if ($pretty){
                $label = $filter->getProperties();
                $new = [];
                foreach($filterValues as $k => $value){
                    $prettyKey = $label[$k] ? $label[$k] : $k;
                    $new[$prettyKey] = $value;
                }
                $rows[$key]['filter_values'] = $new;
            } else{
                $rows[$key]['filter_values'] = $filterValues;
            }
        }
        
        return $rows;
    }
    
    static function add($data){
        global $wpdb;
        
        $format = ['%d', '%s', '%s', '%s', '%d'];
        $result = $wpdb->insert(self::table(), $data, $format);
        
        if  ($result) 
            return $wpdb->insert_id;
            
        return false;
    }
    
    static function delete($id){
        global $wpdb;

        $queryStr = 'SELECT * FROM '. self::table() .' WHERE id=%d';
        $query = $wpdb->prepare($queryStr, array($id));
      
        $element = $wpdb->get_results($query, ARRAY_A);
        $element = $element[0];
        
        $wpdb->query('START TRANSACTION');
        
        $classname = 'Filter'.ucfirst($element['filter']);
        $filter = new $classname();
        $filterTable = $wpdb->prefix . $filter->source;
        
        //throw new Exception(json_encode($id), 1);
        $result = $wpdb->delete( self::table(), ['id' => $id], ['%d'] );
        $related = $wpdb->delete( $filterTable, ['id' => $element['filter_id']], ['%d'] );

        if ($result !== false && $related !== false){
          $wpdb->query('COMMIT');
          return true;
        } else{
          $wpdb->query('ROLLBACK');
          return false;
        }
    }
    
    static function getProperties(){
        global $wpdb;
        
        $queryStr = 'SELECT * FROM ' .self::table(). ' LIMIT 1';
        $first = $wpdb->get_results($queryStr, ARRAY_A);
        return array_keys($first[0]);
    }
}

?>