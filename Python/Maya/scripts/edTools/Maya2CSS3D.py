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

m2css = Maya2CSS3D.webApp()

# m2css.createProject( )
m2css.createProject( "C:/CSS3DEngine", html=1, js=1)


'''

import maya.cmds as cmds
import edCore as ec

reload(ec) # reload edTools module


class webApp():

    def __init__(self):
        
        # Nombre de los folders
        self.folderProject = "C:/CSS3DEngine/"
        self.modelsFolder = "models"
        self.texturesFolder = "textures"
        self.jsFolder = "js"

        self.jsExport = 1;
        self.htmlExport = 1;

        self.edCoreSys = ec.system()
        self.edCoreHelp = ec.helpers()
        self.edCoreGet = ec.getters()


    def setJsFolder(self, path ):
        self.jsFolder = path

    def setModelsFolder(self, path ):
        self.modelsFolder = path

    def setTexturesFolder(self, path ):
        self.texturesFolder = path
       



    def expSelObj( self, name ):

        ext = ".obj"
        path = self.folderProject + "models/"
        opt = "groups=0;ptgroups=0;materials=0;smoothing=0;normals=0"
        
        
        cmds.file( path+name+ext, pr=1, force=1, options=opt, es=1, typ="OBJexport")
        print "Exported... "+path+name+ext






    def createDict(self):
        
        lista = {"none":[]}
        
        # lista de transform que pertenecen a una geometria
        geos = self.edCoreGet.getGeometries()
        
        for obj in geos:
            
            paren = self.edCoreGet.getParents( obj )
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



    def copyFile( self, filename, folderDest ):

        if folderDest != "": folderDest = folderDest +"/"

        jsSrc = self.edCoreGet.getPath()+"Maya2CSS3D/"+filename
        jsDes = self.folderProject+""+folderDest+""+filename
        self.edCoreSys.copyF( jsSrc, jsDes) # Copiamos 
        print "File Copied... "+jsDes


    def exportData( self, lista ):
        
        listGroups = self.edCoreGet.getGroups() # Transform que sean solo grupos
       
        
        jsTemplate = '''var {varName} = css3d.elementFactory.fromObj( document.getElementById('container'), scene, objPath + '{varName}.obj', '{varName}', backfaceCullin,  false, true, texturePath + '{textureName}',{textureSize}); '''
       
        listJS = []
        
        print "-"*20
         
        for obj in lista:
            
            textureData = None
            
            # Si los transform son de grupos o shapes       
            if obj in listGroups: # Transform sin shape( Grupo)
                firstTransf = self.edCoreGet.getChilds(obj)[0]
                textureData = self.edCoreGet.getTexture( firstTransf )
            else:
                textureData = self.edCoreGet.getTexture( obj )
            
            
            textureName = ""
            # Si no hay textura
            if textureData[0] == None :
                textureName = "noT.jpg"
            else:
                
                textureName = textureData[0].split("/")[-1]
                textureDest = self.folderProject+"textures/"+textureName
                
                try:
                    self.edCoreSys.copyF(textureData[0], textureDest) # Copiamos texturas a la carpeta del proyecto
                    print "Texture Copied... " + textureDest
                except:
                    print "Error al copiar "+textureName
                    
                
                
            
            tmpJS = jsTemplate.format( varName = obj, textureName = textureName, textureSize = textureData[1] )
            listJS.append(tmpJS)
        
        
        print "-"*20

        #Copiamos archivo JS,html,imgError
        
        self.copyFile("css3d.min.js","js")
        self.copyFile("gyro.js","js")
        self.copyFile("noT.jpg","textures")
        if self.htmlExport:
            self.copyFile("index.html","")
        

        
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
        
        
       
        jsHELPER = self.edCoreSys.readFile( self.edCoreGet.getPath()+"Maya2CSS3D/appHelpers.js" )    
        jsHELPER = jsHELPER.replace("{templateJSHelperInitPos}", jsTemplateHelperInitPos )
        jsHELPER = jsHELPER.replace("{templateJSHelperAnim}", jsTemplateHelperAnim )   

        if self.jsExport:
            self.edCoreSys.writeFile( self.folderProject + "js/appHelpers.js", jsHELPER)
            print "HELPER Saved !!! "+ self.folderProject + "js/appHelpers.js"



        # Generamos APP JS
        
        jsTemplateHead = '''
        
    var objPath = "./{_models}/";
    var texturePath = "./{_textures}/";
    var backfaceCullin = false;
        
    '''.format(_textures = self.texturesFolder, _models = self.modelsFolder)     

        for l in listJS:
            jsTemplateHead += l+"\n"
        
        
        jsAPP = self.edCoreSys.readFile( self.edCoreGet.getPath()+"Maya2CSS3D/css3dApp.js" )
        jsAPP = jsAPP.replace("{templateJSHead}", jsTemplateHead )
        
        # Reemplazamos lista de objetos en array
        strLista = str(lista).replace("u'","").replace("'","")
        jsAPP = jsAPP.replace( "var objs = []" , "var objs = "+ strLista +";")

        if self.jsExport:
            self.edCoreSys.writeFile( self.folderProject + "js/css3dApp.js", jsAPP)
            print "APP Saved !!! "+ self.folderProject + "js/css3dApp.js"
        
        
        
    def createProject( self, folderPr = "C:/CSS3DEngine/", html=0, js=1):

        # Setting vars
        
        self.folderProject = folderPr
        self.htmlExport = html
        self.jsExport = js

        if self.folderProject[-1] != "/":
            self.folderProject += "/"


        self.edCoreSys.createFolder( self.folderProject + self.modelsFolder )
        self.edCoreSys.createFolder( self.folderProject + self.texturesFolder )
        self.edCoreSys.createFolder( self.folderProject + self.jsFolder )

        lista = self.createDict()
        listaNameObj = []
        
        print "-"*20
            
        for key in lista:
            
            if key == "none":
                for node in lista[key]:
                    name = node
                    geo = node
                    
                    cmds.select(geo, r=1)
                    self.expSelObj(name)
                    listaNameObj.append(name)
            else:
                name = key
                geo = lista[key]

                cmds.select(geo, r=1)
                self.expSelObj(name)
                listaNameObj.append(name)
                
        cmds.select(cl=1)
        
        self.exportData( listaNameObj )
            

