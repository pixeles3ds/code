//posicion inicial del cursor
var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
var lastScroll = 0;
var scrollDir = "";


var scroll_action = 0;

var menu_highest_width = 0;

var carousel_desktop_seted = 0;

//------------------------------------------
// Es Movil
//------------------------------------------



function prefixCSS( sel, val ) {
	$( sel ).css( {
		'-webkit-transform': val,
		'-moz-transform': val,
		'-ms-transform': val,
		'-o-transform': val,
		'transform': val
	} );
}

function isMobile() {
	return ( /(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino|android|ipad|playbook|silk/i.test( navigator.userAgent || navigator.vendor || window.opera ) || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test( ( navigator.userAgent || navigator.vendor || window.opera ).substr( 0, 4 ) ) )
}
var mobile = isMobile();



//================================================
//================================================
// 			Animate.css and JQuery
//================================================
//================================================

function animcss( sel, anim ) {
	$( sel ).animateCss( anim );
	$( sel ).css( {
		"visibility": "visible"
	} );
}



function switch_submenu_mobile( submenu ) {
	if ( $( "." + submenu ).hasClass( "opened" ) ) {
		$( "." + submenu ).removeClass( "opened" );
	} else {
		$( "." + submenu ).addClass( "opened" );
	}
}


//-------------------------------------------
// scrollTo
//-------------------------------------------
function scrollToDiv( sel, offset ) {
	anim = 1;
	$( 'html, body' ).animate( {
		scrollTop: $( sel ).offset().top + offset
	}, 1000, 'easeInOutQuad', function() {
		setTimeout( function() {
			if ( anim == 1 ) {
				anim = 0;
			}
		}, 50 )

	} );
}

function scrollToPos( num ) {
	anim = 1;
	$( 'html, body' ).animate( {
		scrollTop: num
	}, 1000, 'easeInOutQuad', function() {
		setTimeout( function() {
			if ( anim == 1 ) {
				anim = 0;
			}
		}, 50 )
	} );
}

//-------------------------------------------
// onScroll
//-------------------------------------------

var anim = 0;

function checkScroll() {


	scroll = $( window ).scrollTop();

	if ( !mobile ) {

	}


	//show bar menu
	if ( scroll > 1 ) {
		if ( scroll_action == 0 ) {

			setTimeout( function() {
				$( '#header' ).removeClass( 'header-hidden' )
			}, 50 );
			setTimeout( function() {
				$( '#s-side-panel' ).addClass( 'side-fixed' );
				$( '#master_container' ).addClass( 'showed-sidebar' );
			}, 600 );

			if ( $( "#suavaa_avatar" ).css( "visibility" ) == "visible" ) {
				setTimeout( function() {
					$( '#avatar_cont' ).removeClass( 'hide_avatar' );
				}, 100 );
				$( "#down_arrow" ).removeClass( "animating_arrow" );
			}

			scroll_action = 1;
		}

		if ( scroll > 44 ) {
			//$('#header').removeClass('header-hidden');
			$( '.suavaa_role_admin #header' ).addClass( 'menu_fixed' );
		} else {
			$( '.suavaa_role_admin #header' ).removeClass( 'menu_fixed' );
		}

	} else {

		//setTimeout( function(){ $('#header').addClass('header-hidden')}, 100);
		$( '#header' ).addClass( 'header-hidden' );
		$( '#s-side-panel' ).removeClass( 'side-fixed' );
		$( '#master_container' ).removeClass( 'showed-sidebar' );


		if ( $( "#suavaa_avatar" ).css( "visibility" ) == "visible" ) {
			$( '#avatar_cont' ).addClass( 'hide_avatar' );

		}
		scroll_action = 0;


	}
	lastScroll = scroll;

}
//-------------------------------------------
// onLoad
//-------------------------------------------


function setInitConf() {

	window.scrollTo( 0, 0 );

	setResolution();

	setGallery();

	var scrollTop = $( window ).scrollTop();
	lastScroll = scrollTop;

	checkScroll();

	setTimeout( function() {

		window.scrollTo( 0, 0 );

		$( "#preloader" ).addClass( "hidepreloader" );

		setTimeout( function() {

			$( "#preloader" ).addClass( "opacityloader" );

			setTimeout( function() {
				$( "#preloader" ).hide();
				new WOW().init();
			}, 800 );
		}, 800 );

	}, 800 );


	var hammertime = new Hammer( $( "#carousel" )[ 0 ] );

	hammertime.get( 'swipe' ).set( {
		velocity: 0.05,
		threshold: 3
	} );

	hammertime.on( "swipeleft swiperight", function( ev ) {
		if ( ev.type == "swipeleft" ) {
			moveToSelected( 'next' );
		}
		if ( ev.type == "swiperight" ) {
			moveToSelected( 'prev' );
		}
	} );


	setTimeout( function() {
		carouselResponsive();
	}, 10 );


	if ( mobile ) {
		$( "body" ).addClass( "mobile_ios" );
	}

	// Test Purpose
	//$("#preloader").hide();
	//setTimeout(function(){  new WOW().init(); },500);
	//$('#header').removeClass('header-hidden');

}




//-------------------------------------------
// CAROUSEL
//-------------------------------------------

var pendingNumerator = 992 - 320;

var initSize = [];
var finalSize = [];
var galPending = [];
var resSize = [];


initSize.middle = 220;
initSize.next = 150;
initSize.secNext = 80;
initSize.last = 50;

finalSize.middle = 600;
finalSize.next = 400;
finalSize.secNext = 250;
finalSize.last = 200;

galPending.middle = ( finalSize.middle - initSize.middle ) / pendingNumerator;
galPending.next = ( finalSize.next - initSize.next ) / pendingNumerator;
galPending.secNext = ( finalSize.secNext - initSize.secNext ) / pendingNumerator;
galPending.last = ( finalSize.last - initSize.last ) / pendingNumerator;

resSize.middle = 0;
resSize.next = 0;
resSize.secNext = 0;
resSize.last = 0;

function carouselResponsive() {
	/*
	if( width < 992 ){		
		
		resSize.middle = galPending.middle * ( width - 320 ) + initSize.middle;
		resSize.next = galPending.next * ( width - 320 ) + initSize.next;
		resSize.secNext = galPending.secNext * ( width - 320 ) + initSize.secNext;
		resSize.last = galPending.last * ( width - 320 ) + initSize.last;

		$("#carousel div.selected img").css('width', resSize.middle+'px');			
		$("#carousel div.next img, #carousel div.prev img").css('width', resSize.next+'px');			
		$("#carousel div.nextRightSecond img, #carousel div.prevLeftSecond img").css('width', resSize.secNext+'px');	
		$("#carousel div.hideRight img, #carousel div.hideLeft img").css('width', resSize.last+'px');	

		carousel_desktop_seted = 0;

	}else{

		if( carousel_desktop_seted == 0 ){
			$("#carousel div.selected img").css('width','');			
			$("#carousel div.next img, #carousel div.prev img").css('width', '');			
			$("#carousel div.nextRightSecond img, #carousel div.prevLeftSecond img").css('width', '');	
			$("#carousel div.hideRight img, #carousel div.hideLeft img").css('width','');			
		}

		carousel_desktop_seted = 1;

	}
	*/

}

function setImgDots( element, dot ) {
	$( "#gal_dots li" ).removeClass( "dotSelected" );
	$( $( dot ).parent() ).addClass( "dotSelected" );
	moveToSelected( $( "#" + element )[ 0 ] );
}

function moveToSelected( element ) {

	if ( element == "next" ) {
		var selected = $( ".selected" ).next();
	} else if ( element == "prev" ) {
		var selected = $( ".selected" ).prev();
	} else {
		var selected = element;
	}

	var next = $( selected ).next();
	var prev = $( selected ).prev();
	var prevSecond = $( prev ).prev();
	var nextSecond = $( next ).next();

	$( selected ).removeClass().addClass( "selected" );

	$( prev ).removeClass().addClass( "prev" );
	$( next ).removeClass().addClass( "next" );

	$( nextSecond ).removeClass().addClass( "nextRightSecond" );
	$( prevSecond ).removeClass().addClass( "prevLeftSecond" );

	$( nextSecond ).nextAll().removeClass().addClass( 'hideRight' );
	$( prevSecond ).prevAll().removeClass().addClass( 'hideLeft' );


	//carouselResponsive();



	var id_img = $( selected ).attr( "dot" );

	if ( id_img ) {
		$( "#gal_dots li" ).removeClass( "dotSelected" );
		$( "#gal_dots #dot_gal_img_" + id_img ).addClass( "dotSelected" );
	}
}

// Eventos teclado
$( document ).keydown( function( e ) {
	switch ( e.which ) {
		case 37: // left
			moveToSelected( 'prev' );
			break;

		case 39: // right
			moveToSelected( 'next' );
			break;

		default:
			return;
	}
	e.preventDefault();
} );

$( '#carousel div' ).click( function() {
	moveToSelected( $( this ) );
} );

$( '#suavaa-gallery #prev' ).click( function() {
	moveToSelected( 'prev' );
} );

$( '#suavaa-gallery #next' ).click( function() {
	moveToSelected( 'next' );
} );

function setGallery() {
	middle = Math.ceil( $( "#carousel img" ).length / 2 ) - 1;
	obj = $( "#carousel div" )[ middle ];
	objDot = $( "#gal_dots li" )[ middle ];

	$( objDot ).addClass( "dotSelected" );

	moveToSelected( $( obj ) );
}



//-------------------------------------------
// onResize
//-------------------------------------------

function setResolution() {

	width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
	height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

	if ( width < 992 ) {
		$( 'body' ).addClass( "menu_mobile" );
	} else {

		/*
		var offset = 30;
		var padding = 30;
		var logo = $("#header-logo").outerWidth();
		var menu = $(".nav-menu").outerWidth();
		var total = padding + logo + menu + offset;

		if( total > menu_highest_width ){ menu_highest_width = total; }

		if( menu_highest_width >= width ) {
			$('body').addClass("menu_mobile");	
		}else{
			$('body').removeClass("menu_mobile");	
		}
		*/

		$( 'body' ).removeClass( "menu_mobile" );

	}



	//console.log("total: "+menu_highest_width+" - width: "+width);

	$( '.sp .fullheight' ).css( {
		'height': height
	} );

	//carouselResponsive();

}



//================================================
//================================================
// 			 LISTENERS
//================================================
//================================================



$( "#yt_exit_btn" ).click( function() {

	window.scrollTo( 0, 0 );

	$( '#tv' ).removeClass( 'active' );

	$( '.yt_opacity' ).removeClass( 'yt_show_items' );
	$( '#yt_cont' ).removeClass( 'showingVideo' );
	$( '#yt_cont' ).addClass( 'hidingVideo' );

	setTimeout( function() {
		$( '#yt_cont' ).removeClass( 'active' );
		$( '#yt_cont' ).addClass( 'hidden' );
		stopVideo();
	}, 1000 );

} )


// Onclick Display Youtube video
$( "#tooltip_ring" ).click( function() {

	id_vid = $( "#tooltip_ring" ).attr( "yt_link" );
	vid_status = $( "#tooltip_ring" ).attr( "linkstate" );

	if ( vid_status == "1" ) {
		$( '#yt_cont' ).addClass( 'active' );
		$( '#yt_cont' ).removeClass( 'hidden' );

		setTimeout( function() {
			$( '#yt_cont' ).removeClass( 'hidingVideo' );
			$( '#yt_cont' ).addClass( 'showingVideo' );
		}, 10 );
		setTimeout( function() {
			$( '.yt_opacity' ).addClass( 'yt_show_items' );
		}, 500 );

		playVideo( id_vid );
	}
} )




$( "#open_mobile_menu" ).click( function() {

	$( "#menu_cont" ).removeClass( "menu_mobile_hidden" );
	$( "#menu_cont" ).removeClass( "menu_mobile_disabled" );
} )

$( "#close_mobile_menu,#close_mobile_menu_background" ).click( function() {
	$( "#menu_cont" ).addClass( "menu_mobile_hidden" );
	setTimeout( function() {
		$( "#menu_cont" ).addClass( "menu_mobile_disabled" );
	}, 500 );
} )

$( "#down_arrow" ).click( function() {
	scrollToDiv( "#main_avatar", -( height / 2 ) );
	$( "#down_arrow" ).removeClass( "animating_arrow" );
} )

$( "#tooltip_ring" ).hover( function() {
	$( "#ring_anim" ).addClass( "anim-ring" );
} )

$( "#tooltip_ring" ).mouseleave( function() {
	$( "#ring_anim" ).removeClass( "anim-ring" );
} )



window.addEventListener( 'resize', setResolution );
window.addEventListener( 'load', setInitConf );
$( window ).scroll( function() {
	checkScroll();
} );