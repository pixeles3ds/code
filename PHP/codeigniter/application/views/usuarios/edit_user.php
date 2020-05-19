<?php echo form_open(uri_string());?>
	
	<div class="row">
		<div class="col-lg-0 col-md-3"></div>
		
		<div class="col-lg-6 col-md-6">
		
			<div class="panel animation-slide-top" data-plugin="appear" data-animate="slide-top">
				<div class="panel-heading">
				  <h3 class="panel-title"><i class="icon wb-user" aria-hidden="true"></i>Editar Usuario</h3>
				</div>
				<div class="panel-body container-fluid">
				  <form autocomplete="off">
					<div class="form-group form-material floating">
					  <input type="text" class="form-control <?php if( $first_name["value"] == "") echo 'empty'; ?>" name="first_name" value="<?php echo $first_name["value"]; ?>" >
					  <label class="floating-label">Nombre</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control <?php if( $last_name["value"] == "") echo 'empty'; ?>" name="last_name" value="<?php echo $last_name["value"]; ?>" >
					  <label class="floating-label">Apellido</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control <?php if( $company["value"] == "") echo 'empty'; ?>" name="company" value="<?php echo $company["value"]; ?>" >
					  <label class="floating-label">Compañia</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="text" class="form-control <?php if( $phone["value"] == "") echo 'empty'; ?>" name="phone" value="<?php echo $phone["value"]; ?>" >
					  <label class="floating-label">Teléfono</label>
					</div>

					<div class="form-group form-material floating">
					  <input type="password" class="form-control empty" name="password" >
					  <label class="floating-label">Password</label>
					</div>
					<div class="form-group form-material floating">
					  <input type="password" class="form-control empty" name="password_confirm" >
					  <label class="floating-label">Confirmar Password</label>
					</div>

					<div style="margin:30px 20px 20px 20px">

					  <?php if ($this->ion_auth->is_admin()): ?>

						  <h3><?php echo "Roles" ?></h3>
						  <?php foreach ($groups as $group):?>
							  <label class="checkbox">
							  <?php
								  $gID=$group['id'];
								  $checked = null;
								  $item = null;
								  foreach($currentGroups as $grp) {
									  if ($gID == $grp->id) {
										  $checked= ' checked="checked"';
									  break;
									  }
								  }
							  ?>
							  <input type="checkbox" name="groups[]" value="<?php echo $group['id'];?>"<?php echo $checked;?>>
							  <?php 
								if($group['name']=="admin") echo "Administrador";
								if($group['name']=="members") echo "Usuario";
							  ?>
							  </label>
						  <?php endforeach?>

					  <?php endif ?>

					  <?php echo form_hidden('id', $user->id);?>
					  <?php echo form_hidden($csrf); ?>

					</div>
					
					<p><br><button type="submit" class="btn btn-raised btn-primary btn-block">Guardar</button></p>
					
				  
				</div>
			</div>
			
			<div class="col-lg-0 col-md-3"></div>

		</div>
	</div>


</form>
		



