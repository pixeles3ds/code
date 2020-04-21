import maya.cmds as cmds
import maya.mel as mel
import Maya2CSS3D
import edCore

reload(edCore)
reload(Maya2CSS3D)

'''
btn.setLabel("Uncheck")
'''

#------------------------------------------------------------------------------------------------
#          UI Functions
#------------------------------------------------------------------------------------------------

class uiFunc():

    fileDialogPath = "C:/"


    #=============================================================================================================
    #
    #               Shelf Buttons
    #
    #=============================================================================================================
    @classmethod
    def shelfCreateArnoldShader(self,*args):        
        self.createAiStandard()
    
    @classmethod
    def openHypershade(self,*args):        
        mel.eval("HypershadeWindow;")

    @classmethod
    def openNodeEditor(self,*args):        
        mel.eval("NodeEditorWindow;")

    @classmethod
    def shelfShowAttr(self,*args):
        edCore.helpers.showAttr()    

    @classmethod
    def reloadUI(self,*args):
        edCore.runPython("import edToolsMaya.edTools as edTools;reload( edTools );edTools.ui.showUI();")    





    #=============================================================================================================
    #
    #               General Functions
    #
    #=============================================================================================================

    @classmethod
    def getControlByName( self, name ):    
        if( type(name) == str ): 
            return cmds.control( name, query=True , fullPathName=True)
        else:  
            return name


    @classmethod
    def getVal(self, control ):

        #control = self.getControlByName( control )        

        if cmds.objectTypeUI( control ) == "field":
            return cmds.textField( control, query=True, text=True )

        elif cmds.objectTypeUI( control ) == "checkBox":
            return cmds.checkBox( control, query=True, value=True )
        
        elif cmds.objectTypeUI( control ) == "radioCluster":
            return cmds.radioCollection( control, query=True, sl=True )

        elif cmds.objectTypeUI( control ) == "rowGroupLayout":
            return cmds.optionMenuGrp(control, query=True, value=True)

        else:
            return None 

    # Permite crear columnas con porcentajes que se ajustan al tamano de su contenedor
    @classmethod
    def formLayoutSet( self, formName, list, padding = 0 ):            

        '''        
        # way to call:

        cmds.formLayout("btnForm")
        obj1 = cmds.button()
        obj2 = cmds.button()
        cmds.setParent("..") # formLayout
        formLayoutSet( "btnForm ", [ ( obj1, porcentaje ), ( obj2, porcentaje ) ], padding = 20 ) 

        '''

        #Positions    
        result = []    
        lastP = 0
        for i,item in enumerate(list):
            
            paddingLeft = padding
            paddingRight = padding
            
            # Adding double padding to first and last item
            if( i == 0): paddingLeft = padding*2 # First Item
            if( i == len(list)-1 ): paddingRight = padding*2 # Last Item
                    
            left = ( item[0], 'left', paddingLeft, lastP )
            right = ( item[0], 'right', paddingRight, item[1] + lastP )
            top = ( item[0], 'top', padding*2 , 0 )
            bottom = ( item[0], 'bottom', padding*2 , 0 )

            result.append( left )
            result.append( right )
            #result.append( top )
            #result.append( bottom )
            
            
            lastP = item[1] + lastP
        
        
        # Padding top and botton
        resultPaddings = []
        for item in list:
            
            top = ( item[0], 'top', padding * 2 )
            bottom = ( item[0], 'bottom', padding * 2 )
           
            resultPaddings.append( top )
            resultPaddings.append( bottom )
            
        cmds.formLayout( formName, edit=True, numberOfDivisions = 100, attachPosition = result, attachForm = resultPaddings )





    #=============================================================================================================
    #
    #               Maya2CSS
    #
    #=============================================================================================================
    
    @classmethod
    def cssSetFolder(self,idTextField):
        self.edCssDone(0)
        path = edCore.system.folderPicker( path = self.fileDialogPath )
        if( path):
            path = edCore.helpers.uni2Str(path[0])
            self.fileDialogPath = path
            cmds.textField( "edCssPathFolder", edit=True, text=path )            

    @classmethod
    def exportCssProject(self,*args):        
        pathFolder = self.getVal( "edCssPathFolder" )
        jsVal = self.getVal( "edCssJavascript" )
        htmlVal = self.getVal( "edCssHtml" )

        Maya2CSS3D.createProject( pathFolder , html=htmlVal, js=jsVal)
        self.edCssDone(1)
        edCore.alert2("Project Exported")
    
    @classmethod
    def msgCssInstruction(self,*args):
        msg = "INSTRUCCIONES\n\n"
        msg += "1. Los objs deben estar en la RAIZ o agrupados por solo un grupo\n\n"
        msg += "2. El script exportara objetos juntos si estan agrupados, recibiran el nombre del grupo y tendran la misma textura\n\n"
        msg += "3. Solo exporta planos estaticos, no animaciones\n\n"
        msg += "4. La escena debe estar mirando hacia el eje Z positivo\n\n"
        msg += "3. Si las imagenes salen mal, arreglar las UV\n\n"
        return msg

    @classmethod
    def edCssDone(self,opt):
                
        ctr = cmds.control( "edCssDoneContainer", query=True , fullPathName=True)
        if(opt):
            cmds.rowLayout( ctr, edit=True, columnWidth=(2, 30))
        else:
            cmds.rowLayout( ctr, edit=True, columnWidth=(2, 1))
        



    #=============================================================================================================
    #
    #               FIX Maya Configuration
    #
    #=============================================================================================================


    @classmethod
    def edWizardInstallation(self,*args):        

        edCore.maya.setAutoloadEdTools( 1 ) # EdTools AutoLoad Enabled
        edCore.maya.setInitOncePreferences() # Init Preferences Saved
        edCore.scriptJobs.installJobsAtStarting() # ScriptJobs
        edCore.hotkeys.installHotKeys() # HotKeys Installed

        edCore.alert("Maya Preferences Saved Successfully!")
        edCore.showWarning("Maya Preferences Saved Successfully!")


    @classmethod
    def edFixSaveLayout(self,*args):
                
        edCore.runPython("edTools.ui.deleteUI()")
        edCore.maya.saveLayout()
        edCore.runPython("edTools.ui.showUI()")   
        cmds.tabLayout("edToolsTabs", edit=True, selectTab="edFixLayout")

    

    #--------------------------------------------------------------------------------


    @classmethod
    def edFixAutoload(self,*args):

        opt = self.getVal( 'edToolsAutoloadEnabler' )
        if "Yes" in opt: opt = 1
        else: opt = 0        
        edCore.maya.setAutoloadEdTools( opt )        
        edCore.showWarning("Autoload Setted!!")

    @classmethod
    def edFixScriptJobs(self,*args):        
        
        opt = self.getVal( 'edToolsScriptJobEnabler' )

        if "Yes" in opt: 
            edCore.scriptJobs.killScriptJob()
            edCore.scriptJobs.createScriptJobs()
            edCore.showWarning("ScriptJobs Installed")
        else: 
            edCore.scriptJobs.killScriptJob()
            edCore.showWarning("ScriptJobs Deleted")


    @classmethod
    def edFixSetInitConf(self,*args):
        edCore.maya.setInitOncePreferences()
        edCore.showWarning("Initial Preferences Setted!!")


    @classmethod
    def edFixInstallHotkeys(self,*args):
        edCore.hotkeys.installHotKeys()
        edCore.showWarning("Hotkey Installed!!")




        
        
    #=============================================================================================================
    #
    #               ARNOLD
    #
    #=============================================================================================================

    @classmethod
    def createAiStandard(self):
        
        # current selection
        sel = edCore.getters.sel()

        #create and connect arnold shader and shading group
        shd = cmds.shadingNode( 'aiStandardSurface', asShader = True)
        shdSG = cmds.sets( name = shd + 'SG'  , empty = True, renderable = True, noSurfaceShader = True )
        cmds.connectAttr( shd + '.outColor', shdSG +'.surfaceShader' )

        #changing some attrs
        cmds.setAttr( shd + '.base', 0.9 ) # No Specular
        #cmds.setAttr( shd + '.specular', 0.0 ) # No Specular

        # Applying Shader to selections
        for i in sel:
            cmds.sets( i , edit = True, forceElement = shdSG )

        #Select the new shader ands shange to properties panel
        cmds.select( sel[0] )
        #edCore.helpers.focusTabAE( shd  )




    #----------------------------------------------------------------------------------------------
    #       Shading System
    #----------------------------------------------------------------------------------------------



    @classmethod
    def selectShader(self):        
        cmds.select( edCore.edToolsShadingSelectedAI )

    @classmethod
    def selectBump(self):        
        cmds.select( edCore.edToolsShadingBumpNode )

    @classmethod
    def selectNormal(self):        
        cmds.select( edCore.edToolsShadingNormalNode )

    @classmethod
    def selectShapes(self):        
        cmds.select( edCore.edToolsShadingShapes )

    @classmethod
    def selectAO(self):        
        cmds.select( edCore.edToolsShadingAONode )


    @classmethod
    def selectShadingDummyNode(self):        
        if cmds.objExists('edTools'):
            cmds.select("edTools")
        else:
            edCore.helpers.createEdDebugSahder( reconnect = True )


    @classmethod
    def changeShapesSelection( self, type):

        shaderSelected = edCore.edToolsShadingSelectedAI

        if shaderSelected:

            totalShapes = []

            if type == "all":
                shapes = edCore.getters.getShapesByMaterial( shaderSelected )
                totalShapes = shapes
                edCore.edToolsShadingShapes = shapes
            elif type == "selected":
                sel = cmds.ls( selection = True )
                if sel:
                    listShapes = []
                    for shape in sel:                      
                        if "transform" == edCore.getters.getType( shape ):
                            material = edCore.getters.getMaterial( shape )
                            if "aiStandardSurface" == edCore.getters.getType(  material ):
                                listShapes.append( shape )
                            else:
                                edCore.showWarning("Must Select an Object with an Arnold Surface")
                        else:
                            edCore.showWarning("Must Select an Arnold Surface !")

                    totalShapes = listShapes
                    edCore.edToolsShadingShapes = listShapes

                else:
                    edCore.showWarning("Nothing Selected")

            shapesLabel = totalShapes[0] if len(totalShapes) == 1 else "( "+str(len(totalShapes))+" )  Shapes"
            cmds.text( 'edShadingShapeSelected', e=True, label = shapesLabel )




    # Create an empty node to store attribute for shading  purpose
    @classmethod
    def createEdDebugSahder(self):
        edCore.helpers.createEdDebugSahder()                

    @classmethod
    def getEdToolsShadingAttrTemplate(self):
        return edCore.helpers.getEdToolsShadingAttrTemplate()



    @classmethod
    def setShadingForm(self, type ):



        def updateShadingForm(shader):
            self.setShadingForm( "reset" )

            edCore.helpers.createEdDebugSahder( reconnect = True )

            shapes = edCore.getters.getShapesByMaterial(shader)

            edCore.edToolsShadingSelectedAI = shader
            edCore.edToolsShadingShapes = shapes

            shapesLabel = shapes[0] if len(shapes) == 1 else "( "+str(len(shapes))+" )  Shapes"

            cmds.button( 'edShaderLabel', e=True, label=shader )
            cmds.text( 'edShadingShapeSelected', e=True, label = shapesLabel )
            cmds.button( "edShaderBtnGet", e=True, vis=False)
            cmds.button( "edShaderBtnUnset", e=True, vis=True)
            edCore.helpers.setEdToolsShading( type = type )







        if type == "set":            
            sel = edCore.edToolsShadingSelectedAI
            if sel:
                edCore.helpers.setEdToolsShading( type = type )                
            else:
                edCore.showWarning("No Shader Selected")



        if type == "get":            

            sel = cmds.ls( selection = True )
            if sel:
                if "aiStandardSurface" == edCore.getters.getType(sel[0]):
                    updateShadingForm( sel[0] )
                elif "transform" == edCore.getters.getType(sel[0]):
                    material = edCore.getters.getMaterial( sel[0] )
                    if "aiStandardSurface" == edCore.getters.getType(  material ):
                        updateShadingForm( material )
                    else:
                        edCore.showWarning("Must Select an Object with an Arnold Surface")
                else:
                    edCore.showWarning("Must Select an Arnold Surface !")
            else:
                edCore.showWarning("Nothing Selected")




        if type == "reset":                                            
            dummy = "edTools"
            
            edCore.edToolsShadingSelectedAI = None
            edCore.edToolsShadingShapes = None
            edCore.edToolsShadingNormalNode = None
            edCore.edToolsShadingBumpNode = None
            edCore.edToolsShadingAONode = None

            # Form COntrols
            cmds.button( 'edShaderLabel', e=True, label="..." )
            cmds.text( 'edShadingShapeSelected', e=True, label = "...")
            cmds.button( "edShaderBtnGet", e=True, vis=True)
            cmds.button( "edShaderBtnUnset", e=True, vis=False)

            # delete Dummy
            if cmds.objExists("edTools"):
                cmds.delete("edTools")

            # Disconnect regular texture files connected to dummy node, and reset checkboxes
            listAttr = edCore.helpers.edToolsShadingAttrTemplate
            for data in listAttr:
                #edCore.helpers.disconnectAttr( dummy+"."+data[0] )
                cmds.checkBox( "ed"+data[0].capitalize()+"Raw", e=True, v=data[2] )
                cmds.checkBox( "ed"+data[0].capitalize()+"Alpha", e=True, v=data[3] )
                cmds.checkBox( "ed"+data[0].capitalize()+"Filter", e=True, v=data[4] )
                cmds.checkBox( "ed"+data[0].capitalize()+"Bias", e=True, v=data[5] )

            # Normal/Bump
            cmds.radioButton( 'edShadinOptBump', e = True, select = True ) # Bump Fisrt
            cmds.floatSliderGrp( "edShadingNormalVal", e = True, v = 1.0 ) # Normal Value
            cmds.floatSliderGrp( "edShadingBumpVal", e = True, v = 1.0 ) # Bump Value
            
            # Extra fields 
            cmds.optionMenuGrp("edShadingSubdivisionType", e=True, value = "None" ) # Subdivision Type List
            cmds.intSliderGrp( "edShadingDivisionsCount", e = True, v = 0 ) # Subdivision Number
            cmds.floatSliderGrp( "edShadingDisplacementHeight", e = True, v = 1.0 ) # Displacemnet Height
            cmds.checkBoxGrp( "edShadingAutoBumpDisp", e = True, value1 = False ) # AutoBump
            
            # AO
            cmds.floatSliderGrp( "edShadingAOMultiply", e = True, v = 1.0 ) # Displacemnet Height
        



            
