<?php
  $message = preg_replace("/\s+/", " ", $message );
?>

<!DOCTYPE html>
<html class="no-js css-menubar" lang="en">

<!-- Mirrored from getbootstrapadmin.com/remark/base/pages/register.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 05 Feb 2016 00:38:49 GMT -->
<!-- Added by HTTrack --><meta http-equiv="content-type" content="text/html;charset=utf-8" /><!-- /Added by HTTrack -->
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
  <meta name="description" content="bootstrap admin template">
  <meta name="author" content="">

  <title>The Dot Studio</title>

  <link rel="apple-touch-icon" href="<?php echo base_url().'assets';?>/base/assets/images/apple-touch-icon.png">
  <link rel="shortcut icon" href="<?php echo base_url().'assets';?>/base/assets/images/favicon.ico">

  <!-- Stylesheets -->
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/css/bootstrap.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/css/bootstrap-extend.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/base/assets/css/site.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/base/assets/css/style.css?v2.1.0">

  <!-- Skin tools (demo site only) -->
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/css/skintools.min09a2.css?v2.1.0">

  <!-- Plugins -->
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/animsition/animsition.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/asscrollable/asScrollable.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/switchery/switchery.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/intro-js/introjs.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/slidepanel/slidePanel.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/flag-icon-css/flag-icon.min09a2.css?v2.1.0">

  <!-- Page -->
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/base/assets/examples/css/pages/register.min09a2.css?v2.1.0">

  <!-- Fonts -->
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/web-icons/web-icons.min09a2.css?v2.1.0">
  <link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/brand-icons/brand-icons.min09a2.css?v2.1.0">
  <link rel='stylesheet' href='<?php echo base_url().'assets';?>/global/fonts/google/cssade9.css?family=Roboto:300,400,500,300italic'>


  <!--[if lt IE 9]>
    <script src="<?php echo base_url().'assets';?>/global/vendor/html5shiv/html5shiv.min.js"></script>
    <![endif]-->

  <!--[if lt IE 10]>
    <script src="<?php echo base_url().'assets';?>/global/vendor/media-match/media.match.min.js"></script>
    <script src="<?php echo base_url().'assets';?>/global/vendor/respond/respond.min.js"></script>
    <![endif]-->

  <!-- Scripts -->
  <script src="<?php echo base_url().'assets';?>/global/vendor/modernizr/modernizr.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/breakpoints/breakpoints.min.js"></script>
  <script>
    Breakpoints();
  </script>
</head>
<body class="page-register layout-full page-dark">
  <!--[if lt IE 8]>
        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    <![endif]-->


  <!-- Page -->
  <div class="page animsition vertical-align text-center" data-animsition-in="fade-in" data-animsition-out="fade-out">


    <div class="page-content vertical-align-middle">
	
      <div class="brand">
        <img class="brand-img" src="<?php echo base_url().'assets';?>/base/assets/images/logo.png" alt="...">
        <h2 class="brand-text">The Dot Studio</h2>
      </div>

      <?php
        if($message){
          echo '<div class="errormsg">'.$message.'</div>';
        }
      ?>
	  
	<div class="" style="width:800px">
	
	  <div class="" style="float:left; width:400px">
	  
		  <p> ¿Eres Nuevo? Regístrate</p>
		  
		  <form action="<?php echo site_url(); ?>usuarios/create_user_and_login" method="post" role="form" style="width:300px" accept-charset="utf-8" >
			<div class="form-group">			  
			  <input type="text" class="form-control" id="inputName" name="first_name" placeholder="Nombre">
			</div>
			<div class="form-group">			  
			  <input type="email" class="form-control" id="inputEmail" name="email" placeholder="Email">
			</div>
			<div class="form-group">			  
			  <input type="password" class="form-control" id="inputPassword" name="password" placeholder="Password">
			</div>
			<div class="form-group">
			  <input type="password" class="form-control" id="inputPasswordCheck" name="password_confirm" placeholder="Confirmar Password">
			</div>
			<button type="submit" class="btn btn-primary btn-block">Registrarse</button>
		  </form>
		  
      </div>

	  <div class="" style="float:left; width:400px">
	  
		  <p>Iniciar Sesión</p>
		  <form action="<?php echo site_url(); ?>auth/login" method="post" role="form" style="width:300px" accept-charset="utf-8" >
		  
			
			<div class="form-group">
			  <input type="email" class="form-control" id="inputEmail" name="id" value="admin@admin.com" placeholder="Email">
			</div>
			<div class="form-group">
			  
			  <input type="password" class="form-control" id="inputPassword" name="pass" value="admin" placeholder="Password">
			</div>
			<div class="form-group">

			<button type="submit" class="btn btn-primary btn-block">Iniciar</button>
		  </form>
		  
      </div>
	</div>	  
	  
      <footer class="page-copyright page-copyright-inverse">
        <p>WEBSITE BY pixeles3d.com</p>
        <p>© 2016. Todos los derechos reservados.</p>
        <div class="social">
          <a href="javascript:void(0)">
            <i class="icon bd-twitter" aria-hidden="true"></i>
          </a>
          <a href="javascript:void(0)">
            <i class="icon bd-facebook" aria-hidden="true"></i>
          </a>
          <a href="javascript:void(0)">
            <i class="icon bd-dribbble" aria-hidden="true"></i>
          </a>
        </div>
      </footer>
    </div>
  </div>
  <!-- End Page -->


  <!-- Core  -->
  <script src="<?php echo base_url().'assets';?>/global/vendor/jquery/jquery.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/bootstrap/bootstrap.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/animsition/animsition.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/asscroll/jquery-asScroll.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/mousewheel/jquery.mousewheel.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/asscrollable/jquery.asScrollable.all.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/ashoverscroll/jquery-asHoverScroll.min.js"></script>

  <!-- Plugins -->
  <script src="<?php echo base_url().'assets';?>/global/vendor/switchery/switchery.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/intro-js/intro.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/screenfull/screenfull.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/vendor/slidepanel/jquery-slidePanel.min.js"></script>

  <!-- Plugins For This Page -->
  <script src="<?php echo base_url().'assets';?>/global/vendor/jquery-placeholder/jquery.placeholder.min.js"></script>

  <!-- Scripts -->
  <script src="<?php echo base_url().'assets';?>/global/js/core.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/base/assets/js/site.min.js"></script>

  <script src="<?php echo base_url().'assets';?>/base/assets/js/sections/menu.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/base/assets/js/sections/menubar.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/base/assets/js/sections/gridmenu.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/base/assets/js/sections/sidebar.min.js"></script>

  <script src="<?php echo base_url().'assets';?>/global/js/configs/config-colors.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/base/assets/js/configs/config-tour.min.js"></script>

  <script src="<?php echo base_url().'assets';?>/global/js/components/asscrollable.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/js/components/animsition.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/js/components/slidepanel.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/js/components/switchery.min.js"></script>

  <script src="<?php echo base_url().'assets';?>/global/js/components/jquery-placeholder.min.js"></script>
  <script src="<?php echo base_url().'assets';?>/global/js/components/animate-list.min.js"></script>


  <script>
    (function(document, window, $) {
      'use strict';

      var Site = window.Site;
      $(document).ready(function() {
        Site.run();
      });
    })(document, window, jQuery);
  </script>

</body>


<!-- Mirrored from getbootstrapadmin.com/remark/base/pages/register.html by HTTrack Website Copier/3.x [XR&CO'2014], Fri, 05 Feb 2016 00:38:50 GMT -->
</html>