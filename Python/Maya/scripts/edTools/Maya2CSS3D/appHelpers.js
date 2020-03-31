var body = document.body,
    html = document.documentElement;

var sombrero = document.getElementsByClassName( "sombrero1" )[0]


sombrero.onclick = function() {
	//calibrar();
};


function home(){
	alert("hola");
}

function p(data){
	var aa = document.getElementById( "test2" ).innerHTML
	document.getElementById( "test2" ).innerHTML = aa+data+ "</br>";
}

/*

	Matrices con las direcciones para limitar la rotacion en cada uno de los posibles estados

	Filas = Orientacion Inicial
	Columnas = Orientacion Actual
	
	[0,90,-90,180]

				 [Actual 0][Actual 90]
	 [inicial 0] [        ][         ]
	[inicial 90] [		  ][         ]

*/

dirX = 0;
dirY = 0;
var dirLimX =  [[ -1, -1, -1, -1 ],
				[ -1, 1, 1, -1 ],
				[ 1, -1, -1, 1 ],
				[ 1, 1, 1, 1 ]]

var dirLimY =  [[ 1, 1, 1, 1 ],
				[ -1, 1, 1, -1 ],
				[ 1, -1, -1, 1 ],
				[ -1, -1, -1, -1 ]]

var mapaMatrices = { "0":0,"90":1,"-90":2,"180":3}

// [inicial][actual]
// Asignar la direccion del bloqueo del scenario
function setDir(){ 
	dirX = dirLimX[ mapaMatrices[app.initDeviceOrient] ][ mapaMatrices[window.orientation] ];
	dirY = dirLimY[ mapaMatrices[app.initDeviceOrient] ][ mapaMatrices[window.orientation] ];
}


function setObjPos( obj, x, y, z ){
	obj.tx = obj.txd = x;
	obj.ty = obj.tyd = y;
	obj.tz = obj.tzd = z;
	obj.setTranslation(x, y, z);
}

function setInitPos(){
	
	{templateJSHelperInitPos}
	
}

function startAnimation(){
	
	{templateJSHelperAnim}

}

//-------------------------------------------
// onOrientChange
//-------------------------------------------
function calibrar(){

	setAlphaMaster();

	setDir();
	//p( g.beta + "   " + g.rawBeta);
    gyro.calibrate();
    gyro.measurements.alpha = 0;
    gyro.measurements.beta = 0;
    gyro.measurements.gamma = 0;
    g = gyro.getOrientation()    
    //p( g.beta + "   " + g.rawBeta);
	app.initOrientX = 0 ;
	app.initOrientY = 0 ;
	app.initOrientZ = 0 ;
	app.initOrientXLandL = null ;
	app.initOrientYLandL = null ;
	app.initOrientXLandR = null ;
	app.initOrientYLandR = null ;

	// Creamos quaternion con estado incial 0
	app.q = new css3d.quaternion( 0,0,0,1)
	app.qXStraight = inverseQuaternion( eulerToQuaternion(0,0,0) );
	app.qY = inverseQuaternion(eulerToQuaternion(0,0,0)) ;


	var offsetRotAlphaInitState = 0;

	if( window.orientation === 0 ){

		if( g.rawBeta > -30 && g.rawBeta < 30 && g.rawGamma > -10 && g.rawGamma < 10 ){ 
			app.alphaCal = 0;
		}else{ 
			if( g.rawGamma > -10 && g.rawGamma < 10 ){
				app.alphaCal = gyro.getAlphaCalib(0,0,0).alpha;	
			}else{
				app.alphaCal = gyro.getAlphaCalib(-89,1,1).alpha;	
			}
			
		}
	
	}else if( isOrient() == "landscape" ){

		//if( app.initDeviceOrient == 0){ offsetRotAlphaInitState = -90; }
		if( g.rawGamma > -30 && g.rawGamma < 30 && g.rawBeta > -10 && g.rawBeta < 10 ){ 

			app.alphaCal = 0;			

		}else{ 
			
			//app.alphaCal =  gyro.getAlphaCalib( 1, -90 ,1).alpha;	

			if(window.orientation == 90){ app.alphaCal = g.rawBeta }
			if(window.orientation == -90){ app.alphaCal = -g.rawBeta }	

			if( Math.abs(app.alphaCal)>90){
				if( app.alphaCal > 0){ app.alphaCal = 180 - app.alphaCal }
				else{ app.alphaCal = -(180 + app.alphaCal) }
			}
			
		}
	
	}
	

}

function setAlphaMaster(){	

	if( app.initDeviceOrient == 0 ){
		app.offsetOrientation = window.orientation;
	}else if( app.initDeviceOrient == 90 ){
		app.offsetOrientation = window.orientation - 90;
	}else if( app.initDeviceOrient == -90 ){
		app.offsetOrientation = window.orientation + 90;
	}else if( app.initDeviceOrient == 180 ){
		if( window.orientation == 0){ app.offsetOrientation = 180; }
		else if( window.orientation == 90){ app.offsetOrientation = -90; }
		else if( window.orientation == -90){ app.offsetOrientation = 90; }
		else{ app.offsetOrientation = 0; }
	}
}

// Damos medio segundo para que el usuario termine de rotar el device y asi calcular la calibracion
function iniciarCalibracion(){


	setAlphaMaster();
	setDir();

	// Ocultamos escenario mientras se gira el device  y calcula al rotacion
	//document.getElementById("container").style.visibility = "hidden";

	setTimeout(function(){
		//calibrar(); // Calibramos
		document.getElementById("container").style.visibility = "visible"; // Despues de calibrar Mostramos escenario
	},500);
}		

window.addEventListener("orientationchange", iniciarCalibracion);

function isOrient(){
	if( window.orientation === 0 || window.orientation === 180 ){ return "portrait" }
	else if( window.orientation === 90 || window.orientation === -90 ){ return "landscape" }
}



function eulerToQuaternion(beta,gamma,alpha){//Alpha around Z axis, beta around X axis and gamma around Y axis intrinsic local space in that order - like nested gimbals(each axis moves depending on how the other moves so processing order is important)

	var x = degToRad(beta) ; // beta value
	var y = degToRad(gamma) ; // gamma value
	var z = degToRad(alpha) ; // alpha value

	//precompute to save on processing time
	var cX = Math.cos( x/2 );
	var cY = Math.cos( y/2 );
	var cZ = Math.cos( z/2 );
	var sX = Math.sin( x/2 );
	var sY = Math.sin( y/2 );
	var sZ = Math.sin( z/2 );

	var w = cX * cY * cZ - sX * sY * sZ;
	var x = sX * cY * cZ - cX * sY * sZ;
	var y = cX * sY * cZ + sX * cY * sZ;
	var z = cX * cY * sZ + sX * sY * cZ;

	return makeQuat(x,y,z,w);	 //returns simple object 
}

function makeQuat(x,y,z,w){//simple utility to make quaternion object super easy to deal with

	return  {"x":x,"y":y,"z":z,"w":w};
}


function inverseQuaternion(q){
	//return makeQuat(q.x,q.y,q.z,-q.w);
	return makeQuat(q.x,q.y,q.z,-q.w);
}

function degToRad(deg){// Degree-to-Radian conversion

	 return deg * Math.PI / 180; 
}

function r(num){
	if(num){
		return Math.round(num);
	}else{
		return num;
	}
}

function f(num){
	if(num){
		return num.toFixed(2);
	}else{
		return num;
	}
}


function renderApp(){


			if( app.initOrientX == null ){ g = gyro.getOrientation() }

			if(  g.beta < 70 && g.beta > -70 && g.gamma < 70 && g.gamma > -70 ){ 
				beta = g.beta; 
				gamma = g.gamma;
				alpha = g.alpha;
			}
			
			
			

			if ( window.orientation === 0 ) {
				qt =  inverseQuaternion( eulerToQuaternion( beta,-gamma, -alpha ) );
			}else if ( window.orientation === 90) {
				qt = inverseQuaternion( eulerToQuaternion( -gamma, -beta, -alpha ) );				
			}else if ( window.orientation === -90){
				qt = inverseQuaternion( eulerToQuaternion( gamma, beta, -alpha ) );				
			}else if ( window.orientation === 180){
				qt = inverseQuaternion( eulerToQuaternion( -beta, gamma, -alpha ) );
			}
					

			app.q.x = qt.x;
			app.q.y = qt.y;
			app.q.z = qt.z;
			app.q.w = qt.w;


			
			

			if( window.orientation == 0 || window.orientation == 180 ){			ejeX = beta; ejeY = gamma;  }			
			else if( window.orientation == 90 || window.orientation == -90 ){ 	ejeX = gamma; ejeY = beta;  }


			//---------------------------------------------------------------
			// LIMITE ROTACION EJE X
			//---------------------------------------------------------------
			


			distanciaGiroX = ejeX - app.initOrientX;

			if( Math.abs(distanciaGiroX) > app.rangoRotX ){
				if( distanciaGiroX > 0 ){ 
					app.initOrientX = ejeX-app.rangoRotX;
				}
				if( distanciaGiroX < 0){ 
					app.initOrientX = ejeX+app.rangoRotX;
				}

			}
			
			// Si la orientacion incial y el actual son el mismo
			if( isOrient() == app.initOrient ){ 
				app.qXStraight = inverseQuaternion( eulerToQuaternion( app.initOrientX * dirX, 0, 0) );
			}else{ 
				app.qXStraight = inverseQuaternion( eulerToQuaternion( 0, app.initOrientX * dirX, 0) );
			}
			

			
			app.q = app.q.multiply(app.qXStraight); // X
			

			//---------------------------------------------------------------
			// LIMITE ROTACION EJE Y
			//---------------------------------------------------------------	

			// Convertimos a euler despues de rotar el sceneario 90 grados, YA NO HABRA GIMBAL LOCK Y CRAZY GAMMA

			//eu = gyro.quaternionToEuler(app.q);


			distanciaGiroY = ejeY - app.initOrientY;

			if( Math.abs(distanciaGiroY) > app.rangoRotY ){
				if( distanciaGiroY > 0 ){ 
					app.initOrientY = ejeY-app.rangoRotY;
				}
				if( distanciaGiroY < 0 ){ 
					app.initOrientY = ejeY+app.rangoRotY;
				}
				
			}

			// Si la orientacion incial y el actual son el mismo
			if( isOrient() == app.initOrient ){ 
				app.qY = inverseQuaternion( eulerToQuaternion( 0, app.initOrientY * dirY, 0) ); 											
			}else{ 
				app.qY = inverseQuaternion( eulerToQuaternion( app.initOrientY * dirY, 0, 0) );
			}

			
			app.q = app.q.multiply(app.qY); // Y
			
			

			//---------------------------------------------------------------
			// ROTACION EJE Y LANDSCAPE, PORTRAIT
			//---------------------------------------------------------------
			eu = gyro.quaternionToEuler( inverseQuaternion( app.q ) );

			// Solo rota en alpha si se ha calibrado
			qZ = inverseQuaternion(eulerToQuaternion( 0, 0, app.alphaCal + app.offsetOrientation ));
			app.q = app.q.multiply(qZ); // Z
			

			//===================================================================================
			//===================================================================================
			//
			//						 ROTACION EJE Y LANDSCAPE, PORTRAIT
			//
			//===================================================================================
			//===================================================================================
			
			// Convirtiendo el quaternio en una matriz de rotacion
			matrixRot = app.q.toMatrix4();


			// Rotamos cada objeto del escenario via matriz			
			if( g)
			for( i=0; i < objs.length; i++ ){
				objs[i].setRotationMatrix( matrixRot );
			}

/*
			test =  r(g.beta) + "   "+ r(g.gamma) + "   " + r(g.alpha) + "</br>"+
					r(beta) + "   "+ r(gamma) + "   " + r(alpha) + "</br>"+
			 		r(eu.beta) + "   "+ r(eu.gamma) + "   " + r(eu.alpha) + "</br>"+
					"X: "+ r(app.initOrientX) + "   " +r(distanciaGiroX)+ "</br>"+
					"Y: "+ r(app.initOrientY) + "   " +r(distanciaGiroY)+ "</br>"+					
					app.alphaCal+"";
					

			document.getElementById( "test" ).innerHTML = test;
			*/

}



window.addEventListener('load', function(){



	document.getElementsByClassName( "letrasP" )[0].style.backgroundImage = "none";
	document.getElementsByClassName( "letrasG" )[0].style.backgroundImage = "none";
	
	document.getElementsByClassName( "letrasG" )[0].innerHTML = "Arriba Gold";
	document.getElementsByClassName( "letrasP" )[0].innerHTML = "FINEST ECUADORIAN CHOCOLATE";


	if( isMobile() ){

		if( window.orientation == undefined ){ window.orientation = 0; } 

		app.test3 = "";

		app.rangoRotX = 20;
		app.rangoRotY = 30;	

		// Estado Incial de la rotacion en alpha 0;
		app.alphaCal = 0;

		// Capturamos la orientacion inicial del device
		app.initDeviceOrient = window.orientation;
		app.offsetOrientation = 0;
		app.initOrient = isOrient();

		app.rendered = 0;

		app.initCalibrated = 0;
	
		app.startedAnimMobile = 0;

		app.updatingRenderExtend = function(){	

			// Caundo gyro.js ya tenga los datos del gyroscopio
			if( gyro.getOrientation().beta != null ){


				// Solo calibramos la primera vez
				if( app.initCalibrated == 0){ calibrar(); app.initCalibrated = 1; }				
				// Mostramos el escenario despues de hacer los calculos de orientacion en alpha
				if( app.rendered == 0){ showScene(); app.rendered = 1; }


				// Iniciamos animacion inicial
				if( app.startedAnimMobile == 0 ){ startAnimation();	app.startedAnimMobile = 1 }


				renderApp();


				/*
				document.getElementById( "test2" ).innerHTML = 
				r(g.rawBeta) + "   "+ r(g.rawGamma) + "   " + r(g.rawAlpha) + "</br>" + 			
				"actual: "+window.orientation + "</br>" + 
				"inicial: "+app.initDeviceOrient + "</br>" + 
				"";
				*/
				

			}

		}
		if( mobileAnim ){

			app.startApp = function(){

				showScene(); // Mostramos Escenarios
				setInitPos(); // Animaciones FadeIn								
				engine.startRender();

			}
			
		}

	}else{

		/*
		test = camY + "   " + camX + "</br>";
		document.getElementById( "test" ).innerHTML = test;
		//document.getElementsByClassName( "outer" )[0].style.height = height+"px";
		*/


		app.startApp = function(){

			showScene(); // Mostramos Escenarios
			setInitPos(); // Animaciones FadeIn		
			startAnimation();			
			engine.startRender();

		}

		app.updatingRenderExtend = function(){
			/*
			for( i=0; i < objs.length; i++ ){
				//objs[i].setRotationXYZ(0,ii,0);
				//objs[i].setRotation(ii,jj)
			}
			//flor.setRotationXYZ(0,3.14,0);
			*/
		}
			
	}

	app.startApp();


} );



window.addEventListener('deviceorientation', function( event ) {
	
/*	o = event;

	test =  o.beta+ "</br>"+ o.gamma + "</br>" + o.alpha + "</br>";

	document.getElementById( "test" ).innerHTML = test;
*/
/*
	test =  "Height: "+ height + "</br></br>"+
			"pageOffsetY: "+ window.pageYOffset + "</br></br>"+

	
			"bodyScroll: "+ body.scrollHeight + "</br>"+
			"bodyOffset: "+ body.offsetHeight + "</br></br>"+

			"htmlClient: "+ html.clientHeight + "</br>"+
			"htmlScroll: "+ html.scrollHeight + "</br>"+
			"htmlOffset: "+ html.offsetHeight + "</br></br>"+

			"outer: "+ document.getElementById("outer").clientHeight + "</br>"+
			"outer: "+ document.getElementById("middle").clientHeight + "</br>"+
			"outer: "+ document.getElementById("inner").clientHeight + "</br>"+
			
			"";

	document.getElementById( "test2" ).innerHTML = test;
	
*/
}, false);


window.addEventListener('load', function(){

} );


document.addEventListener('touchstart', home, false);