<?php

require_once 'AbstractFilter.php';

class FilterSqf extends AbstractFilter{

    public function __construct(){
        $this->source = 'coode_pc_filterSqf';
    }
    
    public function getProperties(){
        return [
            'a25'  => '25', 
            'a50'  => '50', 
            'a100' => '100', 
            'a150' => '150',
            'a200' => '200'
        ];
    }
    
    public function mapProperty($value){
        if ($value <= 25)
            return 'a25';
        
        if ($value <= 50)
            return 'a50';
        
        if ($value <= 100)
            return 'a100';
        
        if ($value <= 150)
            return 'a150';
        
        return 'a200';
        
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