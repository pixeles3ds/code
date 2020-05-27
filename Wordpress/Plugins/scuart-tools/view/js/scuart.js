
(function($){
    
    let optionsHtml = function(elements, label){
        let html = '<option value="0" selected disabled>Seleccione un ' +label+ '</option>';
        for(let t=0; t<elements.length; t++){
            let element = elements[t];
            html += '<option value="'+element+'">'+element+'</option>'
        }

        return html;
    }
    
    let filterTable = function(props){
        let table = '<table class="table">';
        table += '<thead class="thead-dark"><tr>';
        table += '<th scope="col">Value</th>';
        table += '<th scope="col">Multiplier</th>';
        table += '</tr></thead>';
        
        table += '<tbody>';
        for(let key in props){
            table += '<tr>';
            table += '<th scope="row">'+props[key]+'</th>';
            table += '<td><input type="text" name="Filter[' +key+ ']" value="0"></td>';
            table += '</tr>';
        }
        table += '</tbody>';
        table += '</table>';
        return table;
    }
    
    
    let updateBar = function(value){
        $('.progress-bar').attr('aria-valuenow', value);
        $('.progress-bar').css('width', value+'%');
    }
    
    let showResultMessage = function(data){
        
        $('#result').removeClass('d-none');
        $('#result').find('.alert').html(data['msg']);
        $('#result').find('.alert').addClass('alert-'+data['status']);
        
        setTimeout(function(){
           $('#result').addClass('d-none');
           $('#result').find('.alert').empty(); 
           $('#result').find('.alert').removeClass('alert-'+data['status']);
        }, 2000);        
    }
    
    let root = '#createFilterPanel';
    
    $('#pcForm').trigger('reset');
    
    $(root).on('change', '#productSelect', function(){
        updateBar(0);
        let valueSelected = this.value;    
        
        
        let data = {
            action: 'cp_load_product_attributes',
            id: valueSelected,
        };
        $('#attributeSelect').empty();
        $('#attributeSelect').prop('disabled', true);
        $.post(ajaxurl, data, function(data){
            data = JSON.parse(data);
            options = optionsHtml(data, 'atributo');
            
            $('#attributeSelect').html(options);
            $('#attributeSelect').prop('disabled', false);
            updateBar(100);
           
        });
        
    });
    
    $(root).on('change', '#attributeSelect', function(){
        updateBar(0);
        let valueSelected = this.value;    
        
        let data = {
            action: 'cp_load_attribute_values',
            attribute: valueSelected,
            product: $('#productSelect')[0].value,
        };
        $('#valueSelect').empty();
        $('#valueSelect').prop('disabled', true);
        $.post(ajaxurl, data, function(data){
            data = JSON.parse(data);
            options = optionsHtml(data, 'valor');
            
            $('#valueSelect').html(options);
            $('#valueSelect').prop('disabled', false);
             updateBar(100);
        });       
    });
    
    $(root).on('change', '#filterSelect', function(){
        updateBar(0);
        let valueSelected = this.value;    
        
        let data = {
            action: 'cp_load_filter_table',
            filter: valueSelected,

        };
        $.post(ajaxurl, data, function(data){
            data = JSON.parse(data);
            
            updateBar(100);
            $('#filterTable').html(filterTable(data));
        });       
    });    
        
    $(root).on('submit', 'form', function(e){
        updateBar(0);

        e.preventDefault();
        e.stopPropagation();
        
        let data = {
            action: 'cp_process_new_filter',
            data: $(this).serialize(),
        }
        
        $.post(ajaxurl, data, function(data){
            updateBar(100);

            data = JSON.parse(data);
            
            showResultMessage(data);
            
            if (data['status'] == 'success'){
                console.log(data['status']);
                $('#filterTable').empty();
                $('#pcForm').trigger('reset');
            }
            
        });
    })
    
    
    root = '#updateFilterTabs';

    $(root).on('click', '.deleteFilter', function(){
        let result = confirm('You are about to destroy a filter!! This action can not be undone.\n Do you want to continue?')
        if (result){
            
            let data = {
                action: 'cp_delete_filter',
                product: $(this).data('product'),
            }
            
            $.post(ajaxurl, data, function(data){
                data = JSON.parse(data);
                
                if ( data['status'] == 'success' ){
                    $('#uid_'+data['product']).css('border', '3px solid red');
                    setTimeout(function(){
                        $('#uid_'+data['product']).remove();
                    }, 1000);
                } else{
                    alert(data['msg']);
                }
            });
        }
    })
})(jQuery)