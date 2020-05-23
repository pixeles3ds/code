<?php  defined('BASEPATH') OR exit('No direct script access allowed');

class Capacitaciones_model extends CI_Model{

	public function __construct()
	{
		parent::__construct();
		$this->load->database();
	}
	
	public function crear( $data ){

		// Insertamos en tabla capacitacion
		$this->db->insert('capacitaciones', $data );
		$id = $this->db->insert_id();	

	}


	public function getCapacitaciones($id){

		$sql = "

			SELECT 
				c.id as id,
				c.nombre as nombre,
				c.fecha as fecha,
				c.hora as hora,
				#c.cupos as total_cupos,
				IF( cu_count.total IS NULL, c.cupos, c.cupos - cu_count.total ) as cupos,
				IF( cu.id IS NULL,0,1) AS activo
			FROM capacitaciones  c
			LEFT JOIN capacitaciones_usuarios cu ON ( c.id = cu.capacitacion_id AND cu.usuario_id = $id )
			LEFT JOIN (
				SELECT
				DISTINCT(capacitacion_id) as id,
				COUNT(capacitacion_id ) as total
				FROM capacitaciones_usuarios
				GROUP BY capacitacion_id
			) cu_count ON c.id = cu_count.id 

		";

		return $this->db->query($sql)->result();

	}

	public function inscribir($id, $user){

		//---------------------------------------------------------
		// Obtener valor actual del stock de cupos_activos y sumamos 1
		//---------------------------------------------------------
		$cupo = $this->db->query( " SELECT cupos_activos FROM capacitaciones WHERE id = $id ")->row()->cupos_activos;
		$cupo = $cupo + 1;


		//---------------------------------------------------------
		// Actualizamos el stock de capacitaciones->cupos_activos
		//---------------------------------------------------------
		$stock = array(
			'cupos_activos' => $cupo
		);

		$this->db->where('id', $id);
		$this->db->update('capacitaciones', $stock); 

		//---------------------------------------------------------
		// Agregamos la supscripcion en (capacitaciones_usuarios)
		//---------------------------------------------------------
		$data = array(
			'capacitacion_id' => $id,
			'usuario_id' => $user
		);
		$this->db->insert('capacitaciones_usuarios', $data );

	}

	public function eliminarSub($id, $user){

		//---------------------------------------------------------
		// Obtener valor actual del stock de cupos_activos y restamos 1
		//---------------------------------------------------------
		$cupo = $this->db->query( " SELECT cupos_activos FROM capacitaciones WHERE id = $id ")->row()->cupos_activos;
		$cupo = $cupo - 1;


		//---------------------------------------------------------
		// Actualizamos el stock de capacitaciones->cupos_activos
		//---------------------------------------------------------
		$stock = array(
			'cupos_activos' => $cupo
		);

		$this->db->where('id', $id);
		$this->db->update('capacitaciones', $stock); 


		//---------------------------------------------------------
		// Eliminamos la supscripcion en (capacitaciones_usuarios)
		//---------------------------------------------------------
		$data = array(
			'capacitacion_id' => $id,
			'usuario_id' => $user
		);

		$this->db->where(" capacitacion_id = $id AND usuario_id = $user ");
		$this->db->delete('capacitaciones_usuarios'); 

	}			


}


?>