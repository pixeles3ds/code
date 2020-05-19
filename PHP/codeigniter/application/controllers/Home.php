<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Home extends CI_Controller {

	function __construct()
	{
		parent::__construct();				
		$this->load->database();
		$this->load->library(array('ion_auth'));
		$this->load->helper(array('url'));

		$this->load->model('usuarios_model');

	}
	 

	public function index(){		

		if(!$this->ion_auth->logged_in()){
			redirect('auth/login', 'refresh');
		}else{
			$this->template->view('main','prueba/index' );			
		}
		

	}
	
}
