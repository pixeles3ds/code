<?php

/* 

    public function getProductById($id){
        if (!$id)
            throw new Exception('El id es inválido', 1);

        $product = wc_get_products($id);
        $product = !empty($product) ? $product[0] : null;

        if (!$product)
            throw new Exception('No se encontró ningun producto con el id actual', 1);

        return $product;       
    }
    
    static function getAllProducts(){
        $args = array('status' => 'published');
        return wc_get_products($args);
    }
    
    
*/


class PriceFilter {
    
    
    public function __construct(){

        add_action( 'wp_ajax_cp_load_product_attributes', array($this, 'load_product_attributes') );
        add_action( 'wp_ajax_nopriv_cp_load_product_attributes', array($this, 'load_product_attributes') );

        add_action( 'wp_ajax_cp_load_attribute_values', array($this, 'load_attribute_values') );
        add_action( 'wp_ajax_nopriv_cp_load_attribute_values', array($this, 'load_attribute_values') );

        add_action( 'wp_ajax_cp_load_filter_table', array($this, 'load_filter_table') );
        add_action( 'wp_ajax_nopriv_cp_load_filter_table', array($this, 'load_filter_table') );
        
        add_action( 'wp_ajax_cp_process_new_filter', array($this, 'process_new_filter') );
        add_action( 'wp_ajax_nopriv_cp_process_new_filter', array($this, 'process_new_filter') );
    
        add_action( 'wp_ajax_cp_delete_filter', array($this, 'delete_filter') );
        add_action( 'wp_ajax_nopriv_cp_delete_filter', array($this, 'delete_filter') );
        
    }
    
    static function getFiltersLabel(){
        return [
            'qty' => 'By quantity', 
            'sqf' => 'By sqare feet',
            'pcs' => 'By pieces',
        ];  
    }
    

    static function getAllProducts(){

        
        $args = array(
            'post_type' => 'product',
            'posts_per_page' => -1,
            'post_status'    => 'publish',
        );

        $wp_query = new WP_Query($args);
        $posts = $wp_query->posts;
        $products = [];
        foreach($posts as $post){
            $products[] = new WC_Product($post->ID);
        }
        return $products;
    }    
    
    public function getProductById($id){

        $args = array(
            'post_type' => 'product',
            'posts_per_page' => -1,
            'post_status'    => 'publish',
            'p' => $id,
        ); 
        $query = new WP_Query($args);

        if (!$query)
            throw new Exception('No se encontró ningun producto con el id actual', 1);

        $product = new WC_Product($query->post->ID);
        return $product;
    }
    
    public function load_product_attributes(){
        $id = intval($_POST['id']);
        $product = $this->getProductById($id);
        $attributes = array_keys($product->get_attributes());
        //echo json_encode($product->get_attribute('size'));
        echo json_encode($attributes);
        wp_die();
    }
    
    public function load_attribute_values(){
        $attribute = $_POST['attribute'];
        $id = intval($_POST['product']);
        $product = $this->getProductById($id);

        if ( !strlen($attribute) )
            throw new Exception('El atributo pasado por parámetro no es válido', 1);

        $values = $product->get_attribute($attribute);
        $values = explode('|', $values);

        echo json_encode($values);
        wp_die();
   
    }
    
    public function load_filter_table(){
        $filter = $_POST['filter'];
        if ( !strlen($filter) )
            throw new Exception('El filtro pasado por parámetro no es válido', 1);

        $filterClassName = 'Filter' . ucfirst(trim($filter));
        if (!class_exists($filterClassName))
            throw new Exception('El filtro pasado por parámetro no existe', 1);

        $filter = new $filterClassName();
        echo json_encode($filter->getProperties());
        wp_die();
    }   
    
    public function process_new_filter(){
        $params = array();
        parse_str($_POST['data'], $params);
        
        $formProduct = $params['Product'];
        $formFilter = $params['Filter'];
        
        if ( !$formProduct || !$formFilter || !$formProduct['id'] || !$formProduct['attribute'] || !$formProduct['attribute_value'] ){
            echo json_encode([ 
                'msg' => 'El formulario tiene campos incompletos', 
                'status' => 'danger'
            ]);
            wp_die();
        }
        
        $filterClassName = 'Filter' . ucfirst(trim($formProduct['filter']));
        
        if ( !class_exists($filterClassName) ){
            echo json_encode([ 
                'msg' => 'El formulario tiene campos incompletos. No existe el filtro seleccionado', 
                'status' => 'danger'
            ]);
            wp_die();
        }

        
        $filter = new $filterClassName();
        $toSave = $filter->prepareDataToSave($formFilter);
        
        $result = Filter::add($filter->source, $toSave);
        
        if ($result === false){
           echo json_encode([ 
                'msg' => 'Se produjo un error inesperado. No se pudo guardar el filtro', 
                'status' => 'danger'
            ]);
            wp_die();
        }
        
        
        $product = [];
        $product['product_id'] = $formProduct['id'];
        $product['attribute'] = $formProduct['attribute'];
        $product['value'] = $formProduct['attribute_value'];
        $product['filter'] = ucfirst(trim($formProduct['filter']));
        $product['filter_id'] = $result;
        
        $result = Product::add($product);
        
        if ($result === false){
           $response = [ 
                'msg' => 'Se produjo un error inesperado. No se pudo vincular el producto', 
                'status' => 'danger'
            ];
        } else{
            $response = [ 
                'msg' => 'El filtro se creó exitosamente!', 
                'status' => 'success'
            ];
        }
        
        echo json_encode($response);
        wp_die();
        
        
    }

    public function delete_filter(){
        $product_id = intval($_POST['product']);
        
        if ( !$product_id ){
            echo json_encode([
                'status' => 'danger',
                'msg' => 'Se produjo un error al eliminar el filtro!',
            ]);
            wp_die();
        }
        
        $result = Product::delete($product_id);
        if ($result){
            echo json_encode([
                'status' => 'success',
                'product' => $product_id,
            ]);
        } else{
             echo json_encode([
                'status' => 'danger',
                'msg' => 'Se produjo un error al eliminar el filtro!',
            ]);
        }
        wp_die();
    }
    
}

$priceFilter = new PriceFilter();