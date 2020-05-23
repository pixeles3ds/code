

<div id="referrer" class="refer_block">
	Referrer: <a href="<?php echo get_home_url().'/members/'.suavaa_bp_get_refer( bp_displayed_user_id() ); ?>"><?php echo suavaa_bp_get_refer( bp_displayed_user_id() ); ?></a>
</div>

<div id="refer_container">
	<div id="refer_code" class="refer_block">
		<div class="refer_title">Referral code:</div>
		<div class="refer_value"><input value="<?php echo bp_core_get_username( bp_displayed_user_id() ); ?>"></div>
	</div>
	<div id="refer_url" class="refer_block">
		<div class="refer_title">Referral Invitation URL:</div>
		<div class="refer_value"><input value="<?php echo get_home_url()."/register/?refer=".bp_core_get_username( bp_displayed_user_id() ); ?> "></div>
	</div>
	<div id="refer_link" class="refer_block">
		<div class="refer_title"> <a href='<?php echo get_home_url()."/register/?refer=".bp_core_get_username( bp_displayed_user_id() ); ?>'>Register on Suavaa link:</a> </div>
		<div class="refer_value"><input value="<?php echo "&lt;a href='".get_home_url()."/register/?refer=".bp_core_get_username( bp_displayed_user_id() )."'&gt; Register on Suavaa &lt;/a&gt;"; ?>"></div>
	</div>
</div>

<?php
	
	$refer_list = get_referrals( bp_displayed_user_id() );
	$total = count($refer_list);
	
	
	echo "<div class='refer_counter'> $total Referrals </div>";
	
	echo "<ul class='refer_list_container'>";
	
	foreach( $refer_list as $user){
		
		$id = $user->id;
		
		echo "<li>";
		echo "<div class='ref_avatar'><a href='". bp_core_get_user_domain( $id ) ."'><img src='". suavaa_bp_get_avatar( $id ) ."' width='35' height='35'> </a></div>";
		echo "<div class='ref_name'><a href='". bp_core_get_user_domain( $id ) ."'> ".suavaa_bp_get_name($id)." ".suavaa_bp_get_lastname($id)  ." </a></div>";
		echo "</li>";

		
	}
	
	echo "</ul>";
?>




