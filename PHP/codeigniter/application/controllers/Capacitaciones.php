<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Capacitaciones extends CI_Controller {

	function __construct()
	{
		parent::__construct();				
		$this->load->database();
		$this->load->library(array('ion_auth'));
		$this->load->helper(array('url'));

		$this->load->model('capacitaciones_model');

	}
	 

	public function index(){	
		
		if(!$this->ion_auth->logged_in())
			redirect('auth/login', 'refresh');

		$id = user("id");
		$data = $this->capacitaciones_model->getCapacitaciones($id);

		$this->template->view('main','usuarios/capacitaciones', $data );
		
	}


	public function crear(){
	
		//$fecha = $this->input->post('fecha');
		$fecha = "02/02/1992";
		
		$data = array();
		$capacitacion = array();		

		//$capacitacion["nombre"] = $this->input->post('nombre');
		//$capacitacion["fecha"] = DateTime::createFromFormat('d/m/Y', $fecha)->format('Y-m-d');
		//$capacitacion["hora"] = $this->input->post('hora');
		
		$capacitacion["nombre"] = "asd";
		$capacitacion["fecha"] = DateTime::createFromFormat('d/m/Y', $fecha)->format('Y-m-d');
		$capacitacion["hora"] = "22:50";

		$data["capacitacion"] = $capacitacion;
		$data["cupos"] = "5";

		$this->capacitaciones_model->crear($data);
		
		redirect('./capacitaciones', 'refresh');

	}	


	public function inscribir($id){
		
		$this->capacitaciones_model->inscribir( $id , user("id") );

	}

	public function eliminarSub($id){
		
		$this->capacitaciones_model->eliminarSub( $id , user("id") );

	}	

	public function getCapacitaciones($id){
		
		printr($this->capacitaciones_model->getCapacitaciones($id));

	}

	public function test(){

		printr(user());	
		printr( user("id") );
		printr( user("rol") );
		printr( user("name") );
		printr( user("email") );
	}
	
}
