'''

Maya2CSS
 
For CSS3D Engine Plugin by bitWorking - http://css3d.bitworking.de/

0. Los objs deben estar en la RAIZ o agrupados por solo un grupo
1. El script exportara objetos juntos si estan agrupados, recibiran el nombre del grupo y tendran la misma textura
2. Solo exporta planos estaticos, no animaciones


How install:
    
1. Guardar en maya20xx/prefs/scripts/
2. Cargar con:
            
import edTools.Maya2CSS3D as Maya2CSS3D
reload( Maya2CSS3D )


# Maya2CSS3D.createProject( )
Maya2CSS3D.createProject( "C:/CSS3DEngine", html=1, js=1)


'''

import maya.cmds as cmds
import edCore

reload(edCore) # reload edTools module



    
# Nombre de los folders
folderProject = "C:/CSS3DEngine/"
modelsFolder = "models"
texturesFolder = "textures"
jsFolder = "js"

jsExport = 1;
htmlExport = 1;



def setJsFolder( path ):
    jsFolder = path

def setModelsFolder( path ):
    modelsFolder = path

def setTexturesFolder( path ):
    texturesFolder = path
   



def expSelObj(  name ):

    ext = ".obj"
    path = folderProject + "models/"
    opt = "groups=0;ptgroups=0;materials=0;smoothing=0;normals=0"
    
    
    cmds.file( path+name+ext, pr=1, force=1, options=opt, es=1, typ="OBJexport")
    print "Exported... "+path+name+ext






def createDict():
    
    lista = {"none":[]}
    
    # lista de transform que pertenecen a una geometria
    geos = edCore.getters.getGeometries()
    
    for obj in geos:
        
        paren = edCore.getters.getParents( obj )
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



def copyFile(  filename, folderDest ):

    if folderDest != "": folderDest = folderDest +"/"

    jsSrc = edCore.getters.getPath()+"Maya2CSS3D/"+filename
    jsDes = folderProject+""+folderDest+""+filename
    edCore.system.copyF( jsSrc, jsDes) # Copiamos 
    print "File Copied... "+jsDes


def exportData(  lista ):

    print("----",htmlExport)
    print("----",jsExport)
    
    listGroups = edCore.getters.getGroups() # Transform que sean solo grupos
   
    
    jsTemplate = '''var {varName} = css3d.elementFactory.fromObj( document.getElementById('container'), scene, objPath + '{varName}.obj', '{varName}', backfaceCullin,  false, true, texturePath + '{textureName}',{textureSize}); '''
   
    listJS = []
    
    print "-"*20
     
    for obj in lista:
        
        textureData = None
        
        # Si los transform son de grupos o shapes       
        if obj in listGroups: # Transform sin shape( Grupo)
            firstTransf = edCore.getters.getChilds(obj)[0]
            textureData = edCore.getters.getTexture( firstTransf )
        else:
            textureData = edCore.getters.getTexture( obj )
        
        
        textureName = ""
        # Si no hay textura
        if textureData[0] == None :
            textureName = "noT.jpg"
        else:
            
            textureName = textureData[0].split("/")[-1]
            textureDest = folderProject+"textures/"+textureName
            
            try:
                edCore.system.copyF(textureData[0], textureDest) # Copiamos texturas a la carpeta del proyecto
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

    if htmlExport:
        copyFile("index.html","")
    

    
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
    
    
   
    jsHELPER = edCore.system.readFile( edCore.getters.getPath()+"Maya2CSS3D/appHelpers.js" )    
    jsHELPER = jsHELPER.replace("{templateJSHelperInitPos}", jsTemplateHelperInitPos )
    jsHELPER = jsHELPER.replace("{templateJSHelperAnim}", jsTemplateHelperAnim )   

    if jsExport:
        edCore.system.writeFile( folderProject + "js/appHelpers.js", jsHELPER)
        print "HELPER Saved !!! "+ folderProject + "js/appHelpers.js"



    # Generamos APP JS
    
    jsTemplateHead = '''
    
var objPath = "./{_models}/";
var texturePath = "./{_textures}/";
var backfaceCullin = false;
    
'''.format(_textures = texturesFolder, _models = modelsFolder)     

    for l in listJS:
        jsTemplateHead += l+"\n"
    
    
    jsAPP = edCore.system.readFile( edCore.getters.getPath()+"Maya2CSS3D/css3dApp.js" )
    jsAPP = jsAPP.replace("{templateJSHead}", jsTemplateHead )
    
    # Reemplazamos lista de objetos en array
    strLista = str(lista).replace("u'","").replace("'","")
    jsAPP = jsAPP.replace( "var objs = []" , "var objs = "+ strLista +";")

    if jsExport:
        edCore.system.writeFile( folderProject + "js/css3dApp.js", jsAPP)
        print "APP Saved !!! "+ folderProject + "js/css3dApp.js"
    
    





#----------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------



def createProject(  folderPr = "C:/CSS3DEngine/", html=0, js=1):

    
    # Setting vars    

    global folderProject, htmlExport, jsExport
    
    folderProject = folderPr
    htmlExport = html
    jsExport = js   

    if folderProject[-1] != "/":
        folderProject += "/"


    edCore.system.createFolder( folderProject + modelsFolder )
    edCore.system.createFolder( folderProject + texturesFolder )
    edCore.system.createFolder( folderProject + jsFolder )

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
        

