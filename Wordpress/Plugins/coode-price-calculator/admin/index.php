<?php 

add_action( 'admin_head', 'bootstrap_css');
function bootstrap_css() {
	wp_enqueue_style( 'bootstrap_css', 'https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css', array(), '4.1.3'); 
}


add_action('admin_enqueue_scripts', 'cu_load_scripts' );
function cu_load_scripts() {
    wp_enqueue_script( 'createFilter', plugins_url('/js/createFilter.js', __FILE__), array('jquery'), '1.1', true);
}

add_action('admin_menu', 'pc_admin_menu');
function pc_admin_menu(){
	add_menu_page('Price Calculator', 'Price Calculator', 'manage_options', 'global_price_calculator', 'global_price_calculator_admin');
}


function global_price_calculator_admin(){
    $screen =  get_current_screen();
	$pluginPageUID = $screen->parent_file;

?>
  <h2 class="nav-tab-wrapper">
    <a href="<?= admin_url('admin.php?page='.$pluginPageUID.'&tab=create')?>" class="nav-tab">Create Filters</a>
    <a href="<?= admin_url('admin.php?page='.$pluginPageUID.'&tab=list')?>" class="nav-tab">List Filters</a>
  </h2>

  <div class="panel-body">
    <?php
    $activeTab = $_GET['tab'];

    if ( !isset($activeTab) )
        PriceFilterView::createFormFilter();
    
    if ($activeTab == 'create')
        PriceFilterView::createFormFilter();

    if ($activeTab == 'list')
       PriceFilterView::updateFilters();
    
    ?>
  </div>
<?php
}

require_once 'PriceFilter.php';
require_once 'PriceFilterView.php';


