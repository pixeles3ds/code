$(function() {

	var ladies = window.ladies_registration;
	
    setTimeout(function(){
		
		if( ladies ){
			
			$("input[name='field_2'][value='Female']").prop('checked', true);
			
			$("form.standard-form").append( '<input id="ladies_register" type="hidden" name="first_lady_register" value="1">' );
			
			$("#basic-details-section h2").html("Free Ladies SignUp");
			$("#basic-details-section h2").addClass("ladies-title");			
			
		}
			
   },10)


});