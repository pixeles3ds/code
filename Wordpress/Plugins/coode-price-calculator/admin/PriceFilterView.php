<?php

class PriceFilterView{
    


    static function createFormFilter(){ 
        $args = array('status' => 'published');
        $products = wc_get_products($args);

        $products = PriceFilter::getAllProducts();
        $filters = PriceFilter::getFiltersLabel();
       // echo json_encode($products);
        /*
        $args = array(
            'post_type' => 'product',
            'posts_per_page' => -1,
        );

        $wp_query = new WP_Query($args);
        $products = $wp_query->posts;
        */
        ?>
        <div class="container-fluid" id="createFilterPanel">
           <div class="row">
               <div class="col-12">
                    <div class="progress" style="height: 2px; margin: 3px 0;">
                      <div class="progress-bar bg-info" role="progressbar" aria-valuenow="10" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>                  
               </div>
           </div>
           <form id="pcForm">
            <div class="row">
                    <div class="col-6">
                          <div class="form-group">
                            <label for="productSelect">Product to link</label>
                                <select class="form-control" id="productSelect" name="Product[id]">
                                  <option value="0" disabled selected>Select a product </option>
                                  <?php foreach($products as $product){ ?>
                                      <option value="<?php echo $product->get_id() ?>"><?php echo $product->get_name() ?></option>
                                  <?php }?>
                                </select>
                          </div>

                          <div class="form-group">
                            <label for="attributeSelect">Attribute to filter</label>
                            <select class="form-control" name="Product[attribute]" id="attributeSelect" disabled></select>
                          </div>

                          <div class="form-group">
                            <label for="valueSelect">Attribute's value to filter</label>
                            <select class="form-control" name="Product[attribute_value]" id="valueSelect" disabled></select>
                          </div>

                          <div class="form-group">
                            <label for="filterSelect">Filter to link to product</label>
                            <select class="form-control" name="Product[filter]" id="filterSelect">
                                <option>Select a filter </option>
                                <?php foreach($filters as $key => $filter){ ?>
                                    <option value="<?php echo $key ?>"><?php echo $filter?></option>
                                <?php } ?>
                            </select>
                          </div>
                      
                     </div>
                     <div class="col-6" id="filterTable"></div>
                     <div class="col-12 text-center">
                         <div id="result" class="col-12 d-none">
                             <div class="alert" role="alert"></div>
                         </div>
                         <button type="submit" class="btn btn-dark">Create Filter</button>
                     </div>
            </div>
           </form>
        </div>
    <?php }
    
    static function semiPrettyArrayView($array){
        $str = '';
        foreach($array as $k => $e){
            $str .= ($k!='id') ? '['.$k.'='.$e.'] ' : '';
        }
        return $str;
    }
    
    
    static function updateFilters(){ 

    ?>
        <div class="container-fluid" id="updateFilterTabs">
            <div class="row">
                <div class="col-12">
                    <div id="tableContainer">
                        <table class="table">
                          <thead class="thead-dark">
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">Product</th>
                                <th scope="col">Attribute</th>
                                <th scope="col">Attribute's Value</th>
                                <th scope="col">Filter</th>
                                <th scope="col">Filter's Values</th>
                                <th scope="col">Actions</th>
                            </tr>
                          </thead>
                          <tbody>
                           <?php 
                                $rows = Product::getAllExtended();
                                foreach($rows as $row) {
                                    $product = wc_get_product($row['product_id']);
                                    $labels = PriceFilter::getFiltersLabel();
                            ?>
                                <tr id="uid_<?php echo $row['id']?>">
                                  <th scope="row"><?php echo $row['id']?></th>
                                  <td><?php echo $product->get_name() ?></td>
                                  <td><?php echo $row['attribute']?></td>
                                  <td><?php echo $row['value']?></td>
                                  <td><?php echo $labels[strtolower($row['filter'])]?></td>
                                  <td><?php echo self::semiPrettyArrayView($row['filter_values']) ?></td>
                                  <td><button class="deleteFilter btn btn-dark" data-toggle="tooltip" data-placement="top" title="Delete" data-product="<?php echo $row['id'] ?>">x</button></td>
                                </tr>
                            <?php } ?>
                          </tbody>
                        </table>                         
                    </div>
                </div>
            </div>
        </div>
    <?php }
    
}
