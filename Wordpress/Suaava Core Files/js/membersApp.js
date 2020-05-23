
var level_current_suer = {
	"id": "",
	"name":"",
	"opc":""
}

var loading_DOM_obj = "" ;


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


function delete_user(id,name,obj){
	if( window.processing_action == 0){
		window.loading_DOM_obj = $(obj ).closest('li').find(".level");
		user_action( id, name, "delete", name );	
	}	
}

function role_user(id,name,opc,obj){
	if( window.processing_action == 0){
		window.loading_DOM_obj = $(obj ).closest('li').find(".level");
		user_action( id, name, "role", opc );	
	}	
}

function level_user(){

	if( window.processing_action == 0){

		var radio_option = $('input[name=level]:checked').val();
		var user_level = window.level_current_suer;

		if( user_level["opc"] != radio_option ){
			user_action( user_level["id"], user_level["name"], "level", radio_option );
		}

	}

}

function open_levels_dialog(id,name,opc,obj){

	if( window.processing_action == 0){

		window.loading_DOM_obj = obj;

		window.level_current_suer = {
			"id": id,
			"name":name,
			"opc":opc
		}

		$("#levels_user_name_span").html(name); // change user name on dialog

		$("input[name='level']").parent().removeClass("bold_text"); // delete bold styling
		$("input[name='level']").next().html("");	// delete text current level for all options
		$("input[name='level'][value='"+opc+"']").parent().addClass("bold_text"); // add bold styling
		$("input[name='level'][value='"+opc+"']").next().html(" (Current Level)");	// add text current level for -selected option
		$("input[name='level'][value='"+opc+"']").prop('checked', true);	// select current level of user

		$( "#dialog-confirm" ).dialog( "open" ); // open dialog

	}

}


function before_user_action(){
	
	window.processing_action = 1;
	$('#members-dir-search').addClass('loading');

	$(loading_DOM_obj).find("span").html("");
	$(loading_DOM_obj).addClass("loading_action");

}

function after_user_action(){
	//Refresh list sending form
	$("#members_search_submit").trigger('click');

}

function user_action( id, name, type, info ){
    

    var call = new ajaxCall();    
    var method = "post";
    

    if( type == "delete"){

		if (confirm('Are you sure you want to delete ' + name + '?')) {
			if (confirm('Confirm Deletion?')) {

				before_user_action();

				var data = {
					"do_action" : 1,
					"id" : id,
					"type" : type,
					"data" : info,					
				}

			    var url = root_url+"members/";
			    call.send( true, data, url, method, function(response) {
			    	//response
			    	after_user_action();
			    	console.log("User deleted!");

			    });

			} 		    
		} 
   	
    }

   if( type == "role"){

		if (confirm('Are you sure you want to assign ' + info + ' role to ' + name + '?')) {
			if (confirm('Confirm Change?')) {

				before_user_action();

				var data = {
					"do_action" : 1,
					"id" : id,
					"type" : type,
					"data" : info,					
				}

			    var url = root_url+"members/";
			    call.send( true, data, url, method, function(response) {
			    	//response
			    	after_user_action();
			    	console.log("Role Updated!");

			    });

			} 		    
		} 
   	
    }

   if( type == "level"){

		if (confirm('Are you sure you want to change level for ' + name + '?')) {
			if (confirm('Confirm Change?')) {

				before_user_action();

				var data = {
					"do_action" : 1,
					"id" : id,
					"type" : type,
					"data" : info,					
				}

			    var url = root_url+"members/";
			    call.send( true, data, url, method, function(response) {
			    	//response
			    	after_user_action();
			    	console.log("Level Updated!");

			    });

			} 		    
		} 
   	
    }

    

}


function set_levels_dialog(){

	$( "#dialog-confirm" ).dialog({
		autoOpen: false,
		resizable: false,
		height: "auto",
		width: 400,
		modal: true,
		buttons: {
			"Confirm": function() {
				$( this ).dialog( "close" );
				setTimeout(function(){
					level_user();
				},50);
			},"Cancel": function() {
				$( this ).dialog( "close" );
			}
		}
	});
}



// Create a chagedClass LISTENER
// Create a closure
(function(){

	var originalAddClassMethod = jQuery.fn.addClass;
	var originalRemoveClassMethod = jQuery.fn.removeClass;

	jQuery.fn.addClass = function(){
		// Execute the original method.
		var result = originalAddClassMethod.apply( this, arguments );

		// trigger a custom event
		jQuery(this).trigger('cssClassAdded');

		// return the original result
		return result;
	}
	jQuery.fn.removeClass = function(){ 
		// Execute the original method.
		var result = originalRemoveClassMethod.apply( this, arguments );

		// trigger a custom event
		jQuery(this).trigger('cssClassRemoved');

		// return the original result
		return result;
	}

})();

$(function(){
	
	// Icon loader listener
	$('#members-all').bind('cssClassAdded', function(){  $('#members-dir-search').addClass('loading'); });
	$('#members-all').bind('cssClassRemoved', function(){  $('#members-dir-search').removeClass('loading'); });

	// add icon loader
	$('#search-members-form').append('<span id=\'loader_ajax_members\'></span>');

	// Add item to select filter
	$('#members-order-by').append( new Option('Premium', 'premium') );
	$('#members-order-by').append( new Option('Inactive', 'inactive') );
	$('#members-order-by').append( new Option('Free Users', 'free') );
	$('#members-order-by').append( new Option('No Plan', 'noplan') );
	$('#members-order-by').append( new Option('Administrator', 'admin') );


	set_levels_dialog();


});