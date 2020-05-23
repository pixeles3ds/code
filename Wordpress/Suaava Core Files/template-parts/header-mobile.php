<?php global $woocommerce; ?>
<div id="mobile-header" class="table <?php echo ( boss_get_option( 'boss_adminbar' ) ) ? 'with-adminbar' : ''; ?>">

	<!-- Toolbar for Mobile -->
	<div class="mobile-header-outer table-cell">

		<div class="mobile-header-inner table">

			<!-- Custom menu trigger button -->
			<div id="custom-nav-wrap" class="btn-wrap">
				<a href="#" id="custom-nav" class="sidebar-btn fa fa-bars"></a>
			</div>

			<?php
			if ( boss_get_option( 'boss_search_instead' ) && is_user_logged_in() ) {
				echo get_search_form();
			} else {
				if ( boss_get_option( 'logo_switch' ) && boss_get_option( 'boss_logo', 'id' ) ) {
					?>

					<div id="mobile-logo" class="table-cell">
						<span class="bb-title-large s-icon-logoFull s-icon-white s-logo-mobile"></span>
					</div>

				<?php } else { ?>
					<h1 class="table-cell">
						<span class="bb-title-large s-icon-logoFull s-icon-white s-logo-mobile"></span>
					</h1>
					<?php
				}
			}
			?>

            <!-- Woocommerce Notification for the users-->
            <?php echo boss_mobile_cart_icon_html(); ?>

			<!-- Profile menu trigger button -->
			<?php if ( is_user_logged_in() || (!is_user_logged_in() && buddyboss_is_bp_active() ) ) { ?>

				<div id="profile-nav-wrap" class="btn-wrap">
					<a href="#" id="profile-nav" class="sidebar-btn fa fa-user table-cell"><span id="ab-pending-notifications-mobile" class="pending-count no-alert"></span></a>
				</div>

			<?php } ?>



		</div>

	</div>

</div><!-- #mobile-header -->