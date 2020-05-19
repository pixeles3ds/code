<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Index extends CI_Controller {
	 
	function __construct()
	{
		parent::__construct();						
		$this->load->database();
		$this->load->library(array('ion_auth'));
		$this->load->helper(array('url'));
	}

	public function index()
	{				

		if($this->ion_auth->logged_in())
			redirect('home', 'refresh');
		else
			redirect('auth/login', 'refresh');
	}

}
