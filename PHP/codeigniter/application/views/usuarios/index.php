
<style>
	.firstBtn{
		margin-right:10px;
	}
	.editUser{
		color:#4B6764;
	}
</style>

<div class="row">
<div class="col-xlg-0 col-md-2"></div>
<div class="col-xlg-4 col-md-8">
          <!-- Example Panel With All -->
          <div class="panel panel-bordered animation-slide-top" data-plugin="appear" data-animate="slide-top">
            <div class="panel-heading">
			
              <h3 class="panel-title">
			  <i class="icon wb-user" aria-hidden="true"></i>
			  Crear Usuarios
			  </h3>
            </div>
			<table class="table table-hover">
              <thead>
                <tr>                 
                  <th>Nombre</th>
                  <th>Apellido</th>
				  <th>Email</th>
				  <th>Rol</th>
				  <th>Acción</th>
                </tr>
              </thead>
              <tbody>
				<?php foreach ($users as $user):?>
                <tr>
                  <td><?php echo htmlspecialchars($user->first_name,ENT_QUOTES,'UTF-8');?></td>
                  <td><?php echo htmlspecialchars($user->last_name,ENT_QUOTES,'UTF-8');?></td>
                  <td><?php echo htmlspecialchars($user->email,ENT_QUOTES,'UTF-8');?></td>
				  <td>
					<?php foreach ($user->groups as $group):?>
						<?php  if($group->id == 1) echo "Admin"; ?>
					<?php endforeach?>
				  </td>
                  <td>					
					<a href="<?php echo site_url('usuarios/edit_user')."/".$user->id;?>" class="editUser firstBtn" title="Editar"><i class="icon wb-edit" aria-hidden="true"></i></a>
					<a href="<?php echo site_url('usuarios/delete_user')."/".$user->id;?>" class="editUser" title="Eliminar"><i class="icon wb-close" aria-hidden="true"></i></a>
				  </td>
                </tr>
				<?php endforeach;?>
              </tbody>
            </table>
            <div class="panel-footer"><?php echo anchor('usuarios/create_user', "<strong>+ Nuevo Usuario</strong>")?></div>
          </div>
          <!-- End Example Panel With All -->
        </div>
		
<div class="col-xlg-0 col-md-2"></div>
		
</div>		



<p></p>