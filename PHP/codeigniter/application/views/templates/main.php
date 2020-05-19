<?php extract( user() ); ?>

<!DOCTYPE html>
<html class="no-js css-menubar" lang="en">

<head>
	<meta http-equiv="content-type" content="text/html;charset=utf-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
	<meta name="description" content="bootstrap admin template">
	<meta name="author" content="">

	<title>The Dot Studio</title>

	
	<!-- Stylesheets -->
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/css/bootstrap.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/css/bootstrap-extend.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/base/assets/css/site.min09a2.css?v2.1.0">

	<!-- Plugins -->
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/animsition/animsition.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/asscrollable/asScrollable.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/switchery/switchery.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/intro-js/introjs.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/slidepanel/slidePanel.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/flag-icon-css/flag-icon.min09a2.css?v2.1.0">

	<!-- Plugins For This Page -->
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/nprogress/nprogress.min.css?v2.1.0">
  	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/clockpicker/clockpicker.min09a2.css?v2.1.0">
  	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/bootstrap-datepicker/bootstrap-datepicker.min09a2.css?v2.1.0">
  	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/vendor/bootstrap-touchspin/bootstrap-touchspin.min09a2.css?v2.1.0">

	<!-- Page -->
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/base/assets/examples/css/dashboard/v1.min09a2.css?v2.1.0">

	<!-- Fonts -->
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/web-icons/web-icons.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/brand-icons/brand-icons.min09a2.css?v2.1.0">
	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/glyphicons/glyphicons.min.css?v2.1.0">
	<link rel='stylesheet' href='<?php echo base_url().'assets';?>/global/fonts/google/cssade9.css?family=Roboto:300,400,500,300italic'>

	<link rel="stylesheet" href="<?php echo base_url().'assets';?>/global/fonts/weather-icons/weather-icons.min09a2.css?v2.1.0">

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
	<!-- Core	-->
	<script src="<?php echo base_url().'assets';?>/global/vendor/jquery/jquery.min.js"></script>	
	
	<script>
		Breakpoints();
	</script>
</head>
<body class="dashboard">
	<!--[if lt IE 8]>
				<p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
		<![endif]-->

	<nav class="site-navbar navbar navbar-default navbar-fixed-top navbar-mega" role="navigation">

		<div class="navbar-header">
			<button type="button" class="navbar-toggle hamburger hamburger-close navbar-toggle-left hided"
			data-toggle="menubar">
				<span class="sr-only">Toggle navigation</span>
				<span class="hamburger-bar"></span>
			</button>
			<button type="button" class="navbar-toggle collapsed" data-target="#site-navbar-collapse"
			data-toggle="collapse">
				<i class="icon wb-more-horizontal" aria-hidden="true"></i>
			</button>
			<div class="navbar-brand navbar-brand-center site-gridmenu-toggle" data-toggle="gridmenu">
				<img class="navbar-brand-logo" src="<?php echo base_url().'assets';?>/base/assets/images/logo.png" title="The Dot Studio">
				<span class="dotTitle"> The Dot Studio</span>
			</div>
			<button type="button" class="navbar-toggle collapsed" data-target="#site-navbar-search"
			data-toggle="collapse">
				<span class="sr-only">Toggle Search</span>
				<i class="icon wb-search" aria-hidden="true"></i>
			</button>
		</div>

		<div class="navbar-container container-fluid">
			<!-- Navbar Collapse -->
			<div class="collapse navbar-collapse navbar-collapse-toolbar" id="site-navbar-collapse">
				<!-- Navbar Toolbar -->
				<ul class="nav navbar-toolbar">
					<li class="hidden-float" id="toggleMenubar">
						<a data-toggle="menubar" href="#" role="button">
							<i class="icon hamburger hamburger-arrow-left">
									<span class="sr-only">Toggle menubar</span>
									<span class="hamburger-bar"></span>
								</i>
						</a>
					</li>
					<li class="hidden-xs" id="toggleFullscreen">
						<a class="icon icon-fullscreen" data-toggle="fullscreen" href="#" role="button">
							<span class="sr-only">Toggle fullscreen</span>
						</a>
					</li>

				</ul>
				<!-- End Navbar Toolbar -->

				<!-- Navbar Toolbar Right -->
				<ul class="nav navbar-toolbar navbar-right navbar-toolbar-right">
					<li class="dropdown">
						<a class="navbar-avatar dropdown-toggle" data-toggle="dropdown" href="#" aria-expanded="false"
						data-animation="scale-up" role="button">
							<span class="avatar avatar-online">
								<img src="<?php echo base_url().'assets';?>/global/portraits/5.jpg" alt="...">
								<i></i>
							</span>
						<span> <?php echo $email." - ".$name ?> </span>
						</a>
						<ul class="dropdown-menu" role="menu">
							<li class="divider" role="presentation"></li>
							<li role="presentation">
								<a href="<?php echo site_url(); ?>auth/logout" role="menuitem"><i class="icon wb-power" aria-hidden="true"></i> Salir </a>
							</li>
						</ul>
					</li>
				 <li id="toggleChat">
				<a class="btnG" href="<?php echo site_url(); ?>auth/logout" role="button">
					<i class="icon glyphicon glyphicon-log-out" aria-hidden="true"></i>
				</a>
					</li>
				</ul>
				<!-- End Navbar Toolbar Right -->
			</div>
			<!-- End Navbar Collapse -->

			<!-- Site Navbar Seach -->
			<div class="collapse navbar-search-overlap" id="site-navbar-search">
				<form role="search">
					<div class="form-group">
						<div class="input-search">
							<i class="input-search-icon wb-search" aria-hidden="true"></i>
							<input type="text" class="form-control" name="site-search" placeholder="Search...">
							<button type="button" class="input-search-close icon wb-close" data-target="#site-navbar-search"
							data-toggle="collapse" aria-label="Close"></button>
						</div>
					</div>
				</form>
			</div>
			<!-- End Site Navbar Seach -->
		</div>
	</nav>
	<div class="site-menubar">
		<div class="site-menubar-body">
			<div>
				<div>
					<ul class="site-menu">

						<li class="site-menu-category">Menú</li>

						<li class="site-menu-item">
							<a href="<?php echo site_url(); ?>home">
								<i class="site-menu-icon wb-home" aria-hidden="true"></i>
								<span class="site-menu-title"><strong>Inicio</strong></span>
							</a>
						</li>

						<?php  if(user("rol")==1){ ?>
						<li class="site-menu-item">
							<a href="<?php echo site_url(); ?>usuarios">
								<i class="site-menu-icon wb-users" aria-hidden="true"></i>
								<span class="site-menu-title"><strong>Usuarios</strong></span>
							</a>
						</li>
						<?php } ?>

						<li class="site-menu-item">
							<a href="<?php echo site_url(); ?>capacitaciones">
								<i class="site-menu-icon wb-book" aria-hidden="true"></i>
								<span class="site-menu-title"><strong>Capacitaciones</strong></span>
							</a>
						</li>

						<li class="site-menu-item">
							<a href="<?php echo site_url(); ?>auth/logout">
								<i class="site-menu-icon icon glyphicon glyphicon-log-out" aria-hidden="true"></i>
								<span class="site-menu-title"><strong>Salir</strong></span>
							</a>
						</li>						
												
					</ul>

		
				</div>
			</div>
		</div>


	</div>
	<div class="site-gridmenu">
		<div>
			<div>
				<ul>
					<li>
						<a href="apps/mailbox/mailbox.html">
							<i class="icon wb-envelope"></i>
							<span>Mailbox</span>
						</a>
					</li>
					<li>
						<a href="apps/calendar/calendar.html">
							<i class="icon wb-calendar"></i>
							<span>Calendar</span>
						</a>
					</li>
					<li>
						<a href="apps/contacts/contacts.html">
							<i class="icon wb-user"></i>
							<span>Contacts</span>
						</a>
					</li>
					<li>
						<a href="apps/media/overview.html">
							<i class="icon wb-camera"></i>
							<span>Media</span>
						</a>
					</li>
					<li>
						<a href="apps/documents/categories.html">
							<i class="icon wb-order"></i>
							<span>Documents</span>
						</a>
					</li>
					<li>
						<a href="apps/projects/projects.html">
							<i class="icon wb-image"></i>
							<span>Project</span>
						</a>
					</li>
					<li>
						<a href="apps/forum/forum.html">
							<i class="icon wb-chat-group"></i>
							<span>Forum</span>
						</a>
					</li>
					<li>
						<a href="index.html">
							<i class="icon wb-dashboard"></i>
							<span>Dashboard</span>
						</a>
					</li>
				</ul>
			</div>
		</div>
	</div>


	<!-- Page -->
	<div class="page animsition">
		<div class="page-content padding-30 container-fluid">
		
	<?php echo $body; ?>
	
	</div>
	</div>
	<!-- End Page -->


	<!-- Footer -->
	<footer class="site-footer">
		<div class="site-footer-legal">© 2016 <a href="javascript:void(0)">TheDot-Studio</a></div>
		<div class="site-footer-right">
			
		</div>
	</footer>
	<!-- Core	-->
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
	<script src="<?php echo base_url().'assets';?>/global/vendor/skycons/skycons.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/jquery-appear/jquery.appear.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/nprogress/nprogress.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/aspieprogress/jquery-asPieProgress.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/matchheight/jquery.matchHeight-min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/jquery-placeholder/jquery.placeholder.min.js"></script>
  	<script src="<?php echo base_url().'assets';?>/global/vendor/typeahead-js/bloodhound.min.js"></script>	
	  
	<script src="<?php echo base_url().'assets';?>/global/vendor/bootstrap-datepicker/bootstrap-datepicker.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/asspinner/jquery-asSpinner.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/clockpicker/bootstrap-clockpicker.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/vendor/bootstrap-touchspin/jquery.bootstrap-touchspin.min.js"></script>
	  
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
	<script src="<?php echo base_url().'assets';?>/global/js/components/matchheight.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/js/components/material.min.js"></script>
	
	<script src="<?php echo base_url().'assets';?>/global/js/components/asspinner.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/js/components/clockpicker.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/js/components/bootstrap-datepicker.min.js"></script>
	<script src="<?php echo base_url().'assets';?>/global/js/components/bootstrap-touchspin.min.js"></script>

    

	<script>

		$(document).ready(function($){
			Site.run();
		});

	</script>



</body>



</html>