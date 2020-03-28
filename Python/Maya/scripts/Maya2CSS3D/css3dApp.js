
//posicion inicial del cursor
var px = 0; 
var py = 0;
var cursorInOut = 1;
var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
var height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;

// Posicion Max de la camara en X e Y
var posMaxX = 180+0;
var posMaxY = 130+0;
// Posicion actual de la camara
var camX = 0;
var camY = 0;
// Animacion ease de camara
var tweenX = 0;
var tweenY = 0;


var zCam = 400;

var g = null; //Gyroscope Obj



//==================================================================================
//
//		3D ENGINE
//
//==================================================================================


// Constructores vacios
// Reescribir funciones:    app.startApp = function(){ }
var classApp = function(){

	this.mobile = false;

	this.updatingRender = function(){} // Funcion que se ejecuta cada vez que se renderiza, aqui va el codigo de las animaciones
	this.updatingRenderExtend = function(){} // USAR ESTA FUNCION PARA EXTENDER EL CODIGO, CADA VEZ QUE SE RENDERIZA!!!!!


	this.startApp = function(){}

	//------------------------------------------
	// Calcular posicion de la camara 
	//------------------------------------------
	this.calcCameraPos = function(){}

}





//==================================================================================
//
//		3D ENGINE
//
//==================================================================================

var app = new classApp;


// init engine and scene
var engine = new css3d(document.getElementById('container'));
var scene = new css3d.scene();
scene.getCamera().perspective = 1000;


//=======================================
// load models
//=======================================

{templateJSHead}

// Lista con los objetos del escenario
var objs = []

//=======================================

// Center of scene for lookup camera
var centerScene = new css3d.element(document.getElementById('centerScene'));
centerScene.shading = false;
centerScene.setTranslation(0, 0, 0);
scene.addElement(centerScene);


// add scene to engine
engine.setScene(scene);

if (!engine.browserSupports3d) {
	alert('This browser does not support CSS 3D');
}     



var axis = new css3d.vector3(0, 1, 0).normalize();
var rotation = -Math.PI/4;
 
engine.onRender = updateScene;


function updateScene(deltaTime){     
	app.updatingRender();
	app.updatingRenderExtend();
}




function showScene(){

	setTimeout(function(){
		document.getElementById("cargando").style.display = "none";
		document.getElementById("container").style.visibility = "visible";
	},100);
}


//========================================================================================

var soft = 0.05;
var dist = 0.1; // redondeamos y terminamos loop
var distA = 0.01; // redondeamos y terminamos loop

function renderAnim(){
	
	for(i=0; i < objs.length; i++){

		if( objs[i].anim == 1 ){
			objs[i].tx += ( objs[i].txd - objs[i].tx) * soft;
			objs[i].ty += ( objs[i].tyd - objs[i].ty) * soft;
			objs[i].tz += ( objs[i].tzd - objs[i].tz) * soft;			
			objs[i].setTranslation(objs[i].tx, objs[i].ty, objs[i].tz);
			
			if( objs[i].alpha != objs[i].alphad ){
				objs[i].alpha += ( objs[i].alphad - objs[i].alpha) * 0.1;
				
				hijos = objs[i]._children;
				
				for(j=0; j < hijos.length; j++){

					if( Math.abs( objs[i].alphad - objs[i].alpha ) < 0.02 ){
						objs[i].alpha = objs[i].alphad;
					}

					hijos[j]._domElement.style.opacity = objs[i].alpha;
				}
			}

			// Redondeamos para finalizar el loop rapidamente
			resX = Math.abs( objs[i].txd - objs[i].tx )
			resY = Math.abs( objs[i].tyd - objs[i].ty )
			resZ = Math.abs( objs[i].tzd - objs[i].tz )
			resA = Math.abs( objs[i].alphad - objs[i].alpha )
			
			if( resX < dist && resY < dist && resZ < dist && resA < distA){ 
				objs[i].anim = 0;
			}
		}
	}
	
}

function setPos(obj,val){
	obj.txd = val[0];
	obj.tyd = val[1];
	obj.tzd = val[2];
	
	obj.anim = 1;
}

function setAlpha(obj, opacity, delay){	
	setTimeout(function(){
		obj.alphad = opacity;
		obj.anim = 1;
	}, delay);
}

function masterAnim(obj,delay){

	setTimeout(function(){

		obj.alphad = 1;		
		obj.txd = 0;
		obj.tyd = 0;
		obj.tzd = 0;

		obj.anim = 1;

	}, delay);

}



//fix scroll on ios
function fixedPosition(){				
	maxSize = body.offsetHeight - height;
	if( maxSize > 5 ){
				
		document.getElementById("outer").style.marginTop = window.pageYOffset+"px";
	}else{
		document.getElementById("outer").style.marginTop = "0px"
	}
	//document.body.scrollTop = document.documentElement.scrollTop = 0;
}


//=========================================================================================
//
//			Crear funciones dinamicamente segun el dispositivo
//
//=========================================================================================

// Asignar animaciones en movil o no
var mobileAnim = 1;

// Crear funcion dinamicamente en funcion del dispositivo
function setDeviceFunc(){


	if( app.mobile ){

		g = gyro.getOrientation(); 

		scene.getCamera().setTranslation(0, 0, zCam);
		scene.getCamera().lookAtElement(centerScene);

		if( mobileAnim ){

			for(i=0; i < objs.length; i++){
				objs[i].tx = 0;
				objs[i].txd = 0;
				objs[i].ty = 0;
				objs[i].tyd = 0;
				objs[i].tz = 0;
				objs[i].tzd = 0;
				objs[i].alpha = 0;
				objs[i].alphad = 0;
				objs[i].anim = 0;
			}

			app.updatingRender = function(){
				renderAnim()
			}

		}else{

			app.startApp = function(){

				// Mostramos Escenarios
				for( i=0; i < objs.length; i++ ){
					hijos = objs[i]._children;
					for( j=0; j < hijos.length; j++ ){
						hijos[j]._domElement.style.opacity  =  1;
					}
				}
				engine.startRender();
			}	

		}






	}else{
	
		// Añadimos variables tweener a los objetos, para las animaciones
		for(i=0; i < objs.length; i++){
			objs[i].tx = 0;
			objs[i].txd = 0;
			objs[i].ty = 0;
			objs[i].tyd = 0;
			objs[i].tz = 0;
			objs[i].tzd = 0;
			objs[i].alpha = 0;
			objs[i].alphad = 0;
			objs[i].anim = 0;
		}

		app.startApp = function(){

			//Descomentar si no existe ningun helper.js

			/*
			// Mostramos Escenarios

			showScene();

			// Animaciones FadeIn
			var delay = 120; 
			var incremento = 200;

			for( i=0; i < objs.length; i++ ){	
				if(i==0){ setAlpha( objs[i], 1, delay + i * incremento )}
				else{ setAlpha( objs[i], 1, delay + i * incremento ) }
			}			
			

			engine.startRender();
			*/			

		}

		app.calcCameraPos = function(){
			camX = ( px * 200/width-100)/100 * posMaxX; 
			camY = ( py * 200/height-120)/100 * posMaxY; 
		}


		app.updatingRender = function(){


			if( cursorInOut == 0){
				camX = 0;
				camY = 0;
			}
	
			//------------------------------------------------------
			// POSICION DE LA CAMARA CON EFECTO TWEENER
			//------------------------------------------------------			
			tweenX += ( camX - tweenX) * 0.05;
			tweenY += ( camY - tweenY) * 0.05;
			
			scene.getCamera().setTranslation(tweenX, tweenY, zCam);
			scene.getCamera().lookAtElement(centerScene);

			renderAnim()

		}

	}
}

//=========================================================================================
//=========================================================================================

//------------------------------------------
// Es Movil
//------------------------------------------

function isMobile(){
	return (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino|android|ipad|playbook|silk/i.test(navigator.userAgent||navigator.vendor||window.opera)||/1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test((navigator.userAgent||navigator.vendor||window.opera).substr(0,4)))
}


//------------------------------------------
// Calcular Dimensiones del escenario 
//------------------------------------------


// Default  (-1,-1, 1)
function setScale( num ){

	for(i=0; i < objs.length; i++){
		objs[i].setScale(-1*num,-1*num,1*num)
	}
}

function setSceneScale(){

	// Pendiente
	var m = (100-25)/(975-240); 

	// redimensionamos segun el menor valor entre alto y ancho de la resolucion 
	var menor = height;
	if( width < height ){ menor = width; }

	y = Math.round( m * menor + 0.5 ) / 100;
	setScale(y);
}





//================================================
//================================================
// 			Funciones LISTENERS
//================================================
//================================================


//-------------------------------------------
// onDeviceRotation
//-------------------------------------------
function mobileSetCamera(){
	app.calcCameraPos();	
}


//-------------------------------------------
// onMmouseMove
//-------------------------------------------
function setPointer(){

	px = window.event.pageX;
	py = window.event.pageY;
	
	app.calcCameraPos();
	
}

//-------------------------------------------
// onResize
//-------------------------------------------
function setResolution(){

	width 	= window.innerWidth
			|| document.documentElement.clientWidth
			|| document.body.clientWidth;
	
	height	 = window.innerHeight
			|| document.documentElement.clientHeight
			|| document.body.clientHeight;
		
	document.getElementsByClassName( "outer" )[0].style.height = height+"px";
	
	setSceneScale();
	// fix ios scroll, no esconder detras del topBar
	fixedPosition();

}
//-------------------------------------------
// onScroll
//-------------------------------------------
function setMarginScroll(){
	// fix ios scroll, no esconder detras del topBar
	fixedPosition();
}

//-------------------------------------------
// onLoad
//-------------------------------------------

function setInitConf(){


	// fix ios scroll, no esconder detras del topBar
	fixedPosition();

	// Resolucion viewport
	setResolution();
	
	// Posicion inicial del puntero en el centro
	px = width/2;
	py = height/2;

	app.mobile = isMobile();
	//app.mobile = true;

	// Configuracion de la aplicacion segun del dispositivo
	setDeviceFunc();

	// Scala del escenario segun resolucion
	setSceneScale();	

	//iniciamos aplicacion
	app.startApp();
	
}

//-------------------------------------------
// onMouseInOut
//-------------------------------------------

function cursorIn(){
	cursorInOut = 1;
}

function cursorOut(){
	cursorInOut = 0;
}



//================================================
//================================================
// 			 LISTENERS
//================================================
//================================================


document.addEventListener('mousemove', setPointer );
window.addEventListener("deviceorientation", mobileSetCamera);
window.addEventListener('resize', setResolution ) ;
window.addEventListener('load', setInitConf );
window.addEventListener("scroll", setMarginScroll );

window.addEventListener("mouseout", cursorOut);
window.addEventListener("mousemove", cursorIn);

