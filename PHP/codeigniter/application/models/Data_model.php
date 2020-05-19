<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Data_model extends CI_Model{
	
	public function getData()
	{
		return $this->db->get('ejemplo')->result();
	}
}


?>