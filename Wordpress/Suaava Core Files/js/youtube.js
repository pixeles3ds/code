
var tag = document.createElement('script');
		
var firstScriptTag = document.getElementsByTagName('script')[0];

var tv;
var	playerDefaults = {autoplay: 0, autohide: 1, loop : 1, modestbranding: 0, rel: 0, showinfo: 0, controls: 0, disablekb: 1, enablejsapi: 1, iv_load_policy: 3};



function stopVideo(){
    tv.stopVideo();
}

function onPlayerStateChange(e) {
  if (e.data === 1){
    
    $('#tv').addClass('active');    

  } else if (e.data === 2){

    //$('#tv').removeClass('active');
    //tv.loadVideoById(vid);
    //tv.seekTo(vid.startSeconds);

  }
}

function vidRescale(){

  var w = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth,
    h = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

  if (w/h > 16/9){
    tv.setSize(w, w/16*9);
    $('.tv .screen').css({'left': '0px'});
  } else {
    tv.setSize(h/9*16, h);
    $('.tv .screen').css({'left': -($('.tv .screen').outerWidth()-w)/2});
  }
}






function onYouTubePlayerAPIReady(){
  tv = new YT.Player('tv', {events: {'onReady': onPlayerReady, 'onStateChange': onPlayerStateChange}, playerVars: playerDefaults});
}

function onPlayerReady(){
  //tv.mute();
}

function playVideo( id ){
    var vid = {'videoId': id, 'suggestedQuality': 'hd720'}; 
    vidRescale();
	tv.seekTo(0);
    tv.loadVideoById( vid );    
	tv.seekTo(0);
}

$(".yt_cover").click(function(){
  if( tv.getPlayerState() == 1 ){
      tv.pauseVideo();
  }else if( tv.getPlayerState() == 2){
      tv.playVideo();
  }

});

$(window).on('load', function(){

    tag.src = 'https://www.youtube.com/player_api';
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
  
});

$(window).on('resize', function(){
  if(tv !== undefined){
    vidRescale();
  }  
});