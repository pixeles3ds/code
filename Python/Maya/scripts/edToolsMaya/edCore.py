import maya.cmds as cmds
import maya.mel as mel
from shutil import copyfile
import os
import sys





# Run Python as GLOBAL Scope
def runPython( script):
    return mel.eval( 'python( "{0}" ); '.format( script ) )

    # Get the value of a Global MEL variable
def getMel( name ):
    return mel.eval("$res = ${nameVar};".format( nameVar = name ) )

# Confirm dialog
def confirm( msg):
    msg = "\n" + msg + "\n"
    return cmds.confirmDialog( title='Confirm', message=msg, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No' ).encode('utf-8')

# Alert dialog
def alert( msg ):
    cmds.confirmDialog( title='EdTools', message='\n   %s     \n' % msg  )

# Fancy Alert MSG
def alert2( msg ):
    cmds.inViewMessage( amg='<hl>'+msg+'</hl>', pos='midCenter', textOffset=50, fit=200, fot=300, fadeStayTime=800, textAlpha=1, fade=True )


def showWarning( msg ):
    cmds.warning( msg )

def showError( msg ):
    cmds.error( msg )


#=====================================================================================================
#
#           MAYA CONFIGURATION & PREFERENCES
#
#=====================================================================================================

class maya():
    

    @classmethod
    def setVarInt( self, var, val):
        cmds.optionVar( intValue = ( var , val ) )
    
    @classmethod
    def setVarStr( self, var, val):
        cmds.optionVar( stringValue = ( var , val ) )
    
    @classmethod
    def setVarConf( self, var, val ):
        self.setVarInt( var , val )
        cmds.file( uc = val )
        mel.eval( "$g" + var[:1].upper() + var[1:] + " = " + str( val ) )                



    #----------------------------------------------------------------------------------------------------------------------

    @classmethod
    def saveLayout(self):
        cmds.workspaceLayoutManager( save = True )





    #----------------------------------------------------------------------------------------------------------------------
    #       Maya Init Preferences
    #----------------------------------------------------------------------------------------------------------------------
    # Set maya preferences only once, it means those don't need to be loaded everytime at Maya starting
    @classmethod
    def setInitOncePreferences(self,*args):

        
        # This is a special method just for disable autosave workspaces
        def disableWorkSpaceAutoSave():
            mel.eval( "source workspaceHelperProcs.mel" )   
            mel.eval( "updateWorkspaceAutoSave( 0 );" )   
            workspaceFile = cmds.workspaceLayoutManager( q=True, current=True ).replace(" ","_")+".json"
            workspacesPath = cmds.internalVar( userPrefDir = True ) + "workspaces/"
            workspacesFilePath = workspacesPath + workspaceFile

            # If it is the first time, create a workspace,json file
            if not system.fileExist( workspacesFilePath ):                
                runPython("edTools.ui.deleteUI()")
                cmds.workspaceLayoutManager( save = True )
                runPython("edTools.ui.showUI()")   
                cmds.tabLayout("edToolsTabs", edit=True, selectTab="edFixLayout")

            system.replaceInFile( workspacesFilePath, '"autoSave": true,', '"autoSave": false,')





        #-----------------------------------------------------    
        #     [ ] optionbOxes on main window menus
        #-----------------------------------------------------
        

        # Create -> Polygon/nurbs Primitives -> interactive Creations ([ ])
        self.setVarInt( "createPolyPrimitiveAsTool" , 1 )   # Drag when creates a polygon
        self.setVarInt( "createNurbsPrimitiveAsTool" , 1 )   # Drag when creates a Nurb

        # renderView -> Autoresize ([ ])
        self.setVarInt( "renderViewAutoResize" , 0 )   # Disable auto resize on renderview



        # Windows -> Workplaces -> Maya Classics ([ ])        
        disableWorkSpaceAutoSave() # Automatically save layout changes
        

        #-----------------------------------------------------    
        #     Windows -> Setting/Preferences -> Preferences
        #-----------------------------------------------------

        # [ Interface ]
        #cmds.windowPref( enableAll = True)            # LEAVE IT TRUE, Remember size and position of windows panels
        cmds.mayaDpiSetting( mode=1, scaleValue=1.25 ) # Use custom scaling

        #[ Interface ][ UI Elements ]
        #self.setVarConf( "useSaveScenePanelConfig", 0 )    # Save panel layout with file
        #self.setVarConf( "useScenePanelConfig", 0 )        # Restore panel layout with file
        #self.setVarInt( "ResetModelViewsOnNewScene", 0 )   # Reset viewport panel settings 
        
        
        #[ Rendering ]
        self.setVarInt( "renderSetupEnable" , 0 ) # Prefered render setup system, 1 is newOne, 0 is the legacy one







    #----------------------------------------------------------------------------------------------------------------------
    #       Maya Set AutoLoad Plugin
    #----------------------------------------------------------------------------------------------------------------------
    # Load Maya preferences, for run at Maya starting
    @classmethod
    def setAutoloadEdTools(self, enabled ):


        userSetupPath = getters.getMayaFolder() + "scripts/userSetup.mel"

        code = [
        'evalDeferred("python(\\"import edToolsMaya.edTools as edTools;edTools.ui.showUI()\\")" );'
        ]
        
        #If userSetup.py does not exist, create userSetup.py and add the code
        if not system.fileExist( userSetupPath ) and enabled:

            result=""
            for line in code:
                result += line + "\n"

            result = system.clearEmptyLines( result ) #Cleaning empty newlines
            system.writeFile( userSetupPath , result ) #Save the file

        elif system.fileExist( userSetupPath ):

            oldData = system.readFile( userSetupPath )

            # Deleting the lines first
            for line in code:
                oldData = oldData.replace( line, "" ) 
            
            # If AutoLoad is enabled, add code 
            if( enabled ):
                for line in code:
                    oldData += line + "\n"

            oldData = system.clearEmptyLines( oldData ) #Cleaning empty newlines
            system.writeFile( userSetupPath , oldData ) #Save the file

    


#=====================================================================================================
#
#           SCRIPTJOBS
#
#=====================================================================================================


class scriptJobs:
    

    # List of callbacks:
    #
    #   edCallbackWorkflow -> SceneOpened, SelectionChanged
    #   edCallbackShading  -> Shading Attribute Connections change


    # Start the jobs when maya is starting with edTools
    @classmethod    
    def installJobsAtStarting(self):

        # Run this code Once, only when the edTools module is loaded at first time
        if not self.areScriptsRunning("edCallbackWorkflow"):
            self.scriptOnOpenScene() # Apply Preferences at First opens of Maya
            self.createScriptJobs( "edCallbackWorkflow" ) # Creating the jobs       

    #----------------------------------------------------------------------------
    #----------------------------------------------------------------------------



    # Way to know if there are scripts runninng, it could create the global variable for control the tasks
    @classmethod    
    def areScriptsRunning(self, nameCallback):
        res = runPython("'{0}' in globals()".format( nameCallback ))
        if res: return True
        else: return False



    # Kill the scriptJobs
    @classmethod    
    def killScriptJob(self, nameCallback ):
        # If there are jobs already created
        if self.areScriptsRunning( nameCallback ):
            idList = runPython( nameCallback )            
            for id in idList:
                cmds.scriptJob( kill=id, force=True)
            # Deleting Variable  callback
            runPython("del {0}".format( nameCallback ))        

    # Crea los scriptJobs
    @classmethod
    def createScriptJobs(self, nameCallback, opt = None ):        

        if nameCallback == "edCallbackWorkflow":

            # If not exist any scriptJob, create it.
            if not self.areScriptsRunning( nameCallback ):
                jobsList = []
                jobsList.append(  cmds.scriptJob( event = [ "SceneOpened","edTools.edCore.scriptJobs.scriptOnOpenScene()" ], protected=True )  )
                jobsList.append(  cmds.scriptJob( event = [ "SelectionChanged","edTools.edCore.scriptJobs.scriptOnSelectionChange()" ], protected=True)  )
                if jobsList:
                    runPython( "{0} = {1}".format( nameCallback, str( jobsList ) ) )

        
        # DEPRECATED NOT USED YET !!!
        elif nameCallback == "edCallbackShading":

            # If not exist any scriptJob, create it.
            if not self.areScriptsRunning( nameCallback ):
                jobsList = []
                node, attrList = opt
                for attr in attrList:
                    jobsList.append(   cmds.scriptJob( connectionChange = [ node + '.' + attr, "edTools.edCore.scriptJobs.scriptOnShadingConnectionsChange('{0}')".format( node + '.' + attr ) ], protected=True ) )

                if jobsList:
                    runPython( "{0} = {1}".format( nameCallback, str( jobsList ) ) )



    #----------------------------------------------------------------------------
    #
    #          ScriptJobs Functions
    #
    #----------------------------------------------------------------------------


    @classmethod
    def scriptOnOpenScene(self):
        print("Scene Opened", "------------------------------------------")

        #-------------------------------------
        # Active wire on shade        
        for i in range(4): mel.eval("setWireframeOnShadedOption true modelPanel"+str(i+1) );

        #-------------------------------------
        # Reset edTools Shading form if there is a shader still selected
        if edToolsShadingSelectedAI:
            runPython("import edToolsMaya.edToolsGuiFunc as edToolsGuiFunc;reload(edToolsGuiFunc);edToolsGuiFunc.uiFunc.setShadingForm('reset');")





    @classmethod        
    def scriptOnSelectionChange(self):        
        sel = cmds.ls( selection = True )
        # if something is selected
        if sel:                     
            helpers.showObjInAE()


    @classmethod        
    def scriptOnShadingConnectionsChange(self, attrChanged ):
        print( attrChanged + "Changed", "---------------------")







#=====================================================================================================
#
#           MAYA SHORTCUTS
#
#=====================================================================================================


class hotkeys:
      

    # Install maya shorcuts preferences
    @classmethod
    def installHotKeys(self,*args):
        
        # Create the keyset map file of the keys and commands if not exist        
        if not cmds.hotkeySet( "edToolsHotKeySet", q=True, exists=True ):
            cmds.hotkeySet( "edToolsHotKeySet", current=True )
        
        

        #----------------------------------
        #   Pivots
        #----------------------------------
        cmds.nameCommand( 'edCenterAllPivots', annotation='Center All Pivots', sourceType="python", command=' python("edTools.hotkeys.pivot2center()") ')
        cmds.nameCommand( 'edPivot2Obj', annotation='Move Pivot to Obj', sourceType="python", command=' python("edTools.hotkeys.pivot2Obj()") ')

        #----------------------------------
        #   Manip Context
        #----------------------------------
        cmds.nameCommand( 'edContextToSelfObject', annotation='Context Obj Itself', command='manipMoveContext -e -mode 0 Move;')
        cmds.nameCommand( 'edContextToWorld', annotation='Context World', command='manipMoveContext -e -mode 2 Move;')
        cmds.nameCommand( 'edContextToCustom', annotation='Context Custom', command='manipMoveContext -e -mode 6 Move;')
        cmds.nameCommand( 'edContextToSelfComponent', annotation='Context to Self Components', command='manipMoveContext -e -mode 10 Move;')
        cmds.nameCommand( 'edContextToObjComponent', annotation='Context to Component Other Obj', command='manipMoveOrient 4;')
        cmds.nameCommand( 'edContextToObj', annotation='Context to oter Obj', sourceType="python", command=' python("edTools.hotkeys.contextObj2Obj()") ')

        #----------------------------------
        #   General WorkFLow
        #----------------------------------
        cmds.nameCommand( 'edShowNormals', annotation='Show Normals of Objects', command='setPolygonDisplaySettings("fNormal");')


        #-----------------------------------------------------------------------        
        #-----------------------------------------------------------------------
                
        cmds.hotkey( k='c', name='edCenterAllPivots' )        
        cmds.hotkey( k='c', alt=True, name='edPivot2Obj' )

        cmds.hotkey( k='q', alt=True, name='edContextToSelfObject' )
        cmds.hotkey( k='w', alt=True, name='edContextToWorld' )
        cmds.hotkey( k='e', alt=True, name='edContextToCustom' )
        cmds.hotkey( k='r', alt=True, name='edContextToSelfComponent' )
        cmds.hotkey( k='d', alt=True, name='edContextToObjComponent' )
        cmds.hotkey( k='f', alt=True, name='edContextToObj' )

        cmds.hotkey( k='n', name='edShowNormals' )



        #Saving hotKeys Preferences
        cmds.savePrefs( hotkeys=True )
        

    
    # Funcion Que muestra el objeto actual en AE
    @classmethod
    def showObjInAE(self):        
        helpers.showObjInAE()


    # Media de N cantidad de objs   
    @classmethod
    def centro(self, list):

        res = [0,0,0]
        
        for item in list:
            
            tmpCord = cmds.xform( item, q=1,ws=1,rp=1)

            res[0] += tmpCord[0]
            res[1] += tmpCord[1]
            res[2] += tmpCord[2]

        res[0] = res[0]/len(list)
        res[1] = res[1]/len(list)
        res[2] = res[2]/len(list)
            
            
        return  res

    # Orientar axis hacia otro objeto
    @classmethod
    def contextObj2Obj(self):
          
        def aling(sel,cord):
            cmds.CreateLocator()
            loc = cmds.ls(sl=True)[0] 
            cmds.move( cord[0], cord[1], cord[2], loc, absolute = True )
            mel.eval( 'manipMoveAlignHandleToComponent("'+loc+'", {"'+ sel[0] +'"}, {""}, "none", 0);')
            cmds.delete( loc )
            
        sel = cmds.ls(sl=True)
        
        if sel:            
            tmpCord = [0,0,0]
            if len(sel) < 2:
                showWarning("Must select more objects to point")
                return False
            elif len(sel) == 2:
                tmpCord = cmds.xform(sel[1],q=1,ws=1,rp=1)    
            elif len(sel)>2:
                tmpCord = self.centro( sel[1:] )
            
            aling( sel, tmpCord )

    # Mover pivot hacia centro
    @classmethod
    def pivot2center(self):
        mel.eval(" xform -cpc; ")

    # Mover pivot hacia otro objeto
    @classmethod
    def pivot2Obj(self):
                
        selObj = cmds.ls(sl=True,type="transform")
        
        if selObj:
            shape = selObj[0]
            if len(selObj) == 1:              
              cmds.select(shape)
              mel.eval(" xform -cpc; ")  
            if len(selObj)>1:
                point = self.centro( selObj[1:] )            
                cmds.move(point[0], point[1], point[2], shape+".scalePivot", shape+".rotatePivot", absolute=True)            
                cmds.select(shape)
            else:
                showWarning("Must select at least 2 objects")




#=====================================================================================================
#
#           SYSTEM
#
#=====================================================================================================

class system():
    

    # Create a fileDialog to pick a folder and return the path
    @classmethod
    def folderPicker(self, path="C:/"):    
        return cmds.fileDialog2( dialogStyle=1, fileMode=3, dir=path )

    
    @classmethod
    def fileExist( self, path  ):
        return os.path.exists( path )

    @classmethod
    def createFolder( self, name ):
        if not os.path.exists( name ):
            os.makedirs( name )

    @classmethod
    def copyF( self, src, dst ):
        copyfile(src, dst)    
    
    @classmethod
    def readFile( self, path ):
        f = open( path,"r") 
        data = f.read()
        f.close()
        return data

    @classmethod
    def writeFile( self, pathName, data ):
        f = open( pathName, "w") 
        f.write( data ) 
        f.close() 

    @classmethod
    def clearEmptyLines( self, data ):
        lines = data.split("\n")
        non_empty_lines = [line for line in lines if line.strip() != ""]
        
        result = ""
        for line in non_empty_lines:
                  result += line + "\n"
                  
        return result

    @classmethod
    def replaceInFile( self, pathFile, dataOld, dataNew ):
        fileOld = self.readFile( pathFile )
        fileNew = fileOld.replace( dataOld, dataNew )
        self.writeFile( pathFile, fileNew )

    # Stop ejecucution
    @classmethod
    def stop( self ):
        sys.exit("Stoping")







#=====================================================================================================
#
#           GETTERS
#
#=====================================================================================================

class getters():

    @classmethod    
    def getEvents(self, filter = "" ):
        for item in cmds.scriptJob( listEvents=True ):
            if filter in item.lower():
                print(item)

    @classmethod    
    def getOptionVars(self, filter = "" ):
        for item in cmds.optionVar( list=True ):
            if filter in item.lower():
                print(item)


    #-----------------------------------------------------------------

    @classmethod
    def sel(self):
        return cmds.ls( selection = True )      

    @classmethod
    def getMayaFolder(self):
        return cmds.internalVar( userAppDir = True )
    
    @classmethod
    def getModuleMel( self, name ):
        return mel.eval('whatIs ' + name )

    #-----------------------------------------------------------------

    @classmethod
    def getNodeConnected(self, attr, onlynode = False, type = "src" ):
        if helpers.attrExist(attr):
            if type == "src":
                res = cmds.listConnections( attr, source=True, destination=False, plugs=True )
            elif type == "dst": 
                res = cmds.listConnections( attr, destination=True, source=False, plugs=True )            

            if res:
                if onlynode:
                    node,attr = helpers.separateNodeAttr( res[0].encode('utf-8') )
                    return node
                else:
                    return res[0].encode('utf-8')
            else:
                return False



    @classmethod
    def getNameNode(self):
        pass

    @classmethod
    def getAllAttr(self,name):
        return cmds.attributeInfo( name, all=True, s=True )

    # return all the shapes from a material selected
    @classmethod
    def getShapesByMaterial( self, material ):
        SG = cmds.listConnections( material, type='shadingEngine')
        if SG:
            SG = SG[0]        
            SGConnections = cmds.listConnections( SG, shapes = True )
            shapes = cmds.ls( SGConnections, shapes = 1 )
            return shapes
        else:
            return False


    # return shape of a transform node, full = "transfor|shape"
    @classmethod
    def getShape( self, nodo, full = 0 ):
        res = cmds.listRelatives( nodo , shapes = True)
        if res:
            name = nodo+"|"+res[0] if full else res[0]
            return name
        else:
            return False
            
            
    # return type of a node
    @classmethod
    def getType( self, node ):

        if node:
            node = helpers.separateNodeAttr( node )[0]
            return cmds.objectType( node ).encode('utf-8')
        else:
            return False

    #get the material of any posible node conected to a material
    @classmethod
    def getMaterial( self, node ):
        shadingGrps = self.getShadingGroup(node)
        if shadingGrps:
            material = cmds.ls(cmds.listConnections(shadingGrps),materials=1)
            if material:
                return material[0].encode('utf-8')
            else:
                return False
        else:
            return False

    #get the shadingGroup
    @classmethod
    def getShadingGroup( self, node ):
        nodeType = self.getType( node )
        if "transform" in nodeType:
            shape = self.getShape( node )        
            if shape:
                SG = cmds.listConnections( shape, type='shadingEngine')
                if SG:
                    return SG[0].encode('utf-8')                
        else:
            SG = cmds.listConnections( node, type='shadingEngine')
            if SG:
                return SG[0].encode('utf-8')
        return False
        
        
        
    # return all childs 
    @classmethod
    def getChilds( self,nodo ):
        return cmds.listRelatives( nodo )


    # return parents of a node
    @classmethod
    def getParents( self,nodo ):
        return cmds.listRelatives( nodo , parent = True)

    # return all objects, tipo = all objects of a type
    @classmethod
    def getObjs( self,tipo = "" ):   
        if tipo == "": return cmds.ls()
        else: return cmds.ls( type=[ tipo ])

    # return the transform of all original shapes (geometry), without surfaceShape mesh nodes
    @classmethod
    def getGeometries(self):
        list = []
        for tr in self.getObjs("transform"):
              
            child = self.getShape(tr,full=1)
            if child:
              tipo = self.getType(child)
              if tipo == "mesh":
               list.append(tr)
        return list


    # return all groups nodes, (transform) without shapes
    @classmethod
    def getGroups(self):
        
        groups = []
        
        transforms = cmds.ls( type=[ "transform" ])
        
        for obj in transforms:
            parents = cmds.listRelatives( obj , parent = True)
            childrens = cmds.listRelatives( obj , shapes = True)
            if( parents is None and  childrens is None):
               groups.append(obj)
        
        return groups

    # Get Path of current File python
    @classmethod
    def getPath( self, ):
        return os.path.dirname(os.path.realpath(__file__))+"/"

    # Get texture system path from transform node
    @classmethod
    def getTexture( self, node ):    
        shape = self.getShape( node )
        if shape:
            shadingGrps = cmds.listConnections( shape, type='shadingEngine')
            material = cmds.ls(cmds.listConnections(shadingGrps),materials=1) 
            fileNode = cmds.listConnections( material, type='file')
            if fileNode:
                textureFile = cmds.getAttr(fileNode[0]+".fileTextureName")
                xRes = int(cmds.getAttr( fileNode[0]+'.outSizeX') )
                yRes = int(cmds.getAttr( fileNode[0]+'.outSizeY') )
            else:
                textureFile = None
                xRes = 5
                yRes = 5
                
            return ( textureFile, xRes, yRes)



    


#=====================================================================================================
#
#           HELPERS
#
#=====================================================================================================

edToolsShadingSelectedAI = None
edToolsShadingShapes = None
edToolsShadingNormalNode = None
edToolsShadingBumpNode = None
edToolsShadingAONode = None

class helpers():

    

    edToolsShadingAttrTemplate = [
    ("color","float3",0,0,0,0),
    ("metalness","float",1,1,0,0),
    ("colorSpec","float3",0,0,0,0),
    ("roughness","float",1,1,0,0),
    ("disp","float",1,1,0,0),
    ("normal","float3",1,0,0,0),
    ("bump","float",1,1,0,0),
    ("ao","float3",0,0,0,0)
    ]


    @classmethod
    def getEdToolsShadingAttrTemplate(self):
        return self.edToolsShadingAttrTemplate

    #============================================================
    #     Attributes
    #============================================================


    @classmethod
    def separateNodeAttr( self, node ):    
        if node:
            if "." in node:
                return node.split(".")
            else:
                return [node]
        else:
            return False

    @classmethod
    def attrExist( self, nodeAttr ):    
        l = nodeAttr.split(".")
        attr =  l[-1:][0]
        node = ".".join( l[:-1] )
        return cmds.attributeQuery( attr, node = node, exists = True )
    
    @classmethod
    def setAttr( self, node, attr = "", val = 0 ):   
        if attr == "": node, attr = node.split(".") # Fixing input data    
        if self.attrExist(node+"."+attr): cmds.setAttr( node+'.'+attr, val )
        else: print(node+"."+attr+" does not exist")

    @classmethod
    def getAttr( self, node, attr = "" ):    
        if attr == "": node, attr = node.split(".") # Fixing input data    
        return cmds.getAttr( node+'.'+attr)

    @classmethod
    def connectAttr( self, nodeSrc, nodeDset ):        
        if self.attrExist(nodeSrc) and self.attrExist(nodeDset ):
            existTexture = getters.getNodeConnected(nodeDset)
            if existTexture:
                cmds.disconnectAttr( existTexture, nodeDset )
            cmds.connectAttr( nodeSrc, nodeDset )
        else:
            print("Nodes can not be connected")


    @classmethod
    def disconnectAttr( self, attr ):        
        if self.attrExist( attr ):
            nodeConnected = getters.getNodeConnected( attr )
            if nodeConnected:
                cmds.disconnectAttr( nodeConnected, attr )



    @classmethod
    def createEdAttrsDebugSahder( self, node ):
        list = self.edToolsShadingAttrTemplate
        for data in list:    
            attr = data[0]
            type = data[1]
            if type == "float3":
                cmds.addAttr( node, longName = attr, usedAsColor=True, attributeType='float3' )
                cmds.addAttr( node, longName=attr+'R', attributeType='float', parent=attr )
                cmds.addAttr( node, longName=attr+'G', attributeType='float', parent=attr )
                cmds.addAttr( node, longName=attr+'B', attributeType='float', parent=attr )
            elif type == "float":
                cmds.addAttr( node, longName=attr, attributeType='float' )
            
            
            


    #============================================================
    #     Node edTools
    #============================================================


    # Create an empty node to store attribute for debug shading purpose
    @classmethod
    def deleteNode( self, node ):
        if cmds.objExists( node ):
            cmds.delete( node )

    # Create an empty node to store attribute for debug shading purpose
    @classmethod
    def createEdDebugSahder( self, replace = False, reconnect = False):
        if not cmds.objExists('edTools'):
            cmds.createNode( 'unknown', name = "edTools" )
            self.createEdAttrsDebugSahder("edTools")
            if reconnect:
                # Reconnect inputs form with dummy shader
                listTemplate = self.getEdToolsShadingAttrTemplate()
                for data in listTemplate:    
                    connectionDest = "edTools." + data[0]                  
                    cmds.attrNavigationControlGrp( "ed"+data[0].capitalize()+"Texture", edit = True, attribute = connectionDest )
        else:
            #Delete  connections 
            listAttr = helpers.edToolsShadingAttrTemplate
            for data in listAttr:
                helpers.disconnectAttr( "edTools."+data[0] )










    # ==========================================================================================================================================
    # ==========================================================================================================================================
    #
    #       SHADING TOOL
    #
    # ==========================================================================================================================================
    # ==========================================================================================================================================


    @classmethod
    def setEdToolsShading( self, type = "" ):


        shader = edToolsShadingSelectedAI
        dummy = "edTools"


        # ===================================================================
        #
        #       FORMS AND NODES UPDATE 
        #
        # ===================================================================

        def setFormToTexturePref( fileNode, shadingType ):
            
            if "." in fileNode:
                fileNode = fileNode.split(".")[0]

            if getters.getType( fileNode ) == "file":
                result = []            
                result.append( cmds.checkBox( "ed"+shadingType.capitalize()+"Raw", query=True, value=True ) )
                result.append( cmds.checkBox( "ed"+shadingType.capitalize()+"Alpha", query=True, value=True ) )
                result.append( cmds.checkBox( "ed"+shadingType.capitalize()+"Filter", query=True, value=True ) )
                result.append( cmds.checkBox( "ed"+shadingType.capitalize()+"Bias", query=True, value=True ) )
                
                preferences = result                
                if getters.getType( fileNode ) == "file":

                    raw = "Raw" if preferences[0] else "sRGB"            
                    alpha = preferences[1]
                    filt = 0 if preferences[2] else 3
                    bias = -10 if preferences[3] else 0

                    cmds.setAttr( fileNode+".colorSpace", raw, type='string' )
                    cmds.setAttr( fileNode+".alphaIsLuminance", alpha )
                    cmds.setAttr( fileNode+".aiFilter", filt )
                    cmds.setAttr( fileNode+".aiMipBias", bias )


        def getTextureToFormPref( fileNode, shadingType ):
            
            if "." in fileNode:
                fileNode = fileNode.split(".")[0]

            if getters.getType( fileNode ) == "file":

                raw = True if cmds.getAttr( fileNode+".colorSpace" ) == "Raw" else False
                alpha = True if cmds.getAttr( fileNode+".alphaIsLuminance" ) else False
                filt = True if cmds.getAttr( fileNode+".aiFilter" ) == 0 else False
                bias = True if cmds.getAttr( fileNode+".aiMipBias" ) < 0 else False

                cmds.checkBox( "ed"+shadingType.capitalize()+"Raw", edit=True, value = raw ) 
                cmds.checkBox( "ed"+shadingType.capitalize()+"Alpha", edit=True, value = alpha ) 
                cmds.checkBox( "ed"+shadingType.capitalize()+"Filter", edit=True, value = filt ) 
                cmds.checkBox( "ed"+shadingType.capitalize()+"Bias", edit=True, value = bias )



        # ===================================================================
        #
        #       CONNECTIONS GETTERS
        #
        # ===================================================================



        # Get displacement Connections
        def getDisplacementConnections(shader):
            displacementResult = []
            SG = getters.getShadingGroup( shader )
            displacementNode = getters.getNodeConnected( SG + ".displacementShader", onlynode = True )
            if displacementNode:
                texture = getters.getNodeConnected( displacementNode + ".displacement" )
                displacementResult.append( displacementNode )
                displacementResult.append( texture ) 

            return displacementResult




        # Get Normals/Bump Connections
        def getNormalsConnections(shader):

            orderList = []

            nodeA = getters.getNodeConnected( shader + ".normalCamera" )
            if nodeA:
                typeNodeA = getters.getType( nodeA )
                nodeA = self.separateNodeAttr( nodeA )[0] # Leave Node Alone
                nodeB = False

                if "aiNormalMap" in typeNodeA :
                    textureNodeA = getters.getNodeConnected( nodeA + ".input" )
                    orderList.append( ( typeNodeA, nodeA, textureNodeA ) )

                    nodeB = getters.getNodeConnected( nodeA + ".normal" )   
                    # If Second Node is Connected, it is bump2d
                    if nodeB:            
                        typeNodeB = getters.getType( nodeB )
                        nodeB = self.separateNodeAttr( nodeB )[0] # Leave Node Alone
                        textureNodeB = getters.getNodeConnected( nodeB + ".bumpValue" )
                        orderList.append( ( typeNodeB, nodeB, textureNodeB ) )


                elif "bump2d" in typeNodeA :
                    textureNodeA = getters.getNodeConnected( nodeA + ".bumpValue" )
                    orderList.append( ( typeNodeA, nodeA, textureNodeA ) )

                    nodeB = getters.getNodeConnected( nodeA + ".normalCamera" )
                    # If Second Node is Connected, it is aiNormalMap
                    if nodeB:
                        typeNodeB = getters.getType( nodeB )
                        nodeB = self.separateNodeAttr( nodeB )[0] # Leave Node Alone
                        textureNodeB = getters.getNodeConnected( nodeB + ".input" )
                        orderList.append( ( typeNodeB, nodeB, textureNodeB ) )        

            return orderList


        def getAOConnections( node ):
            
            listLayersResult = []
            connNode = node
            #If There is a connection
            if connNode:
                typeConnNode = getters.getType( connNode )
                # If the node is a layeredTexture
                # If node has the "edToolsAO" system
                if "layeredTexture" in typeConnNode and "edToolsAO" in connNode:
                    global edToolsShadingAONode
                    edToolsShadingAONode = connNode

                    listLayers = cmds.listAttr( connNode+".inputs", multi = True)
                    if listLayers:
                        for layer in listLayers:
                            layerAttr = self.separateNodeAttr(layer)                
                            # If split result has two elements, input and attribute
                            if len(layerAttr) == 2:
                                # if the attribute is color
                                if layerAttr[1] == "color":                                    
                                    
                                    # Assigning the layer id to a dict
                                    texture = getters.getNodeConnected( connNode+"."+layer )
                                    listLayersResult.append( [ layerAttr[0].encode('utf-8'), texture ] )


            return listLayersResult



        # ===================================================================
        #
        #       GETTING SPECIALS MAPS
        #
        # ===================================================================


        #----------------------------------------------------------------------
        #       Displacement
        #----------------------------------------------------------------------
        def getDisplacementMapsPref():        

            displacementConn = getDisplacementConnections( shader )

            if displacementConn:
                print(displacementConn)
                displacementNode, displacementTexture = displacementConn

                # Disbale AutoBump in displacementNode immediately, let's autobump in shape node runs
                if "displacementShader" in getters.getType( displacementNode ):
                    cmds.setAttr( displacementNode+".aiDisplacementAutoBump", False )


                # If exist a texture, load the texture in the form
                if displacementTexture:
                    self.connectAttr( displacementTexture,  dummy + ".disp" )
                    getTextureToFormPref( displacementTexture, "disp" )

                # Load Preferences of Displacement Type and Iterations
                if len(edToolsShadingShapes) == 1 :
                    
                    #Subdivition Type
                    subType = cmds.getAttr( edToolsShadingShapes[0] + ".aiSubdivType" )
                    subTypeRes = "None"
                    if subType == 1: subTypeRes = "Catclark"
                    elif subType == 2: subTypeRes = "Linear"

                    #Subdivition Iterations
                    subCount = cmds.getAttr( edToolsShadingShapes[0] + ".aiSubdivIterations" )

                    #Displacement Height
                    disHeight = cmds.getAttr( edToolsShadingShapes[0] + ".aiDispHeight" )

                    #AutoBump
                    autoBump = cmds.getAttr( edToolsShadingShapes[0] + ".aiDispAutobump" )


                    cmds.optionMenuGrp("edShadingSubdivisionType", e = True, v = subTypeRes )
                    cmds.intSliderGrp( "edShadingDivisionsCount", e = True, v = subCount )
                    cmds.floatSliderGrp( "edShadingDisplacementHeight", e = True, v = disHeight )
                    cmds.checkBoxGrp( "edShadingAutoBumpDisp", edit = True, value1 = autoBump )

            

        #----------------------------------------------------------------------
        #       Normals/Bump
        #----------------------------------------------------------------------
        def getNormalBumpMapsPref():

            normalsOrder = getNormalsConnections( shader )
            # If there is any normal/bump connection
            if normalsOrder:
                numberNodes = len(normalsOrder)
                nodeAType, nodeA, textureA = normalsOrder[0]

                nodesNames = {"normal":False,"bump":False}

                if "bump2d" in nodeAType:
                    nodesNames["bump"] = nodeA
                    cmds.radioButton( 'edShadinOptBump', e = True, select = True)                    
                    if textureA:
                        self.connectAttr( textureA,  dummy + ".bump" )
                        getTextureToFormPref( textureA, "bump" )

                    if numberNodes == 2:
                        nodesNames["normal"] = normalsOrder[1][1]
                        textureB = normalsOrder[1][2]
                        if textureB:
                            self.connectAttr( textureB,  dummy + ".normal" )
                            getTextureToFormPref( textureB, "normal" )

                elif "aiNormalMap" in nodeAType:
                    nodesNames["normal"] = nodeA
                    cmds.radioButton( 'edShadinOptNormals', e = True, select = True)
                    if textureA:
                        self.connectAttr( textureA,  dummy + ".normal" )
                        getTextureToFormPref( textureA, "normal" )
                    if numberNodes == 2:
                        nodesNames["bump"] = normalsOrder[1][1]
                        textureB = normalsOrder[1][2]
                        if textureB:
                            self.connectAttr( textureB,  dummy + ".bump" )
                            getTextureToFormPref( textureB, "bump" )


                # Get sliders values
                if nodesNames["bump"]:
                    val = cmds.getAttr( nodesNames["bump"]+".bumpDepth" )
                    cmds.floatSliderGrp( "edShadingBumpVal", e = True, v = val )
                    global edToolsShadingBumpNode
                    edToolsShadingBumpNode = nodesNames["bump"]
                if nodesNames["normal"]:
                    val = cmds.getAttr( nodesNames["normal"]+".strength" )
                    cmds.floatSliderGrp( "edShadingNormalVal", e = True, v = val )
                    global edToolsShadingNormalNode
                    edToolsShadingNormalNode = nodesNames["normal"]




        #----------------------------------------------------------------------
        #       Ambient Oclussion
        #----------------------------------------------------------------------
        def getAOMapsPref():
            #AOLayeredConns = getAOConnections( shader )

            # Query node connected to a baseColor attr
            connNode = getters.getNodeConnected( shader + ".baseColor", onlynode = True ) 

            AOLayeredConns = getAOConnections( connNode )

            if AOLayeredConns:

                layerAO = AOLayeredConns[0][0] # input[n]
                textureAO = AOLayeredConns[0][1] # file#

                if len(AOLayeredConns) < 2:
                    textureDiffuse = False
                else:
                    textureDiffuse = AOLayeredConns[1][1] # 

                # Disconnect texture from colorBase
                self.disconnectAttr("edTools.color")

                if textureAO:
                    
                    self.connectAttr( textureAO,  dummy + ".ao" )
                    getTextureToFormPref( textureAO, "ao" )

                    # Setting blendMode to Multiply Just in Case                    
                    cmds.setAttr( edToolsShadingAONode+"."+layerAO+".blendMode", 6 )

                    # Get the alpha value
                    multiplyVal = cmds.getAttr( edToolsShadingAONode+"."+layerAO+".alpha" )
                    cmds.floatSliderGrp( "edShadingAOMultiply", e = True, v = multiplyVal )
                    
                    # Update difuse texture
                    if textureDiffuse:
                        self.connectAttr( textureDiffuse,  dummy + ".color" )
                        typeTextureDiffuse = getters.getType( textureDiffuse )
                        if "file" in typeTextureDiffuse:
                            getTextureToFormPref( textureDiffuse, "color" )





        # ===================================================================
        #
        #       SAVING SPECIALS MAPS
        #
        # ===================================================================


        #----------------------------------------------------------------------
        #       Displacement
        #----------------------------------------------------------------------            
        def setDisplacementMapsPref():
            
            shapes = edToolsShadingShapes
            texture = getters.getNodeConnected( dummy+".disp" )
            if texture:    
                # Check shader connection first
                SG = getters.getShadingGroup( shader )
                dispNode = getters.getNodeConnected( SG+".displacementShader", onlynode = True )    
                # if nothing connected on shader, create a new one
                if not dispNode:    
                    dispNode = cmds.createNode( 'displacementShader' )
                    self.connectAttr( dispNode+".displacement", SG+".displacementShader" )       
                # Disbale AutoBump in displacementNode immediately, let's autobump in shape node runs    
                cmds.setAttr( dispNode+".aiDisplacementAutoBump", False )
                # Conect texture to the displacemnet node, and apply preferences
                self.connectAttr( texture,  dispNode+".displacement" )
                setFormToTexturePref( texture, "disp" )
                
                divType = cmds.optionMenuGrp("edShadingSubdivisionType", q = True, v = True )
                iterations = cmds.intSliderGrp( "edShadingDivisionsCount", q = True, v = True )
                height = cmds.floatSliderGrp( "edShadingDisplacementHeight", q = True, v = True )
                autobump = cmds.checkBoxGrp( "edShadingAutoBumpDisp", q = True, value1 = True )
                
                for shape in shapes:
                    
                    shape = shape.encode("utf-8")

                    divTypeRes = 0
                    if divType == "Catclark": divTypeRes = 1
                    elif divType == "Linear": divTypeRes = 2
                           
                    cmds.setAttr( shape + '.aiDispAutobump', autobump )
                    cmds.setAttr( shape + '.aiSubdivIterations',iterations )
                    cmds.setAttr( shape + '.aiDispHeight', height )
                    cmds.setAttr( shape + '.aiSubdivType', divTypeRes )

            # Disconnecting displacement node
            else:
                SG = getters.getShadingGroup( shader )
                dispNode = getters.getNodeConnected( SG+".displacementShader", onlynode = True )    
                # if nothing connected on shader, create a new one
                if dispNode:                    
                    self.deleteNode( dispNode ) # Delete attr




        #----------------------------------------------------------------------
        #       Normals/Bump
        #----------------------------------------------------------------------
        def setNormalBumpMapsPref():

            textureBump = getters.getNodeConnected( dummy+".bump" )
            textureNormal = getters.getNodeConnected( dummy+".normal" )

            # Converting originalConnList to a queriable Dictionary
            originalConnList = getNormalsConnections( shader ) 
            originalConn = {
            "aiNormalMap" : False,
            "bump2d" : False
            }
            for i,item in enumerate( originalConnList ):
                originalConn[ item[0] ] = True
                originalConn[ item[0]+"Name" ] = item[1]
                originalConn[ item[0]+"Order" ] = i+1


            # Disconect normalsCamera connections
            self.disconnectAttr( shader + ".normalCamera" ) # Shader Itself
            if originalConn["aiNormalMap"]:
                self.disconnectAttr( originalConn["aiNormalMapName"] + ".normal" ) # Normal Node
            if originalConn["bump2d"]:
                self.disconnectAttr( originalConn["bump2dName"] + ".normalCamera" ) # Bump Node
                

            #---------------------------
            #    Bump
            #---------------------------
            if textureBump:    
                # If a node already exist, connect the texture to the node, else create a new one
                if originalConn["bump2d"]:
                    self.connectAttr( textureBump, originalConn["bump2dName"] + ".bumpValue" )       
                else:        
                    bumpNode = cmds.createNode( 'bump2d' ).encode("utf-8")
                    originalConn["bump2d"] = True
                    originalConn["bump2dName"] = bumpNode
                    self.connectAttr( textureBump, bumpNode + ".bumpValue" )
                    
                # Apply preferences to the texture
                setFormToTexturePref( textureBump, "bump" ) 
                # apply sliders preferences to nodes
                bumpSliderVal = cmds.floatSliderGrp( "edShadingBumpVal", q = True, v = True )
                cmds.setAttr( originalConn["bump2dName"] + '.bumpDepth', bumpSliderVal )

                global edToolsShadingBumpNode
                edToolsShadingBumpNode = originalConn["bump2dName"]
                    
            else:
                if originalConn["bump2d"]:
                    self.deleteNode( originalConn["bump2dName"] ) # Delete Node

            #---------------------------
            #    Normal
            #---------------------------
            if textureNormal:
                # If a node already exist, connect the texture to the node, else create a new one
                if originalConn["aiNormalMap"]:
                    self.connectAttr( textureNormal, originalConn["aiNormalMapName"] + ".input" )       
                else:        
                    normalNode = cmds.createNode( 'aiNormalMap' ).encode("utf-8")
                    originalConn["aiNormalMap"] = True
                    originalConn["aiNormalMapName"] = normalNode
                    self.connectAttr( textureNormal, normalNode + ".input" )    

                # Apply preferences to the texture        
                setFormToTexturePref( textureNormal, "normal" )
                # apply sliders preferences to nodes
                normalSliderVal = cmds.floatSliderGrp( "edShadingNormalVal", q = True, v = True )
                cmds.setAttr( originalConn["aiNormalMapName"] + '.strength', normalSliderVal )
                global edToolsShadingNormalNode
                edToolsShadingNormalNode = originalConn["aiNormalMapName"]
                
            else:
                if originalConn["aiNormalMap"]:
                    self.deleteNode( originalConn["aiNormalMapName"] ) # Delete Node
                    

            # Organizing and connecting nodes        
            if textureNormal and textureBump:

                firstElement = cmds.radioCollection( "edShadingNormalsOrder", q = True, select = True )
                
                # If bump node is the first element
                if firstElement == "edShadinOptBump":
                    # Connect normal to bump
                    self.connectAttr( originalConn["aiNormalMapName"]+".outValue", originalConn["bump2dName"] + ".normalCamera" )
                    # Connect bump to the shader
                    self.connectAttr( originalConn["bump2dName"]+".outNormal", shader+".normalCamera" )       
                else:
                    # Connect normal to bump
                    self.connectAttr( originalConn["bump2dName"]+".outNormal", originalConn["aiNormalMapName"] + ".normal" )
                    # Connect normal to the shader
                    self.connectAttr( originalConn["aiNormalMapName"]+".outValue", shader+".normalCamera" )


            elif textureNormal:
                # Connect normal to the shader
                self.connectAttr( originalConn["aiNormalMapName"]+".outValue", shader+".normalCamera" )
            elif textureBump:
                # Connect bump to the shader
                self.connectAttr( originalConn["bump2dName"]+".outNormal", shader+".normalCamera" )




        #----------------------------------------------------------------------
        #       Ambient Oclussion
        #----------------------------------------------------------------------
        def setAOMapsPref():

            originalConnAO = getAOConnections( edToolsShadingAONode ) # [ (input[n], textureAO), (input[n], textureColor) ]
            #fixing
            
            
            texture = getters.getNodeConnected( dummy+".ao" )
            if texture:
                
                nodeAO = False
                inputAO = ""
                inputColor = ""
                textureColor = ""                
                
                # if there is an AO Node already, use it, else create a new one    
                if edToolsShadingAONode:
                    nodeAO = edToolsShadingAONode
                    inputAO = originalConnAO[0][0]
                    inputColor = "inputs[" + str( int( inputAO.replace("inputs[","").replace("]",""))+1 ) + "]" # Setting the colorLayer input value as the next numeber
                    textureColor = getters.getNodeConnected( dummy+".color" )
                else:
                    nodeAO = cmds.createNode( 'layeredTexture', name=" edToolsAO_"+shader+"_layerTexture" ).encode("utf-8")
                    global edToolsShadingAONode
                    edToolsShadingAONode = nodeAO
                    inputAO = "inputs[0]"
                    inputColor = "inputs[1]"
                    textureColor = getters.getNodeConnected( shader+".baseColor" )

                        
                # Disconnect baseColor attr
                self.disconnectAttr( shader + ".baseColor" ) # Shader Itself
                
                # Connect AO and Color textures to the layer
                self.connectAttr( texture, nodeAO + "." + inputAO + ".color" )
                if textureColor:
                    self.connectAttr( textureColor, nodeAO + "." + inputColor + ".color" )
                else:
                    self.disconnectAttr( nodeAO + "." + inputColor + ".color" )
                    
                    

                # Connect NodeAO to shader
                self.connectAttr( nodeAO+".outColor", shader+".baseColor" )
                
                
                # Setting blendMode to Multiply
                cmds.setAttr( nodeAO+"."+inputAO+".blendMode", 6 )
                # Set the alpha value
                multiplyVal = cmds.floatSliderGrp( "edShadingAOMultiply", q = True, v = True )
                cmds.setAttr( nodeAO+"."+inputAO+".alpha", multiplyVal )
                # Set preferences to texture
                setFormToTexturePref( texture, "ao" )

            else:
                if edToolsShadingAONode:
                    self.deleteNode(edToolsShadingAONode)        
                    textureColor = getters.getNodeConnected( dummy+".color" )
                    if textureColor:
                        self.connectAttr( textureColor, shader+".baseColor" )
                    edToolsShadingAONode = None




                    



        # ===================================================================
        #
        #       SHADING TOOL
        #
        # ===================================================================



        if type == "set":

            #-----------------------------------------------------------------------------------
            #       REGULAR NODES
            #-----------------------------------------------------------------------------------

            #-----------------------------------
            # Difuse
            #-----------------------------------

            #textureAO = getters.getNodeConnected( dummy+".ao" )
            #if not textureAO:
            shaderAttr = shader + ".baseColor"
            self.disconnectAttr( shaderAttr )
            texture = getters.getNodeConnected( dummy+".color" )
            if texture:
                self.connectAttr( texture,  shaderAttr )
                setFormToTexturePref( texture, "color" )

            #-----------------------------------
            # Metalness
            #-----------------------------------
            shaderAttr = shader+".metalness"
            self.disconnectAttr( shaderAttr )
            texture = getters.getNodeConnected( dummy+".metalness" )
            if texture:
                self.connectAttr( texture, shaderAttr )
                setFormToTexturePref( texture, "metalness" )

            #-----------------------------------
            # Color Specular
            #-----------------------------------
            shaderAttr = shader+".specularColor"
            self.disconnectAttr( shaderAttr )
            texture = getters.getNodeConnected( dummy+".colorSpec" )
            if texture:
                self.connectAttr( texture, shaderAttr )
                setFormToTexturePref( texture, "colorSpec" )

            #-----------------------------------
            # specular Roughness
            #-----------------------------------
            shaderAttr = shader+".specularRoughness"
            self.disconnectAttr( shaderAttr )
            texture = getters.getNodeConnected( dummy+".roughness" )
            if texture:
                self.connectAttr( texture, shaderAttr  )
                setFormToTexturePref( texture, "roughness" )


            #-----------------------------------------------------------------------------------
            #       SPECIAL NODES
            #-----------------------------------------------------------------------------------
            
            setDisplacementMapsPref()
            setNormalBumpMapsPref()
            setAOMapsPref()





        if type == "get":



            #-----------------------------------------------------------------------------------
            #       REGULAR NODES
            #-----------------------------------------------------------------------------------

            #-----------------------------------
            # Difuse
            #-----------------------------------
            texture = getters.getNodeConnected( shader+".baseColor" )
            if texture:
                self.connectAttr( texture,  dummy + ".color" )
                getTextureToFormPref( texture, "color" )

            #-----------------------------------
            # Metalness
            #-----------------------------------
            texture = getters.getNodeConnected( shader+".metalness" )
            if texture:
                self.connectAttr( texture,  dummy+".metalness" )
                getTextureToFormPref( texture, "metalness" )

            #-----------------------------------
            # Color Specular
            #-----------------------------------
            texture = getters.getNodeConnected( shader+".specularColor" )
            if texture:
                self.connectAttr( texture,  dummy+".colorSpec" )
                getTextureToFormPref( texture, "colorSpec" )

            #-----------------------------------
            # specular Roughness
            #-----------------------------------
            texture = getters.getNodeConnected( shader+".specularRoughness" )
            if texture:
                self.connectAttr( texture,  dummy+".roughness" )
                getTextureToFormPref( texture, "roughness" )



            #-----------------------------------------------------------------------------------
            #       SPECIAL NODES
            #-----------------------------------------------------------------------------------
            
            getDisplacementMapsPref()
            getNormalBumpMapsPref()
            getAOMapsPref()











    #========================================================================================================================

    @classmethod        
    def showObjInAE(self):

        sel = cmds.ls( selection = True )                

        # if something is selected
        if sel: 
            # Type of the node
            typeNode = getters.getType( sel[0] ) 
            # Transform
            if typeNode == "transform":                 
                panel = cmds.getPanel( withFocus=True ).encode('utf-8')            
                # if we are in de modelPanel and the obj is a transform
                if "modelPanel" in panel:                    
                    material = getters.getMaterial( sel[0] )
                    if material:
                        helpers.focusTabAE( sel[0], force = True )
                        helpers.focusTabAE( material )
                    pass

            # ShadingEngine
            elif typeNode == "shadingEngine":                
                helpers.focusTabAE( sel[0], force=True )


    
    # Focus TAB on attributeEditor
    @classmethod
    def focusTabAE(self,  node, force = False ):

        if not force:            
            # Name of AtributeEditor Tab
            aeTabName = mel.eval('$aeTabName = $gAETabLayoutName;')
            # List of tabs
            listTabs = cmds.tabLayout( aeTabName, q=1, tl=1)
            if node in listTabs:
                indexTabShader = listTabs.index( node ) + 1 
                cmds.tabLayout( aeTabName , edit=True, selectTabIndex = indexTabShader )
                mel.eval("AEbuildControls;")
        else:
            mel.eval ( ' showEditorExact("{data}") '.format(data=node) )


    @classmethod
    def uni2Str( self, data):
        return data.encode('utf-8')





    @classmethod
    def showAttrEditor(self, obj ):        
        cmds.select( obj )
        mel.eval( 'showEditor( ' + obj + ' )' )

    @classmethod
    def showAttr( self, name=False):  

        # Allows the cell to be editable
        def letChange(*args):
            return 1
        
        if not name:
            sel = cmds.ls( selection = True )
            if sel:
                name = sel[0]
        
        if name:

            listAttr = cmds.attributeInfo( name, all=True, s=True )

            if cmds.window( 'edAttrViewer', exists=True):
                cmds.deleteUI( 'edAttrViewer' )
            elif cmds.windowPref( 'edAttrViewer', exists=True):
                cmds.windowPref( 'edAttrViewer', remove=True)
                 

            window = cmds.window( 'edAttrViewer', t=name, w=600, h=800 )

            form = cmds.formLayout()
            table = cmds.scriptTable( rows=0, columns=4, cw=[[1, 50], [2, 150], [3, 150], [4,150] ], l=((1, 'Short'), (2,'Long'), (3,'Nice'), (4,'Type') ), ccc=letChange)
            cmds.formLayout(form, edit=True, attachForm=[[table, 'right', 0], [table, 'left', 0], [table, 'top', 0], [table, 'bottom', 0]])

            for i in listAttr:
                cmds.scriptTable(table, edit=True, insertRow=1)

            for i,short in enumerate(listAttr):

                longer = cmds.attributeName( name+"."+short, l=True )
                nice = cmds.attributeName( name+"."+short )

                try: typeAttr = cmds.getAttr( name+"."+short, type=True)
                except: typeAttr = ""

                cmds.scriptTable(table, edit=True, ci=[1+i, 1], cellValue = short )
                cmds.scriptTable(table, edit=True, ci=[1+i, 2], cellValue = longer )
                cmds.scriptTable(table, edit=True, ci=[1+i, 3], cellValue = nice )
                cmds.scriptTable(table, edit=True, ci=[1+i, 4], cellValue = typeAttr )
               
            cmds.scriptTable(table, edit=True,ccc=lambda *x: False)
            cmds.showWindow(window)


















