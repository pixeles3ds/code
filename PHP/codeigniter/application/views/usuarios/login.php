<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="<?php echo base_url().'assets';?>/css/style.css" media="screen" type="text/css" />
    </head>
    <body>    
        <div class="container">
      <div id="texto">Iniciar Sesión</div>
      <div id="infoMessage"><?php echo $message;?></div>
      <div id="login">

            <form action="<?php echo base_url().'auth/login';?>" method="post" accept-charset="utf-8">

              <fieldset class="clearfix"> 

                <p><span class="fontawesome-user"></span><input name="id" type="text" value="admin@admin.com" onBlur="if(this.value == '') this.value = 'admin@admin.com'" onFocus="if(this.value == 'admin@admin.com') this.value = ''" required></p> 
                <p><span class="fontawesome-lock"></span><input name="pass" type="password"  value="password" onBlur="if(this.value == '') this.value = 'password'" onFocus="if(this.value == 'password') this.value = ''" required></p>
                <p style="display: none"><input type="checkbox" name="remember" value="1" id="remember"></p>
                <p><input type="submit" name="submit" value="Iniciar"></p>            
              </fieldset>            
            </form>  

            <p><a href="forgot_password">Recuperar Contraseña</a></p> 

          </div>
        
        </div>
   
    </body>
</html>
