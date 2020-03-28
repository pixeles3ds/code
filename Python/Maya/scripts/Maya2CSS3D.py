'''

Maya2CSS
 
For CSS3D Engine Plugin by bitWorking - http://css3d.bitworking.de/

0. Los objs deben estar en la RAIZ o agrupados por solo un grupo
1. El script exportara objetos juntos si estan agrupados, recibiran el nombre del grupo y tendran la misma textura
2. Solo exporta planos estaticos, no animaciones


How install:
    
1. Guardar en maya20xx/scripts/
2. Cargar con:
    
        
import Maya2CSS3D as m2css
m2css.createProject( )
m2css.createProject( "c:/FolderProyecto", html=1, js=1)


'''


import maya.cmds as cmds
import edTools as e

reload(e) # reload edTools module



# Nombre de los folders
folderProject = "C:/CSS3DEngine/"
modelsP = "models"
texturesP = "textures"
jsP = "js"

       

def expSelObj( name ):

    ext = ".obj"
    path = folderProject + "models/"
    opt = "groups=0;ptgroups=0;materials=0;smoothing=0;normals=0"
    
    
    cmds.file( path+name+ext, pr=1, force=1, options=opt, es=1, typ="OBJexport")
    print "Exported... "+path+name+ext






def createDict():
    
    lista = {"none":[]}
    
    # lista de transform que pertenecen a una geometria
    geos = e.getGeometries()
    
    for obj in geos:
        
        paren = e.getParents( obj )
        paren = paren[0] if paren else paren
        
        if paren is None:
            lista["none"].append(obj)
        else:
            if paren in lista:
                lista[paren].append(obj)
            else:
                lista[paren] = []
                lista[paren].append(obj)
                
    return lista



def copyFile( filename, folderDest ):

	if folderDest != "": folderDest = folderDest +"/"

	jsSrc = e.getPath()+"Maya2CSS3D/"+filename
	jsDes = folderProject+""+folderDest+""+filename
	e.copyF( jsSrc, jsDes) # Copiamos 
	print "File Copied... "+jsDes


def exportData( lista ):
    
    listGroups = e.getGroups() # Transform que sean solo grupos
   
    
    jsTemplate = '''var {varName} = css3d.elementFactory.fromObj( document.getElementById('container'), scene, objPath + '{varName}.obj', '{varName}', backfaceCullin,  false, true, texturePath + '{textureName}',{textureSize}); '''
   
    listJS = []
    
    print "-"*20
     
    for obj in lista:
        
        textureData = None
        
        # Si los transform son de grupos o shapes       
        if obj in listGroups: # Transform sin shape( Grupo)
            firstTransf = e.getChilds(obj)[0]
            textureData = e.getTexture( firstTransf )
        else:
            textureData = e.getTexture( obj )
        
        
        textureName = ""
        # Si no hay textura
        if textureData[0] == None :
            textureName = "noT.jpg"
        else:
            
            textureName = textureData[0].split("/")[-1]
            textureDest = folderProject+"textures/"+textureName
            
            try:
                e.copyF(textureData[0], textureDest) # Copiamos texturas a la carpeta del proyecto
                print "Texture Copied... " + textureDest
            except:
                print "Error al copiar "+textureName
                
            
            
        
        tmpJS = jsTemplate.format( varName = obj, textureName = textureName, textureSize = textureData[1] )
        listJS.append(tmpJS)
    
    
    print "-"*20

    #Copiamos archivo JS,html,imgError
	
    copyFile("css3d.min.js","js")
    copyFile("gyro.js","js")
    copyFile("noT.jpg","textures")
    if ghtml: copyFile("index.html","")
    
    
    print "-"*20


    # Generamos HELPER JS
    

    
    # Posicion inicial de objetos en cero
    jsTemplateHelperInitPos = '\n'    
    
    for i,obj in enumerate(lista):
        jsTemplateHelperInitPos += "\tsetObjPos( objs["+str(i)+"], 0, 0, 0 ); // " + obj + "\n"

    jsTemplateHelperInitPos += ' \n\n'
        

    # Iniciamos animaciones
    jsTemplateHelperAnim = '\n'

    for i,obj in enumerate(lista):
        jsTemplateHelperAnim += "\tmasterAnim( objs["+str(i)+"], "+ str((i+1)*100) +" ); // " + obj + "\n"


    jsTemplateHelperAnim += '\n\n' 
    
    
   
    jsHELPER = e.readFile( e.getPath()+"Maya2CSS3D/appHelpers.js" )    
    jsHELPER = jsHELPER.replace("{templateJSHelperInitPos}", jsTemplateHelperInitPos )
    jsHELPER = jsHELPER.replace("{templateJSHelperAnim}", jsTemplateHelperAnim )   

    if gjs:
        e.writeFile( folderProject + "js/appHelpers.js", jsHELPER)
        print "HELPER Saved !!! "+ folderProject + "js/appHelpers.js"



    # Generamos APP JS
    
    jsTemplateHead = '''
    
var objPath = "./{_models}/";
var texturePath = "./{_textures}/";
var backfaceCullin = false;
    
'''.format(_textures = texturesP, _models = modelsP)     

    for l in listJS:
        jsTemplateHead += l+"\n"
    
    
    jsAPP = e.readFile( e.getPath()+"Maya2CSS3D/css3dApp.js" )
    jsAPP = jsAPP.replace("{templateJSHead}", jsTemplateHead )
    
    # Reemplazamos lista de objetos en array
    strLista = str(lista).replace("u'","").replace("'","")
    jsAPP = jsAPP.replace( "var objs = []" , "var objs = "+ strLista +";")

    if gjs:
        e.writeFile( folderProject + "js/css3dApp.js", jsAPP)
        print "APP Saved !!! "+ folderProject + "js/css3dApp.js"
    
    
    
def createProject( folderPr = "", html=0, js=1):
    
    global folderProject

    global ghtml
    global gjs
    
    ghtml = html
    gjs = js
    

    if folderPr != "":
        folderProject = folderPr
        if folderProject[-1] != "/":
            folderProject += "/"
    


    e.createFolder( folderProject + modelsP )
    e.createFolder( folderProject + texturesP )
    e.createFolder( folderProject + jsP )

    lista = createDict()
    listaNameObj = []
    
    print "-"*20
        
    for key in lista:
        
        if key == "none":
            for node in lista[key]:
                name = node
                geo = node
                
                cmds.select(geo, r=1)
                expSelObj(name)
                listaNameObj.append(name)
        else:
            name = key
            geo = lista[key]

            cmds.select(geo, r=1)
            expSelObj(name)
            listaNameObj.append(name)
            
    cmds.select(cl=1)
    
    exportData( listaNameObj )
        

