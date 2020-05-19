<?php  
	

	if ( ! function_exists('user'))
	{
	    function user( $data = null ){

			$ci = & get_instance();

	    	if($data == null){
				
				$user = array(
					'id' => $ci->session->all_userdata()["user_id"],
					'rol' => $ci->session->all_userdata()["rol"],
					'name' => $ci->session->all_userdata()["name"],
					'email' => $ci->session->all_userdata()["email"]
				);

			}else{
				$data == "id" ? $user = $ci->session->all_userdata()["user_id"] : "";
				$data == "rol" ? $user = $ci->session->all_userdata()["rol"] : "";
				$data == "name" ? $user = $ci->session->all_userdata()["name"] : "";
				$data == "email" ? $user = $ci->session->all_userdata()["email"] : "";
			}

			return $user;
	    }   
	}

	if ( ! function_exists('printr'))
	{
	    function printr($data)
	    {
	        echo "<pre>";
			print_r($data);
			echo "</pre>";		
	    }   
	}

	if ( ! function_exists('pr'))
	{
	    function pr($data)
	    {
	        echo "<pre>";
			print_r($data);
			echo "</pre>";		
	    }   
	}

	if ( ! function_exists('setUserData'))
	{
	    function setUserData(){

	    	$ci = & get_instance();
			
			$id = $ci->session->all_userdata()["user_id"];

 			$query = $ci->db->query("SELECT users.first_name, users.last_name, users_groups.group_id FROM users INNER JOIN users_groups ON users.id = users_groups.user_id WHERE users.id = $id ORDER BY users_groups.group_id ASC LIMIT 1")->row();
			
			$data = array(	    		
	    		'name' => $query->first_name." ".$query->last_name,
	    		'rol' => $query->group_id
	    	);	    
	        
			$ci->session->set_userdata($data);
			
	        
	    }   
	}




