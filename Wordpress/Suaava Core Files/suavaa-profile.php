<?php
/**
 * Suavaa Profile for BuddyPress
 *
 * Displays all of the <head> section and everything up until <div id="main">
 *
 * @package WordPress
 * @subpackage Suavaa Profile
 * @since Boss 1.0.0
 */
?><!DOCTYPE html>

<?php

	$id = bp_displayed_user_id();
	$name = suavaa_bp_get_name( $id );
	$lastname = suavaa_bp_get_lastname( $id );

	
	$main_data = suavaa_get_base_fields( $id);
	$images = suavaa_bp_get_images( $id ) ;
	$social = bp_get_social_media($id);
	
	$user_role = "suavaa_role_".get_role_user();

	$linkVideo = suavaa_bp_get_link( $id ); 
	$linkTooltip = "See my life behind the scenes"; 
	$linkState = 1; 

	if( $linkVideo == ""){
		$linkTooltip = "No Video Available!";
		$linkState = 0;
	}

	//pr( get_nav_menu_locations()  );



?>

<html <?php language_attributes(); ?>>

	<head>
		<meta charset="<?php bloginfo( 'charset' ); ?>" />
		<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
		<meta name="apple-mobile-web-app-capable" content="yes" />
		<meta name="msapplication-tap-highlight" content="no"/>
		<meta http-equiv="X-UA-Compatible" content="IE=edge" />
		<link rel="profile" href="http://gmpg.org/xfn/11" />
		
		
		<?php wp_head(); ?>

	</head>

	<body class="sp <?php echo $user_role; ?>">
		
		<?php  if(is_user_logged_in() && get_role_user() == "admin" ){ do_action( 'buddyboss_before_header' );} ?>


		  <div id='preloader'>

				<div class="cv_outer">
						<div class="cv_middle">
							<div class="cv_inner">
								<div id="loader-logo"> <span class="s-icon-logoFull s-icon-white s-logo-loader"></span> </div>
								<div class="loading-container">									
									<div class="spinner-container">
										<div class="spinner spinner3"></div>		
									</div>
									
								</div>
				    		</div>
						</div>
					</div>	
				</div>

		  </div>


  <!--==========================
  Header
  ============================-->

	  <header id="header" class="header-hidden">
	    <div class="container">
	    	
	      <div id="header-logo" class="pull-left">
	      	<span class="s-icon-logoFull s-icon-blue s-logo-profile"></span>
	        <!-- Uncomment below if you prefer to use a text logo <span>-->
	        <!-- <a id="test" href="#hero">Regna</a> -->
	      </div>
	      
	      <div id="open_mobile_menu"> <span class="fa"></span> </div>

	      <div id="menu_cont" class="menu_mobile_hidden menu_mobile_disabled">
	      	  <div id="close_mobile_menu_background"></div>
	      	  <div class="nav-menu-container-scroll">
			      <nav id="nav-menu-container">		      	
			      	<div id="close_mobile_menu"> <span class="fa"></span> </div>
			        <ul class="nav-menu">

			        	<?php suavaa_get_profile_menu(); ?>	          

				        <li id="search_item">
						    <div id="header-search" class="input-group">
						      <input type="text" class="form-control" placeholder="Search">
						      <span class="input-group-btn">
						        <button class="btn btn-default" type="button">
						        	<!--<span class="glyphicon glyphicon-search"></span>-->
									<span class="fa search_icon"></span>
						        </button>
						      </span>
						    </div><!-- /input-group -->
			   		    </li>

			        </ul>

			      </nav><!-- #nav-menu-container -->

		      </div><!-- #nav-menu-container-scroll -->


	      </div>

	    </div>
	  </header><!-- #header -->

	  <!--==========================
	  Left SIDEBAR MENU
	  ============================-->

		<div id="s-side-panel" class="s-side-close">

			<div id="s-scroll-area">

				<div id="s-nav-menu" class="menu-sidepanel-container">

					<ul id="s-menu">
    
						<?php suavaa_get_profile_sidebar_menu(); ?>	      
						
					</ul>
				</div>
			</div>
		</div>


			<!--==========================
			    Youtube Window
			  ============================-->
		<div id="yt_cont" class="hidden hidingVideo">
			<div id="yt_info" class="">
				<div id="yt_logo"  class="yt_opacity"> <span class="s-icon-logoFull s-icon-white s-logo-video"></span> </div>
				<div id="yt_name"  class="yt_opacity"> <?php echo $name." ".$lastname; ?> </div>
				<div id="yt_exit_btn" class="yt_opacity"><span class="fa exit_video_btn"></span></div>
			</div>
			<div class="yt_cover"></div>
			<div class="tv">
				  <div id="tv" class="screen " ></div>
			</div>
		</div>



	<div id="master_container">
		  	
	







		<!--==========================
		    Main Cover Section
		  ============================-->
		  <section id="main" class="fullheight">
		  	<div class="main-container background fullheight" style=" background-image: url('<?php echo suavaa_bp_get_cover( $id ); ?>'); "></div>
		    <div class="main-container">
				<div class="cv_outer">
					  <div class="cv_middle">
					    <div class="cv_inner">
						      <p class="wow fadeInLeft"> <span>Get to know</span></p>
						      <p id="conatiner_name" class="wow fadeInRight" data-wow-delay="0.4s"> <span id="suavaa_user_name" > <?php echo $name; ?> </span> </p>

						      <div class="link_container wow fadeIn">
						      		<span id="tooltip_ring" yt_link="<?php echo $linkVideo ?>" tooltip="<?php echo $linkTooltip ?>" linkstate="<?php echo $linkState ?>" flow="right"></span>
						      		<span id="ring_anim"></span>
						      		<a id="youtube-link" class="glyphicon glyphicon-play" href="http://youtube.com"></a>	
						      </div>
						      
					    </div>
				  	</div>
				</div>
		    </div>
		    <div id="down_arrow" class="animating_arrow">
		    	<span class="fa down_icon"></span>
		    </div>
		  </section><!-- #main -->


		<!--==========================
		    Avatar and Data
		  ============================-->
		  <section id="main_avatar" class="">
			<div id="avatar_cont">
				<div id="suavaa_avatar" class="wow fadeInUp" data-wow-offset="300" style=" background-image: url('<?php echo suavaa_bp_get_avatar( $id ); ?>'); "></div>
			</div>
			<div id="description_cont" class="wow fadeIn" data-wow-offset="200" data-wow-delay="0.4s">
				<div id="suavaa_name"><p class="title"><?php echo $name." ".$lastname; ?></p></div>
				<div class="suavaa_separator"><span></span></div>
				<div id="suavaa_description"><p class="self_desc_text"><?php echo suavaa_bp_get_self_description( $id ); ?></p></div>
			</div>
			<div id="data_cont">
				<div id="suavaa_data">
					
				<?php
				$i =1; 
				foreach ( $main_data as $data) { ?>

					<div class="item_data_container">
						<div class="item_icon_cont_anim">
							<div class="item_icon_cont  wow zoomIn" data-wow-offset="200" data-wow-delay="0.<?php echo $i; ?>s">
								<span class="item_icon fa item_icon_<?php echo strtolower($data->name); ?>"></span>
							</div>
						</div>
						<div class="item_text_cont">
							<span class="item_data_title"><?php echo $data->name; ?>:</span>
							<span class="item_data_val"><?php echo $data->val; ?></span>
						</div>
					</div>
										
				<?php $i = $i+1;  } ?>

				</div>

			</div>

			<?php if( $social["total"] != "0" ): ?>

				<div id="suavaa_social">

					<ul id="profile_social_list">
						<?php if( $social["youtube"] != "" ){ ?> <li><span class="item_icon_cont_social"><a href='<?php echo $social["youtube"]; ?>' class="item_icon item_icon_youtube" target="_blank"></a></span></li> <?php } ?>
						<?php if( $social["facebook"] != "" ){ ?> <li><span class="item_icon_cont_social"><a href='<?php echo $social["facebook"]; ?>' class="item_icon item_icon_facebook" target="_blank"></a></span></li> <?php } ?>
						<?php if( $social["twitter"] != "" ){ ?> <li><span class="item_icon_cont_social"><a href='<?php echo $social["twitter"]; ?>' class="item_icon item_icon_twitter" target="_blank"></a></span></li> <?php } ?>
						<?php if( $social["instagram"] != "" ){ ?> <li><span class="item_icon_cont_social"><a href='<?php echo $social["instagram"]; ?>' class="item_icon item_icon_instagram" target="_blank"></a></span></li> <?php } ?>
					</ul>
					
				</div>
			<?php endif; ?>

		  </section><!-- #Avatar&Data -->

		
		<!--==========================
		    Second Image
		  ============================-->
		  <section id="second-image" class="fullheight">
		  	<div class="main-container background fullheight" style=" background-image: url('<?php echo suavaa_bp_get_second_cover( $id ); ?>'); "></div>
		    <div class="main-container">
				<div class="cv_outer">
					  <div class="cv_middle">
					    <div class="cv_inner">
					    	<div class="info_second_cover">
						      	<p class="upper wow fadeInDown" data-wow-offset="300"> <?php echo suavaa_bp_get_about_desc( $id ); ?> </p>
					      	</div>
					    </div>
				  	</div>
				</div>
		    </div>
		  </section><!-- #secon image -->


		<!--==========================
		    About Me
		  ============================-->		
		<section id="about" class="">

			<div class="container">
				
				<div class="row">
					<div class="about-title center-text upper"><h1 class="title">About me</h1></div>
				</div>
				
				<div class="row">
			        <div class="col-md-6">
			        	<div class="about-img-cont center-text wow fadeInLeft" data-wow-offset="200">
			        		<img src="<?php echo suavaa_bp_get_about_image( $id ); ?>">
			        	</div>
			        </div>
			        <div class="col-md-6">
			        	<div class="about-text wow fadeInRight" data-wow-offset="100" data-wow-delay="0.2s">
			        		<?php echo suavaa_bp_get_about( $id ); ?>
			        	</div>			            
			        </div>
				</div>

			</div>

		</section><!-- #AboutMe -->

		<!--==========================
		    Gallery
		  ============================-->
		<section id="suavaa-gallery" class="">

			<div class="container">
				
				<div class="row">
					<div class="about-title center-text upper"><h1 class="title">WORTH A THOUSAND WORDS</h1></div>
				</div>

				<div class="row">
					<div class="gallery-container">
						 

					      <button id="prev"> <span class="fa arrowleft"></span> </button>
					      <button id="next"> <span class="fa arrowright"></span> </button>



						    <div id="carousel">

					
							<?php foreach ( $images as $img) { ?>

								  <div id="gal_img_<?php echo $img->id; ?>" dot="<?php echo $img->id; ?>">
							      	  	<img src="<?php echo $img->val; ?>">
							      </div>

							<?php } ?>

						    </div>

					      
					      <ul id="gal_dots">
							<?php foreach ( $images as $img) { ?>

								  <li id="dot_gal_img_<?php echo $img->id; ?>"><a href="javascript:void(0)" onclick="setImgDots('gal_img_<?php echo $img->id; ?>',this);"></a></li>

							<?php } ?>
					      		
					      </ul>


					</div>
				</div>
				
				<div class="row">
					<div class="contact-btn"> <a href="<?php echo suavaa_get_message_link( bp_displayed_user_id() ) ?>">Message Me</a> </div>
				</div>

				<div class="row cont_terms">

					<a class="terms_footer" href="<?php echo get_home_url().'/contact-us';?>">Contact Us</a>
					<a class="terms_footer" href="<?php echo get_home_url().'/terms-of-use';?>">Terms of Use</a>
					<a class="terms_footer" href="<?php echo get_home_url().'/privacy-policy';?>">Privacy Policy</a>

				</div>
				
			</div>



		</section><!-- #Gallery -->

	</div>



	<?php wp_footer(); ?>
	</body>

</html>