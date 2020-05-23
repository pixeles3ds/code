<?php
  $message = preg_replace("/\s+/", " ", $message );
?>

<?php
if($message){
  echo '<div class="errormsg">'.$message.'</div>';
}
?>

<?php echo form_open("usuarios/create_user");?>
	
	<div class="row">
		<div class="col-lg-0 col-md-3"></div>
		
		<div class="col-lg-6 col-md-6">
		
			<div class="panel animation-slide-top" data-plugin="appear" data-animate="slide-top">
				<div class="panel-heading">
				  <h3 class="panel-title"><i class="icon wb-user" aria-hidden="true"></i>Crear Usuario</h3>
				</div>
				<div class="panel-body container-fluid">
				  <form autocomplete="off">
					<div class="form-group form-material floating">
					  <input type="text" class="form-control empty" name="first_name">
					  <label class="floating-label">Nombre</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control empty" name="last_name">
					  <label class="floating-label">Apellido</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control empty" name="company">
					  <label class="floating-label">Compañia</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control empty" name="email">
					  <label class="floating-label">Email</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control empty" name="phone">
					  <label class="floating-label">Teléfono</label>
					</div>

					<div class="form-group form-material floating">
					  <input type="password" class="form-control empty" name="password">
					  <label class="floating-label">Password</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="password" class="form-control empty" name="password_confirm">
					  <label class="floating-label">Confirmar Password</label>
					</div>
					
					<p><br><button type="submit" class="btn btn-raised btn-primary btn-block">Guardar</button></p>
					
				  
				</div>
			</div>
			
			<div class="col-lg-0 col-md-3"></div>

		</div>
	</div>


</form>