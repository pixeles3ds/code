<?php


class PriceCalculator{
    
    
    private $filters = [];
    
    public function __construct(){
        add_action('wp_ajax_rightpress_live_product_price_update', array($this, 'update_price'));
        add_action('wp_ajax_nopriv_rightpress_live_product_price_update', array($this, 'update_price'));
        add_action('woocommerce_before_calculate_totals', array($this, 'custom_price_to_cart_item'), 99 );
       // add_action('woocommerce_coode_show_subtotal', array($this, 'custom_price_preview'), 60);
    }
    
    
    private function filterAttributeField($attribute){
        return ( strpos($attribute, 'attribute') !== false ) ? $attribute : 'attribute_' . strtolower($attribute);
        
    }
    
    private function getDbFilter($products, $data){
        //$product = wc_get_product($product_id);
        
        foreach($products as $product){
            $attribute = $this->filterAttributeField($product['attribute']);

            if ( isset($data[$attribute]) && strtolower($data[$attribute]) == strtolower($product['value'])){
                $filterClassName = 'Filter' . $product['filter'];
                if ( !class_exists($filterClassName) )
                    return null;
                
                return $filterClassName;
            }
        }
        return null;
    }
    
    private function filterProductByAttr($products, $data){
        foreach($products as $product){
            $attribute = $this->filterAttributeField($product['attribute']);
            
            if ( isset($data[$attribute]) && strtolower($data[$attribute]) == strtolower($product['value']))
                return $product;
            
        }
        return null;        
    }
    
    public function update_price(){
        $dataStr = $_POST['data'];
        parse_str($dataStr, $data);


        $products = Product::getById($data['product_id']);

        //$filterClassName = $this->getDbFilter($products, $data);
        $product = $this->filterProductByAttr($products, $data);
        
        if ($product){
            $filterClassName = 'Filter' . $product['filter'];
            $calculator = new $filterClassName();
            $filter = Filter::get($calculator->source, $product['filter_id']);
            $filter = $filter[0];
            $price = ($filter) ? $calculator->getPrice($filter, $data) : 0;
        } else {
            $price = 0;
        }
        
        $coode_result = [
                'label_html'    => $price,
                'result'        => 'success',
                'display'       => true,
            ];
        echo json_encode( $coode_result );
        wp_die();
    }
    
    
    public function custom_price_to_cart_item($cart_object){
        if( !WC()->session->__isset( "reload_checkout" )) {
            foreach ( $cart_object->cart_contents as $key => $value ) {
                //for woocommerce version lower than 3
                //$value['data']->price = $value["custom_price"];
                //for woocommerce version +3

                $metadata = $value;
                $product_id = $metadata['product_id'];

                $product = wc_get_product($product_id);

                // Unable to load product
                if (!$product) 
                     echo json_encode(array(
                        'result'    => 'error',
                        'message'   => 'Unable to load product.',
                    ));

                $data = $metadata['variation'];
                $data['product_id'] = $product_id;
                
                $products = Product::getById($data['product_id']);
                $product = $this->filterProductByAttr($products, $data);

                if ($product){
                    $filterClassName = 'Filter' . $product['filter'];
                    $calculator = new $filterClassName();
                    $filterRow = Filter::get($calculator->source, $product['filter_id']);
                    
                    $filterRow = $filterRow[0];
                    //throw new Exception (json_encode($filterRow), 1);
                    $price = (isset($filterRow)) ? $calculator->getPrice($filterRow, $data) : 0;
                    $value['data']->set_price($price);
                } else {
                    throw new Exception('Not product filtered', 1);
                }
                        
            }
        }
    }
    
    public function custom_price_preview($cart_object){
         $result = 0;
    }
}

$priceCalculator = new PriceCalculator();

