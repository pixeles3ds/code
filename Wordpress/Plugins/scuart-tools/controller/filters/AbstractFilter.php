<?php 


abstract class AbstractFilter{
    
    public $source;
    
    public abstract function getPrice($product, $data);
    
    public abstract function mapProperty($value);
 
    public abstract function getProperties();
 
    
    public function prepareDataToSave($data){
        $toSave = [];
        foreach($data as $key => $value){
            $value = (strlen($value) == 0) ? '0.0' : $value;
            $toSave[$key] = ( strpos($value, '$') === false ) ? '$'.$value : $value;
        }
        return $toSave;
    }
}

?>