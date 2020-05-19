<?php  defined('BASEPATH') OR exit('No direct script access allowed');

class Capacitaciones_model extends CI_Model{

	public function __construct()
	{
		parent::__construct();
		$this->load->database();
	}
	
	public function crear($data){

		// Insertamos en tabla capacitacion
		$this->db->insert('capacitaciones', $data["capacitacion"]);
		$id = $this->db->insert_id();

		

		$data_cupos= array(
			'capacitacion_id' => $id,
			'cupos' => $data["cupos"]
		);

		// Insertamos los cupos de la capacitacion
		$this->db->insert('capacitaciones_stock', $data_cupos );

	}


	public function getCapacitaciones($id){

		$sql = "

			SELECT c.*, cs.cupos, cu.id AS idUserCap
			FROM capacitaciones c
			LEFT JOIN capacitaciones_usuarios cu ON (c.id = cu.capacitacion_id AND cu.usuario_id = $id)
			LEFT JOIN capacitaciones_stock cs ON c.id = cs.capacitacion_id 

		";

		return $this->db->query($sql)->result();

	}

	public function inscribir($id, $user){

		//valor actual cupos
		$cupo = $this->db->query( " SELECT cupos FROM capacitaciones_stock WHERE capacitacion_id = $id ")->row()->cupos;
		$cupo = $cupo - 1;


		// cambiamos el cupo
		$stock = array(
			'cupos' => $cupo
		);

		$this->db->where('capacitacion_id', $id);
		$this->db->update('capacitaciones_stock', $stock); 


		// añadimos la supscripcion
		$data = array(
			'capacitacion_id' => $id,
			'usuario_id' => $user
		);

		// Insertamos los cupos de la capacitacion
		$this->db->insert('capacitaciones_usuarios', $data );

	}

	public function eliminarSub($id, $user){

		//valor actual cupos
		$cupo = $this->db->query( " SELECT cupos FROM capacitaciones_stock WHERE capacitacion_id = $id ")->row()->cupos;
		$cupo = $cupo + 1;


		// cambiamos el cupo
		$stock = array(
			'cupos' => $cupo
		);

		$this->db->where('capacitacion_id', $id);
		$this->db->update('capacitaciones_stock', $stock); 


		// añadimos la supscripcion
		$data = array(
			'capacitacion_id' => $id,
			'usuario_id' => $user
		);

		$this->db->where(" capacitacion_id = $id AND usuario_id = $user ");
		$this->db->delete('capacitaciones_usuarios'); 

	}			


}


?>