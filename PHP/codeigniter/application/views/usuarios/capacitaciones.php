<?php $rol=user( "rol"); ?>
<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/asspinner/asSpinner.min09a2.css?v2.1.0">
<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/clockpicker/clockpicker.min09a2.css?v2.1.0">
<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/jt-timepicker/jquery-timepicker.min09a2.css?v2.1.0">

<style>
	.fecha {
		font-size: 12px;
		margin-left: 5px;
	}
	.logo {
		font-size: 30px;
		margin-left: 30px;
		margin-top: 5px;
	}
	.media-right {
		padding: 0px !important;
	}
	.media-right .btn {
		margin: 10px 20px 0px 0px;
	}
	.media-heading {
		font-size: 16px;
		color: #0D6F65;
	}
	.icon {
		color: #76838f;
	}
	.media {
		margin: 0px;
		padding-top: 10px;
	}
	.media:hover {
		background-color: rgba(237, 244, 247, 0.7);
	}
	.btn-success {
		background-color: #48BBB0 !important;
		color: #fff !important;
		border-style: none !important;
	}
	hr {
		margin: 5px 0px;
	}
	.profile-job {
		font-size: 16px;
		/*margin-left: 20px;*/
		
		margin-top: 10px;
		text-align: center;
		margin-bottom: 0px;
	}
	.example {
		margin-top: 0px;
	}
	.datepicker-inline {
		margin: 0px auto;
		margin-top: 5px;
	}
	.bootstrap-touchspin-down,
	.bootstrap-touchspin-up {
		background-color: rgba(118, 131, 143, .1) !important;
		transition: background-color 1000;
	}
	.bootstrap-touchspin-down:hover,
	.bootstrap-touchspin-up:hover {
		background-color: rgba(118, 131, 143, .16) !important;
	}
	input {
		background-color: rgba(239, 243, 245, 0.7) !important
	}
	.form-control.focus,
	.form-control:focus {
		border-color: #B9D0E2;
	}
	.txtCupos {
		float: right;
		margin-right: 30px;
		font-size: 14px;
	}
	.datepicker table tr td.highlighted {
		background: #fff;
		border-radius: 0;
	}
	#msgError {
		text-align: center;
	}
	.panel-bordered>.panel-footer {
		border-top: none;
	}
	.media {
		border-bottom: 1px solid #e4eaec;
	}
	.oculto {
		visibility: hidden;
	}
</style>


<!-- MODAL -->
<div class="modal fade" id="examplePositionSidebar" aria-hidden="true" aria-labelledby="examplePositionSidebar" role="dialog" tabindex="-1" style="display: none;">
	<div class="modal-dialog modal-sidebar modal-sm">
		<div class="modal-content">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal" aria-label="Close">
					<span aria-hidden="true">×</span>
				</button>
				<h4 class="modal-title"><i class="site-menu-icon wb-warning" aria-hidden="true" style="color:#B12C24"></i> ¡Error!</h4>
			</div>
			<div class="modal-body">
				<p id="msgError"></p>
			</div>
			<div class="modal-footer">
				<button type="button" class="btn btn-primary btn-block" data-dismiss="modal">Aceptar</button>
			</div>
		</div>
	</div>
</div>
<!-- MODAL -->


<div class="row">

	<?php if($rol==1){ ?>
	<div class="col-xlg-4 col-md-4">

		<div class="widget widget-shadow text-center">

			<form id="crearCapacitacion" action="<?php echo site_url(); ?>capacitaciones/crear" method="post" accept-charset="utf-8">

				<div class="widget-header">
					<div class="widget-header-content" style="padding-top: 10px; ">

						<h4 class="profile-user" style="text-align: center">Crear Capacitación</h4>
						<hr>

						<div class="example">
							<div class="input-group bootstrap-touchspin" style="padding:0px 20px; margin-top: 10px; width: 100%">
								<input id="inputNombre" name="nombre" type="text" class="form-control" id="inputPlaceholder" placeholder="Nombre">
							</div>
						</div>
						<hr>

						<p class="profile-job">Cupos</p>
						<div class="example">

							<div class="input-group bootstrap-touchspin" style="padding:0px 20px; margin-top: 10px;">
								<input id="inputCupos" type="text" class="form-control" name="cupos" data-plugin="TouchSpin" data-min="-1000000000" data-max="1000000000" data-stepinterval="50" data-maxboostedstep="10000000" value="10" style="display: block;">
							</div>
						</div>
						<hr>

						<p class="profile-job">Hora</p>
						<div class="example">
							<div class="input-group" style="padding:0px 20px; margin-top: 10px; ">
								<span class="input-group-addon"><span class="wb-time"></span></span>
								<input type="text" id="inputTime" name="hora" value="" class="timepicker form-control" data-plugin="clockpicker" data-donetext="Hecho" data-autoclose="false" data-twelvehour="true" data-fromnow="now">
							</div>
						</div>
						<hr>

						<p class="profile-job">Fecha</p>
						<div class="example" style="">

							<div id="inlineDatepicker"></div>
							<input type="hidden" id="inputDate" name="fecha" />

						</div>
						<hr>

						<button id="btnGuardar" type="button" class="btn btn-primary padding-horizontal-50" style="margin:8px 0px 12px 0px">Crear</button>


					</div>
				</div>

			</form>

		</div>
	</div>
	<?php }else{ ?>
	<div class="col-xlg-4 col-md-2"></div>
	<?php } ?>


	<div class="col-xlg-4 col-md-8">
		<!-- Example Panel With All -->
		<div class="panel panel-bordered animation-slide-top" data-plugin="appear" data-animate="slide-top">
			<div class="panel-heading">

				<h2 class="panel-title">			  
			  Capacitaciones
			  </h2>
			</div>


			<?php foreach($data as $val){ ?>


			<div class="media">
				<div class="media-left">
					<i class="icon icon-color wb-book logo" aria-hidden="true"></i>
				</div>
				<div class="media-body">
					<h4 class="media-heading">
                  <?php echo $val->nombre; ?>                  
                </h4>
					<p>
						<i class="icon icon-color wb-time" aria-hidden="true"></i>
						<span class="fecha">
	                  <?php 
	                  	$fecha = DateTime::createFromFormat('Y-m-d', $val->fecha )->format('d/m/Y');
						echo $fecha." ".$val->hora;
	                  ?>
                  </span>
						<span class="txtCupos"><strong>
					<?php

				 	if ( $val->idUserCap == "" ){

						if( $val->cupos == 1){
				 			echo $val->cupos." Cupo";
				 		}else{
							echo $val->cupos." Cupos ";
				 		}

				 	}else{

				 		if( $rol == 1){

							if( $val->cupos == 1){
					 			echo $val->cupos." Cupo";
					 		}else{
								echo $val->cupos." Cupos ";
					 		}

				 		}

				 	}
					 	

					?>
                  </strong></span>


					</p>
				</div>
				<div class="media-right">

					<?php if ( $val->idUserCap == "" ){ if( $val->cupos == 0){ echo '
					<button type="button" class="btn btn-primary oculto">Inscribir</button>'; }else{ echo '
					<button type="button" class="btn btn-primary" onclick="inscribir('.$val->id.')">Inscribir</button>'; } }else{ echo '
					<button type="button" class="btn btn-danger" onclick="baja('.$val->id.')">Eliminar</button>'; } ?>

				</div>
			</div>

			<?php } ?>


			<div class="panel-footer"></div>
		</div>
		<!-- End Example Panel With All -->
	</div>

	<?php if($rol==1){ }else{ ?>
	<div class="col-xlg-4 col-md-2"></div>
	<?php } ?>

</div>



<p></p>

<script>
	function getHora() {

		var currentTime = new Date()
		var hours = currentTime.getHours()
		var minutes = currentTime.getMinutes()

		if (minutes < 10)
			minutes = "0" + minutes;

		var suffix = "AM";
		if (hours >= 12) {
			suffix = "PM";
			hours = hours - 12;
		}
		if (hours == 0) {
			hours = 12;
		}
		var current_time = hours + ":" + minutes + " " + suffix;
		return current_time;
	}



	function hoy() {

		var today = new Date();
		var dd = today.getDate();
		var mm = today.getMonth() + 1;
		var yyyy = today.getFullYear();

		if (dd < 10) {
			dd = '0' + dd
		}
		if (mm < 10) {
			mm = '0' + mm
		}

		return dd + '/' + mm + '/' + yyyy;
	}



	function setInputDate(fecha) {
		$("#inputDate").val(fecha);
	}




	//-----------------------------------------------------------------------------

	function guardar() {

		var nombre = $("#inputNombre").val();
		var cupos = $("#inputCupos").val();
		var hora = $("#inputTime").val();
		var fecha = $("#inputDate").val();


		if (hora != "") {

			var array = hora.split(" ");
			var franja = array[1];
			var hora = parseInt(array[0].split(":")[0]);
			var minuto = parseInt(array[0].split(":")[1]);


			var errorHora = function() {
				$('#msgError').html("Seleccione un horario entre las <br> 10:00 AM y 10:00 PM");
				$('#examplePositionSidebar').modal('toggle');
			}

			if (franja == "AM" && hora < 10 || franja == "PM" && hora >= 10) {

				if (franja == "AM") {
					errorHora();
					return false;
				}
				if (franja == "PM" && hora > 10) {
					errorHora();
					return false;
				}
				if (franja == "PM" && hora == 10 && minuto > 0) {
					errorHora();
					return false;
				}

			}

		}


		if (fecha == "") $('#msgError').html("Seleccione una fecha");
		if (hora == "") $('#msgError').html("Seleccione una hora");
		if (cupos == "") $('#msgError').html("Seleccione la cantidad de cupos");
		if (nombre == "") $('#msgError').html("Digite el nombre de la capacitación");

		if (nombre == "" || cupos == "" || hora == "" || fecha == "") {
			$('#examplePositionSidebar').modal('toggle');
			return false;
		}

		$('#crearCapacitacion').submit();


	}

	//----------------------------------------------------------------------------------------

	$("#btnGuardar").click(guardar);

	//-----------------------------------------------------------------------------------------

	//-----------------------------------------------------------------------------------------
	//			AJAX
	//-----------------------------------------------------------------------------------------

	function inscribir(id) {

		$.ajax({
			type: "POST",
			async: false,
			url: "<?php echo site_url(); ?>capacitaciones/inscribir/" + id,
			cache: false,
			dataType: 'text',
			success: function(response) {
				location.reload(true)
			},
			error: function(xhr, textStatus, errorThrown) {
				alert(textStatus + " : " + errorThrown);
			}
		});

	}

	function baja(id) {

		$.ajax({
			type: "POST",
			async: false,
			url: "<?php echo site_url(); ?>capacitaciones/eliminarSub/" + id,
			cache: false,
			dataType: 'text',
			success: function(response) {
				location.reload(true)
			},
			error: function(xhr, textStatus, errorThrown) {
				alert(textStatus + " : " + errorThrown);
			}
		});

	}

	//-----------------------------------------------------------------------------------------


	$(document).ready(function($) {

		Site.run();

		$("#inputTime").val(getHora());


		$.fn.datepicker.dates['en'] = {
			days: ["Domingo", "Lúnes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
			daysShort: ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"],
			daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sa"],
			months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
			monthsShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
			today: "Hoy",
			clear: "Borrar",
			format: "mm/dd/yyyy",
			titleFormat: "MM yyyy",
			/* Leverages same syntax as 'format' */
			weekStart: 1
		};


		$date = $("#inlineDatepicker").datepicker({
			todayHighlight: true,
			daysOfWeekDisabled: "0,6",
			daysOfWeekHighlighted: "1,2,3,4,5"
		}).on('changeDate', function(e) {
			setInputDate(e.format('dd/mm/yyyy'));
		})




		var d = new Date();
		if (d.getDay() == 1 || d.getDay() == 2 || d.getDay() == 3 || d.getDay() == 4 || d.getDay() == 5) {
			$date.datepicker("setDate", "0");
			setInputDate(hoy())
		}




		$(".datepicker").addClass('well');
		$("#inlineDatepicker").on("changeDate", function(event) {
			//   $("#inputHiddenInline").val($("#inlineDatepicker").datepicker("getFormattedDate"))
		})
	})
</script>