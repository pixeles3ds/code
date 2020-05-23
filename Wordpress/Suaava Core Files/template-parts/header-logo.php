<?php
/*
 * Logo Option
 */

$show		 = boss_get_option( 'logo_switch' );
$show_mini	 = boss_get_option( 'mini_logo_switch' );

$logo_id		 = boss_get_option( 'boss_logo', 'id' );
$logo_small_id	 = boss_get_option( 'boss_small_logo', 'id' );

$site_title = get_bloginfo( 'name' );

$logo_large	 = ( $show && $logo_id ) ? wp_get_attachment_image( $logo_id, 'full', '', array( 'class' => 'boss-logo large' ) ) : '<span class="bb-title-large s-icon-logoFull s-icon-white s-logo-dashboard"></span>';
$logo_small	 = ( $show_mini && $logo_small_id ) ? wp_get_attachment_image( $logo_small_id, 'full', '', array( 'class' => 'boss-logo small' ) ) : '<span class="bb-title-small s-icon-logoS s-icon-white s-logo-dashboard-small"></span>';

// This is for better seo
$elem = ( is_front_page() && is_home() ) ? 'h1' : 'h2';
?>

<div id="logo" class="logo-container">
	
	<?php if( is_user_logged_in() ){ ?>

	<a href="<?php echo esc_url( get_member_domain()."profile/" ); ?>" rel="home">
		<?php echo $logo_large; ?>
		<?php echo $logo_small; ?>
	</a>
	
	<?php }else{ ?>

	<a href="<?php echo esc_url( "https://suavaa.com" ); ?>" rel="home">
		<?php echo $logo_large; ?>
		<?php echo $logo_small; ?>
	</a>	
	
	<?php } ?>



</div>
