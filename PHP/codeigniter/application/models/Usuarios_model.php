<?php  defined('BASEPATH') OR exit('No direct script access allowed');

class Usuarios_model extends CI_Model{

	public function __construct()
	{
		parent::__construct();
		$this->load->database();
	}
	
	public function getUsers()
	{

		return $this->db->get('users')->result();

	}
}


?>