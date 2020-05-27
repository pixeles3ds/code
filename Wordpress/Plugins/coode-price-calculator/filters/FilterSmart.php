<?php

require_once 'AbstractFilter.php';

class FilterSqf extends AbstractFilter{

    public function __construct(){
        $this->source = 'coode_pc_filterSqf'; // Nombre de la tabla
    }
    

    

    public function getPrice($product, $data){

        
        if (!isset($data['attribute_quantity']) || $data['attribute_quantity'] == null)
            return 0;
        
        if (!isset($data['attribute_size']) || $data['attribute_size'] == null)
            return 0;
        
        
        
        $sizes = explode('x', $data['attribute_size']);
        
        $sizeA = explode(' ', $sizes[0]);
        $sizeA = array_filter(array_map('trim', $sizeA));
        
        $sizeB = explode(' ', $sizes[1]);
        $sizeB = array_filter(array_map('trim', $sizeB));
        
        $size =  reset($sizeA) * reset($sizeB);
        $qty = (int) $data['attribute_quantity'];
        
        $prod = $size * $qty;
        $property = $this->mapProperty($prod);
        
        $filtredPrice = substr($product[$property], 1);
        
        return $filtredPrice * $prod;
        
    }
 
}

?>