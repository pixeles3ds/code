<?php 

require_once 'AbstractFilter.php';

class FilterPCs extends AbstractFilter{
    
    public function __construct(){
        $this->source = 'coode_pc_filterPcs';
    }

    public function getProperties(){
        return [
            '1a3' => '1 to 3', 
            '4a7' => '4 to 7', 
            '8a15' => '8 to 15', 
            '16a30' => '16 to 30', 
            '31a50' => '31 to 50', 
            '51a100' => '51 to 100',
        ];
    }    
    
    public function mapProperty($value){
        if ($value >=1 && $value <=3)
            return '1a3';

        if ($value >=4 && $value <=7)
            return '4a7';

        if ($value >=8 && $value <=15)
            return '8a15';

        if ($value >=16 && $value <=30)
            return '16a30';

        if ($value >=31 && $value <=50)
            return '31a50';

        return '51a100';
    }
    
    public function getPrice($product, $data){
       if (!isset($data['attribute_quantity']) || $data['attribute_quantity'] == null)
            return 0;
        
        $property = $this->mapProperty($data['attribute_quantity']);
        $filtredPrice = substr($product[$property], 1);
        
        return $filtredPrice * $data['attribute_quantity'] ;
    }
    
}

?>