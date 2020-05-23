
function ajaxCall() {
    this.send = function(sync, data, url, method, success, type) {
      type = type||'json';
      var successRes = function(data) {
          success(data);
      };

      var errorRes = function(e) {
          console.log(e);
          alert("Error found \nError Code: "+e.status+" \nError Message: "+e.statusText);
      };
      $.ajax({
        url: url,
        type: method,
        async : sync,
        data: data,
        success: successRes,
        error: errorRes,
        dataType: type,
        timeout: 60000
    });

  }

}

function locationInfo() {
    var rootUrl = root_url+"locations/";
    var call = new ajaxCall();
    
    this.set_data_dropdowns = function() {
        
        $.each( json_countries['result'], function(key, val) {
            var option = $('<option />');
            option.attr('value', key).text(val);
            $('.countries').append(option);
        });
        $(".countries").prop("disabled",false);
        
        $.each( json_states['result'], function(key, val) {
            var option = $('<option />');
            option.attr('value', key).text(val);
            $('.states').append(option);
        });
        $(".states").prop("disabled",false);

        $.each( json_cities['result'], function(key, val) {
            var option = $('<option />');
            option.attr('value', key).text(val);
            $('.cities').append(option);
        });
        $(".cities").prop("disabled",false);

        // Set Country
        $(".countries").val( json_location.country );
        $(".field_country .buddyboss-select-inner span").html( $(".countries option:selected").html() );
        $(".field_country input:first").val( $(".countries option:selected").html() );

        // Set State
        $(".states").val( json_location.state );
        $(".field_state .buddyboss-select-inner span").html( $(".states option:selected").html() );
        $(".field_state input:first").val( $(".states option:selected").html() );

        // Set Country
        $(".cities").val( json_location.city );
        $(".field_city .buddyboss-select-inner span").html( $(".cities option:selected").html() );
        $(".field_city input:first").val( $(".cities option:selected").html() );


    };

    this.getCities = function(id) {
        $(".cities option:gt(0)").remove();
        var url = rootUrl+'?type=getCities&stateId=' + id;
        var method = "post";
        var data = {};
        $('.cities').find("option:eq(0)").html("Please wait..");
        $(".field_city .buddyboss-select-inner span").html( "Please wait.." );
        $(".field_city").addClass("select_disabled");

        call.send(true,data, url, method, function(data) {
            $('.cities').find("option:eq(0)").html("Select City");
            $(".field_city .buddyboss-select-inner span").html( "Select City" );
            $(".field_city").removeClass("select_disabled");

            if(data.tp == 1){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                    option.attr('value', key).text(val);
                    $('.cities').append(option);
                });
                $(".cities").prop("disabled",false);
            }
            else{
               alert(data.msg);
           }
       });
    };

    this.getStates = function(id) {
        $(".states option:gt(0)").remove(); 
        $(".cities option:gt(0)").remove(); 
        var url = rootUrl+'?type=getStates&countryId=' + id;
        var method = "post";
        var data = {};
        $('.states').find("option:eq(0)").html("Please wait..");
        $(".field_state .buddyboss-select-inner span").html( "Please wait.." );
        $(".field_state").addClass("select_disabled");

        call.send(true,data, url, method, function(data) {
            $('.states').find("option:eq(0)").html("Select State");
            $(".field_state .buddyboss-select-inner span").html( "Select State" );
            $(".field_state").removeClass("select_disabled");

            if(data.tp == 1){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                    option.attr('value', key).text(val);
                    $('.states').append(option);
                });
                $(".states").prop("disabled",false);
            }
            else{
                alert(data.msg);
            }
        }); 
    };

    this.getCountries = function() {
        var url = rootUrl+'?type=getCountries';
        var method = "post";
        var data = {};
        $('.countries').find("option:eq(0)").html("Please wait..");
        $(".field_country .buddyboss-select-inner span").html( "Please wait.." );
        $(".field_country").addClass("select_disabled");

        call.send(true,data, url, method, function(data) {
            $('.countries').find("option:eq(0)").html("Select Country");
            $(".field_country .buddyboss-select-inner span").html( "Select Country" );
            $(".field_country").removeClass("select_disabled");
            
            if(data.tp == 1){
                $.each(data['result'], function(key, val) {
                    var option = $('<option />');
                    option.attr('value', key).text(val);
                    $('.countries').append(option);
                });
                $(".countries").prop("disabled",false);
            }
            else{
                alert(data.msg);
            }
        }); 
    };

    /*
    this.saveLocation = function( json_data ) {
        var url = rootUrl+'?type=save';
        var method = "post";
        var data = json_data;

        call.send(false,data, url, method, function(data) {

        }); 
    };
    */

}

$(function() {


    setTimeout(function(){

        $(".field_country, .field_city, .field_state").addClass('location_field');

        $(".field_country input:first").after( '<div class="buddyboss-select"><div class="buddyboss-select-inner"><span style="">----</span><select id="select_country" class="form-control countries location_select" name="select_country" aria-labelledby="select_country" aria-describedby="select_country"><option value="">----</option></select></div></div>' );
        $(".field_state input:first").after( '<div class="buddyboss-select"><div class="buddyboss-select-inner"><span style="">----</span><select id="select_state" class="form-control states location_select" name="select_state" aria-labelledby="select_state" aria-describedby="select_state"><option value="">----</option></select></div></div>' );
        $(".field_city input:first").after( '<div class="buddyboss-select"><div class="buddyboss-select-inner"><span style="">----</span><select id="select_city"  class="form-control cities location_select"  name="select_city" aria-labelledby="select_city" aria-describedby="select_city"><option value="">----</option></select></div></div>' );
        $("form.standard-form").append( '<input id="input_location" type="hidden" name="location" value="">' );

        var loc = new locationInfo();
        if( json_location_saved ){
            loc.set_data_dropdowns(); 
        }else{
            loc.getCountries(); 
        }
       


        $(".countries").on("change", function(ev) { 


            var countryId = $(this).val();
            if(countryId != ''){
                loc.getStates(countryId);
            }else{
                $(".states option:gt(0)").remove();
            }

            $(".field_country .buddyboss-select-inner span").html( $(".countries option:selected").html() );
            if( $(".countries option:selected").val() == "" ) $(".field_country input:first").val( "" );
            else $(".field_country input:first").val( $(".countries option:selected").html() );

            //$(".field_state .buddyboss-select-inner span").html( "----" );
            $(".field_state input:first").val( "" );
            $(".field_city .buddyboss-select-inner span").html( "----" );
            $(".field_city input:first").val( "" );

            $(".field_location-postal-code input:first").val( " " );
            GMW_XF.clear_fields();
            


        });

       $(".states").on("change", function(ev) {


             var stateId = $(this).val();
             if(stateId != ''){
                 loc.getCities(stateId);
             }else{
                $(".cities option:gt(0)").remove();
            }

            $(".field_state .buddyboss-select-inner span").html( $(".states option:selected").html() );			
            if( $(".states option:selected").val() == "" ) $(".field_state input:first").val( "" );
            else $(".field_state input:first").val( $(".states option:selected").html() );


           // $(".field_city .buddyboss-select-inner span").html( "----" );
            $(".field_city input:first").val( "" );

            $(".field_location-postal-code input:first").val( " " );
            GMW_XF.clear_fields();

        });

        $(".cities").on("change", function(ev) {

            $(".field_city .buddyboss-select-inner span").html( $(".cities option:selected").html() );
            $(".field_city input:first").val( $(".cities option:selected").html() );

            $(".field_location-postal-code input:first").val( " " );
            GMW_XF.clear_fields();            

        });

   },10)





});


function location_collect_and_save(){

    var response = {"data":""};

    // if all field has an option selected
    if( $(".countries option:selected").val() != "" && $(".states option:selected").val() != "" && $(".cities option:selected").val() != ""  ){
        var json_obj = {"country": parseInt($(".countries option:selected").val()), "state": parseInt($(".states option:selected").val()), "city": parseInt($(".cities option:selected").val()) };
        response["data"] = json_obj;
    }else{
        response["data"] = "";
        $(".field_city input:first").val( "" );
        $(".field_state input:first").val( "" );
        $(".field_country input:first").val( "" );
    }

    //Hidden input with a json collected
    $("#input_location").val( JSON.stringify( json_obj ) );

    //var loc = new locationInfo();
    //loc.saveLocation( response );
    
}

$( "#profile-edit-form" ).submit(function( event ) {  
    //console.log("aaa");
    location_collect_and_save();
    //event.preventDefault();
});
$( "#signup_form" ).submit(function( event ) {      
    location_collect_and_save();
    //event.preventDefault();
});

