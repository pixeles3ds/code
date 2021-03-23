window.scalator = (function () {
	

	// CLASS
	function Scalator (data) {

		var masterClass = this;

		this.map = new Map();

		var elements = data.elements;
		var conf = data.conf;
		
		
		var getObjConf = function( element ){


			var id = element.getAttribute("id");



			var width = 1024;
			var height = 1024;


			// Si se envia la configuracion por el constructor, las dimensiones se le palicaran a todos los elementos
			if( conf ){
				if( conf.length ){
					width = conf.width;
					height = conf.height;
				}
			}

			// Si existen los atributos en el tag
			if( element.hasAttribute("scalator-width") ) width = parseInt( element.getAttribute("scalator-width") ); 
			if( element.hasAttribute("scalator-height") ) height = parseInt( element.getAttribute("scalator-height") ); 



			var conf = {
				e: element,
				id: id,
				width: width,
				height: height,
				parent: element.parentNode
			};

			return conf;
		}




		this.length = elements.length;
		this.list = [];

		for(var i = 0; i < elements.length; i++ ) {

			var element = elements[i];
			var objData = getObjConf( element );

			this.list[i] = objData;

			if( element.hasAttribute("id") ){
				masterClass.map.set( "#"+element.getAttribute("id") , i );
			} 

			 
		}		

		return this;


	}

	
	// CONSTRUCTOR
	var scalator = function () {

		var thereIsSelectors = 0;
		var data = {}

		if( arguments.length ){				

			var selector = arguments[0];
			var conf = {}


			if( arguments.length > 1){
				conf = arguments[1];
			}


			var els;

			if (typeof selector === "string") {
		    	els = document.querySelectorAll(selector);
			} else if (selector.length) {
				els = selector;
			} else {
				els = [selector];
			}

			var data = {
				"elements":els,
				"conf":conf
			}
			thereIsSelectors = 1;


		}else{

			var els = document.querySelectorAll(".scalator");
			if(els.length){
				

				var data = {
					"elements":els,
					"conf":{}
				}
				thereIsSelectors = 1;

			}
			

		}


		// Retornamos Instancia
		if( thereIsSelectors ){

			var instance = new Scalator(data);

			window.addEventListener('resize', function(){					
				instance.scale();
			});

			instance.appendHeadStyle();
			instance.scale();				

			return instance;

		}else{

			console.log("Scalator: Nothing Selected");
		}


			
		
	};



   
   Scalator.prototype.scale = function () {
   	
   		

   		for(var i = 0; i < this.list.length; i++ ) {

   			var element = this.list[i];

   			var obj = element.e;

   			var objW = element.width;   			
   			var objH = element.height;

   			var parentW = element.parent.offsetWidth;
   			var parentH = element.parent.offsetHeight;




   			var scaleW = parentW/objW;
   			var scaleH = parentH/objH;


   			var scaleFactor = scaleH;
   			if( scaleW < scaleH ) scaleFactor = scaleW;
   			   			
			obj.style.setProperty("width", objW+"px", "important");
			obj.style.setProperty("height", objH+"px", "important");
			obj.style.setProperty("transform", "translate(-50%,-50%) scale("+ scaleFactor +")", "important");

   		}
   };

   


   Scalator.prototype.appendHeadStyle = function () {

   		var styleTag = document.getElementById("scalator-plugin-style-head");
   		
   		// Si no existe el tag
   		if( !styleTag ){

			var css = '.scalator{ left: 50%; top: 50%; position: absolute !important; transform: translate(-50%,-50%); }',
			    head = document.head || document.getElementsByTagName('head')[0],
			    style = document.createElement('style');		    

			head.appendChild(style);

			style.type = 'text/css';
			if (style.styleSheet){
			  // This is required for IE8 and below.
			  style.styleSheet.cssText = css;
			} else {
			  style.appendChild(document.createTextNode(css));
			}

			// add id to style tag
			style.setAttribute("id", "scalator-plugin-style-head");

		}

	}


	Scalator.prototype.getWindowSize = function () {
		var width = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;
		var height = window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight;
		return {"w":width,"h":height}
	}
	

	return scalator;
}());



/*

scalator(); // buscara todas las clases .scalator



//	Formas de llamar y aplicar atributos

//----------------------------------------------------
//	JAVASCRIPT
//----------------------------------------------------

scalator("#obj",{width:100,height:100});

//----------------------------------------------------
//	INLINE
//----------------------------------------------------

<div class="scalator" scalator-width="100" scalator-height="100">










*/