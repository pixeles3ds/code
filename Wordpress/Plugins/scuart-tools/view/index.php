<?php 



add_action('wp_ajax_test_ajax', 'test_ajax' ); // executed when logged in
function test_ajax(){
    echo json_encode([ 
                  'msg' => 'edwwinnnnn', 
                  'status' => 'danger'
    ]);
    wp_die();
}


function scuart_admin_tools(){
    
    require_once plugin_dir_path(__DIR__).'/controller/ScuartProductsPriceFilters.php';

    $screen =  get_current_screen();
    $pluginPageUID = $screen->parent_file;

?>
  <h2 class="nav-tab-wrapper">
    <a href="<?= admin_url('admin.php?page='.$pluginPageUID.'&tab=create')?>" class="nav-tab">Create Filters</a>
    <a href="<?= admin_url('admin.php?page='.$pluginPageUID.'&tab=list')?>" class="nav-tab">List Filters</a>
  </h2>

  <div class="panel-body">
  
<script>
(function($){

data = { action: 'test_ajax', data: 'some value' };

jQuery.post(ajaxurl, data, function(response){
  data = JSON.parse(response);
  console.log(data);
});

})(jQuery);
</script>

    <?php

        attrsVariablesTree();
        
        
    //$activeTab = $_GET['tab'];
    /*

    if ( !isset($activeTab) )
        PriceFilterView::createFormFilter();
    
    if ($activeTab == 'create')
        PriceFilterView::createFormFilter();

    if ($activeTab == 'list')
       PriceFilterView::updateFilters();

     */
    
    ?>
  </div>




<?php
}


function attrsVariablesTree(){

    $products = ScuartProductsPriceFilters::getAllProducts();
        foreach ($products as $key => $product) {

            echo $product->get_id()." - ";
            echo $product->get_name()."<br>";
            $attributes = $product->get_attributes();
              foreach ($attributes as $attr_name => $attr) {
                  echo "--".$attr_name."<br>";                  

                  if( $attr_name != "quantity" ){
                    foreach ($attr["options"] as $val_id => $val) {
                        echo "----".$val."<br>";
                    }
                  }else{
                     echo "----"."<br>"; 
                  }
              }
        }
}

//require_once 'PriceFilter.php';
//require_once 'PriceFilterView.php';


