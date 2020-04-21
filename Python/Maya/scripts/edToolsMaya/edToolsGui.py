import maya.cmds as cmds
import edToolsGuiFunc 

reload( edToolsGuiFunc )




colArgs = {"adjustableColumn":True}
scrollArgs = {"childResizable":True}
frameArgs = {"collapsable":True, "bgs":False, "mw":10, "mh":10}
frameArgsPadding = { "lv" : False, "bgs" : True, "mw" : 50, "mh" : 20 }
cssChkBox = { "cc" : lambda *args : uiFunc.edCssDone(0) }

uiFunc = edToolsGuiFunc.uiFunc   


class layout():

    

       


    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #       SHELF ICONS LAYOUT
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    
    @classmethod
    def scriptShelf(self):

        iArgs = {"adjustableColumn":True}

        shelf = cmds.shelfLayout( 'shelf', w=40, cellWidthHeight=[40,40] )        
        cmds.separator(height=15)

        cmds.iconTextButton( st='iconOnly', i1='render_aiStandard.png', ann="Create Arnold Shader", c = uiFunc.shelfCreateArnoldShader )
        cmds.iconTextButton( st='iconOnly', i1='objectSet.svg', ann="HyperShade", c = uiFunc.openHypershade )
        cmds.iconTextButton( st='iconOnly', i1='dagNode.svg', ann="Node Editor", c = uiFunc.openNodeEditor )

        cmds.separator(height=15)

        cmds.iconTextButton( st='iconOnly', i1='outliner.png', ann="Show Attributes of selected", c = uiFunc.shelfShowAttr )

        cmds.separator(height=15)

        cmds.iconTextButton( st='iconOnly', i1='perspMultiLayout.png', ann="Reload UI", c = uiFunc.reloadUI )

        cmds.setParent("..")




    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #       ARNOLD LAYOUT
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------

    @classmethod
    def edArnoldLayout(self):

        #Create the dummy node for testing shader purposes
        uiFunc.createEdDebugSahder()
        

        marginCheck = 20

        def edShadingUICreateRow():
            list = uiFunc.getEdToolsShadingAttrTemplate()
            for data in list:    
                attr = data[0]
                type = data[1]
                connectionDest = "edTools." + attr       
                cmds.rowLayout( height = 20, numberOfColumns=5, columnWidth5=( 10, marginCheck, marginCheck, marginCheck, marginCheck ), adjustableColumn=1, columnAlign=(1, 'left'), columnAttach=[1,"right",5] )                
                cmds.attrNavigationControlGrp( "ed"+attr.capitalize()+"Texture", l = attr, columnWidth= [1,60], columnAttach=[1,"right",5], attribute = connectionDest )
                cmds.checkBox( "ed"+attr.capitalize()+"Raw", label='' , v=data[2] )
                cmds.checkBox( "ed"+attr.capitalize()+"Alpha", label='', v=data[3] )
                cmds.checkBox( "ed"+attr.capitalize()+"Filter", label='', v=data[4] )
                cmds.checkBox( "ed"+attr.capitalize()+"Bias", label='', v=data[5] )
                cmds.setParent("..")
                


        #================================================================

        cmds.scrollLayout( "edArnoldLayout", **scrollArgs )        
        cmds.columnLayout(adjustableColumn=True)
        
        #================================================================
        cmds.formLayout("arnoldHeader")

        cmds.columnLayout( "btnSetShaderCont", adjustableColumn = True )
        cmds.button( "edShaderBtnGet", label="Select Shader", height=30, c = lambda *x: uiFunc.setShadingForm("get") )
        cmds.button( "edShaderBtnUnset", label="Unset Shader", height=30, backgroundColor = [0.2,0.2,0.2], vis = False, c = lambda *x: uiFunc.setShadingForm("reset") )
        cmds.setParent("..") # columnLayout

        cmds.columnLayout( "btnShaderSaveCont", adjustableColumn = True )
        cmds.button( l = "SAVE", h=30, c = lambda *x: uiFunc.setShadingForm("set") )
        cmds.setParent("..") # columnLayout        

        cmds.setParent("..") # formLayout
        uiFunc.formLayoutSet( "arnoldHeader", [ ( "btnSetShaderCont", 40 ), ( "btnShaderSaveCont", 60 ) ], padding = 3 ) 

        cmds.columnLayout( adjustableColumn = True, columnAttach=["both",10], columnAlign="left")
        cmds.button( 'edShaderLabel', label="...", c = lambda *x: uiFunc.selectShader() )
        cmds.setParent("..") # columnLayout                
        

        #================================================================
        cmds.separator( h = 6, st="none" )
        cmds.separator( h = 2, st="in" )
        cmds.separator( h = 5, st="none" )
        
        cmds.columnLayout(adjustableColumn=True, columnAttach=["both",5])
        
        cmds.rowLayout( numberOfColumns=5, columnWidth5=( 10, marginCheck, marginCheck, marginCheck, marginCheck ), adjustableColumn=1, columnAlign=(1, 'left') )                
        cmds.columnLayout(adjustableColumn=True, columnAttach=["both",10])
        cmds.button( l='Select Shading Node', c = lambda *x: uiFunc.selectShadingDummyNode() )
        cmds.setParent("..")
        cmds.text( label='Raw')
        cmds.text( label='Alph')
        cmds.text( label='Filt')
        cmds.text( label='Bias')
        cmds.setParent("..")
        cmds.separator( h = 5, st="none" )
        
        #-------------------------------------------------------------------------------------------------------------------------------
        edShadingUICreateRow()
        #-------------------------------------------------------------------------------------------------------------------------------
        
        cmds.setParent("..")
        
        cmds.separator( h = 10, st="none")


        #================================================================
        cmds.frameLayout( label='Normals/Bump', **frameArgs)   
        cmds.rowLayout( numberOfColumns=2, columnWidth2=( 60,50 ), adjustableColumn=2, columnAlign=(1, 'right'), columnAttach=[1,"both",5] )                

        cmds.columnLayout(adjustableColumn=True)       
        cmds.radioCollection( "edShadingNormalsOrder" )
        cmds.radioButton( 'edShadinOptBump', label = 'N > B', select = True )
        cmds.separator( h = 4, st="none")
        cmds.radioButton( 'edShadinOptNormals', label = 'B > N' )       
        cmds.setParent("..")                

        cmds.columnLayout( adjustableColumn=True)         
        cmds.button( l="Select Bump", c = lambda *x: uiFunc.selectBump() )
        cmds.separator( h = 4, st="none")
        cmds.button( l="Select Normal", c = lambda *x: uiFunc.selectNormal() )
        cmds.setParent("..")

        cmds.setParent("..") # RowLayout

        cmds.columnLayout(adjustableColumn=True)       
        cmds.floatSliderGrp( "edShadingNormalVal", label='Normal:  ', field=True, columnWidth3=( 60, 60, 50 ), minValue=0, maxValue=5, value = 1, adjustableColumn = 3, sliderStep = 0.005, precision = 3 )
        cmds.floatSliderGrp( "edShadingBumpVal", label='Bump:  ', field=True, columnWidth3=( 60, 60, 50 ), minValue=-1, maxValue=1, value = 0.1, adjustableColumn = 3, sliderStep = 0.005, precision = 3 )
        cmds.setParent("..")  

        cmds.setParent("..") # FrameLayout
        


        #================================================================
        cmds.frameLayout( label='Displacement', **frameArgs)   

        cmds.rowLayout( numberOfColumns=2, columnWidth2=( 60, 5 ), adjustableColumn=2, columnAlign2=['right','left'], columnAttach = [2,"left", 4]  )                            
        cmds.button(l=" Sel Shape ", c = lambda *x: uiFunc.selectShapes() )
        cmds.text("edShadingShapeSelected", l="..." )
        cmds.setParent("..")

        cmds.rowLayout( numberOfColumns=3, columnWidth3=( 60, 45,60 ), adjustableColumn=3, columnAlign3=['right','left','left'], columnAttach = [2,"left", 4]  )
        cmds.text("")        
        cmds.radioCollection( "edShadingShapesChange" )
        cmds.radioButton( 'edShadinAllShapes', label = 'All', select = True, onCommand = lambda *x: uiFunc.changeShapesSelection("all") )        
        cmds.radioButton( 'edShadinOnlySelectedShape', label = 'Selected', onCommand = lambda *x: uiFunc.changeShapesSelection("selected") )        
        cmds.setParent("..")

        #--------------------------------------------------            
        cmds.columnLayout( adjustableColumn = True )        

        cmds.optionMenuGrp("edShadingSubdivisionType", label='DivType:  ', columnWidth2=(60, 10), adjustableColumn=2, columnAttach = [1,"right", 0]  )
        cmds.menuItem( "edShadingSubTypeNone", label='None' )
        cmds.menuItem( "edShadingSubTypeNoneCatclark", label='Catclark' )
        cmds.menuItem( "edShadingSubTypeNoneLinear", label='Linear' )
        cmds.intSliderGrp( "edShadingDivisionsCount", label='Iterations:  ', field=True, columnWidth3=( 60, 60, 50 ), minValue=0, maxValue=8, value = 0, adjustableColumn = 3 )        
        cmds.floatSliderGrp( "edShadingDisplacementHeight", label='Height:  ', field=True, columnWidth3=( 60, 60, 50 ), minValue=-5, maxValue=5, value = 1, adjustableColumn = 3, sliderStep = 0.005, precision = 3 )
        cmds.checkBoxGrp( "edShadingAutoBumpDisp", numberOfCheckBoxes=1, label='AutoBump:  ', value1=False, columnWidth2=(60, 10), adjustableColumn = 2, columnAttach = [2,"left", 2]  )

        cmds.setParent("..")                
        #--------------------------------------------------
        cmds.setParent("..") # FrameLayout        
        #================================================================


        cmds.frameLayout( label='Ambient Oclussion', **frameArgs)   
        cmds.floatSliderButtonGrp( "edShadingAOMultiply", label='Multiply:  ', field=True, columnAttach = [4,"left", 10], columnWidth4=( 60, 60, 50, 60 ), minValue=0, maxValue=2, value = 1, adjustableColumn = 3, sliderStep = 0.005, precision = 3, buttonLabel='Sel AO', bc = lambda *x: uiFunc.selectAO() )
        cmds.setParent("..")
        #================================================================

        cmds.separator( h = 2, st="in" )

        cmds.setParent("..") # formLayout ArnoldOptions
        cmds.setParent("..") #scrollLayout

        # Deleting the Shading Dummy
        cmds.delete("edTools")



    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #       MAYA2CSS3D LAYOUT
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------

    @classmethod
    def edCssLayout(self):

        def tBox( id, data ):
            cmds.columnLayout( bgc=[0.2,0.2,0.2], adjustableColumn=True )
            cmds.frameLayout(mw=12, mh=12, lv=False )
            cmds.scrollField( id, height=200, editable=False, wordWrap=True, bgc=[0.2,0.2,0.2], text=data )
            cmds.setParent("..")
            cmds.setParent("..")


        cssTab = cmds.scrollLayout( "edCssLayout",**scrollArgs )

        cmds.separator( height=8, style='none' )        
        cmds.text( label='Maya to CSS Exporter' )
        cmds.separator( height=20, style='in' )

        cmds.columnLayout( columnOffset=["both",10],**colArgs )
        cmds.checkBox( "edCssJavascript",label='Javascript', value=True, **cssChkBox )
        cmds.checkBox( "edCssHtml", label='Html', value=True, **cssChkBox )
        cmds.setParent("..") #colLayout

        cmds.separator( height=8, style='none' )

        cmds.rowLayout( numberOfColumns=2, columnWidth2=(50, 40), adjustableColumn=1, columnAlign=(1, 'right'), columnAttach=[(1, 'left', 10), (2, 'both', 0)] )
        cmds.textField( "edCssPathFolder", text="C:/xampp/htdocs/CSS3DEngine/", bgc=[0.22,0.22,0.22], rfc = lambda *args : uiFunc.edCssDone(0) )
        cmds.iconTextButton( style='iconOnly', image1='openScript.png', al="center", label='Choose Folder', command=lambda *args : uiFunc.cssSetFolder("edCssPathFolder") )
        cmds.setParent("..") #rowLayout

        cmds.separator( height=10, style='none' )
        
        cmds.rowLayout( "edCssDoneContainer", numberOfColumns=2, columnWidth2=(50, 1), adjustableColumn=1, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 10), (2, 'both', 0)] )
        cmds.button(label="Export Project", command = uiFunc.exportCssProject )
        cmds.picture( image='confirm.png' )
        cmds.setParent("..") #rowLayout

        
        cmds.frameLayout(mw=10, mh=10,lv=False)                
        cmds.separator( height=20, style='in' )
        tBox( "edCssMsgBox", uiFunc.msgCssInstruction() )
        cmds.setParent("..") #frameLayout


        cmds.setParent("..")#scrollLayout




    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #       FIX MAYA LAYOUT
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------

    @classmethod
    def edFixLayout(self):

        fixTab = cmds.scrollLayout( "edFixLayout", **scrollArgs )

        #---------------------------------
        #   Save Layout Button & WIZARD Installation
        #---------------------------------
        
        cmds.formLayout("edBtnMainWizard")
        edBtnWizard = cmds.button(label="WIZARD INSTALL", height=40, c = uiFunc.edWizardInstallation )
        edBtnSaveLayout = cmds.button(label="SAVE LAYOUT", height=40, c = uiFunc.edFixSaveLayout )
        cmds.setParent("..") # formLayout
        uiFunc.formLayoutSet( "edBtnMainWizard", [ ( edBtnWizard, 50 ), ( edBtnSaveLayout, 50 ) ], padding = 5 ) 

        #---------------------------------
        #   Set AutoLoad EdTools
        #---------------------------------
        
        cmds.frameLayout( label='EdTools AutoStart' )
        cmds.rowLayout( height = 50, numberOfColumns=2, columnWidth2=(10, 120 ), adjustableColumn=1, columnAlign=(1, 'left'), columnAttach=[ (1, 'both', 20), (2, 'both', 0) ] )

        cmds.columnLayout()
        cmds.radioCollection( "edToolsAutoloadEnabler" )
        cmds.radioButton( 'edToolsAutoloadEnablerYes', label = 'Yes', select = True )
        cmds.radioButton( 'edToolsAutoloadEnablerNo', label = 'No' )
        cmds.setParent( '..' )

        cmds.columnLayout()
        cmds.button( l = "Enable Auto Load", c = uiFunc.edFixAutoload )
        cmds.setParent( '..' )

        cmds.setParent( '..' )
        cmds.setParent( '..' )

        #---------------------------------
        #   Install ScriptJobs
        #---------------------------------
        
        cmds.frameLayout( label='Install ScriptJobs' )        
        cmds.rowLayout( height = 50, numberOfColumns=2, columnWidth2=(10, 120 ), adjustableColumn=1, columnAlign=(1, 'left'), columnAttach=[ (1, 'both', 20), (2, 'both', 0) ] )        

        cmds.columnLayout()
        cmds.radioCollection( "edToolsScriptJobEnabler" )
        cmds.radioButton( 'edToolsScriptJobEnablerYes', label = 'Yes', select = True )
        cmds.radioButton( 'edToolsScriptJobEnablerNo', label = 'No' )
        cmds.setParent( '..' )

        cmds.columnLayout()
        cmds.button( l = "Enable Script Jobs", c = uiFunc.edFixScriptJobs )
        cmds.setParent( '..' )

        cmds.setParent( '..' )        
        cmds.setParent( '..' )

        

        #---------------------------------
        #   Maya Init Configuration
        #---------------------------------
        cmds.frameLayout( label='Maya Init configuration', collapse = True, **frameArgs)        
        msg = "Disable WorkSpace AutoSave\n"
        msg += "Drag when creates a Polygon/Nurb\n"        
        msg += "Enable Legacy Render Layers\n"
        msg += "Maya DPI to 125%"
        cmds.text( align = "left", l = msg )
        cmds.setParent("..") # frameLayout
        cmds.frameLayout(  **frameArgsPadding )
        cmds.button(label="Set Init Conf", c = uiFunc.edFixSetInitConf )
        cmds.setParent("..") # frameLayout


        #---------------------------------
        #   Hotkeys Installer
        #---------------------------------
        cmds.frameLayout( label='HotKeys Installer', collapse = False, **frameArgs)
        cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[ (1, 180),(2, 40) ], columnAttach=[1,"right",10] )

        cmds.text( l = 'Show in AttributeEditor:')
        cmds.text( l = 'a' )
        cmds.text( l = '' )
        cmds.separator()
        cmds.text( l = 'Center All Pivots:')
        cmds.text( l = 'c' )
        cmds.text( l = 'Move Pivot to Objects:')
        cmds.text( l = 'Alt + c' )
        cmds.text( l = '' )
        cmds.separator()
        cmds.text( l = 'Context Object:')
        cmds.text( l = 'Alt + q' )
        cmds.text( l = 'Context World:')
        cmds.text( l = 'Alt + w' )
        cmds.text( l = 'Context Custom:')
        cmds.text( l = 'Alt + e' )
        cmds.text( l = 'Context to Self Comp:')
        cmds.text( l = 'Alt + r' )
        cmds.text( l = 'Context to Other Obj Comps:')
        cmds.text( l = 'Alt + d' )
        cmds.text( l = 'Context to Other Obj:')
        cmds.text( l = 'Alt + f' )
        cmds.setParent("..")
        cmds.setParent("..") # frameLayout
        cmds.frameLayout(  **frameArgsPadding )
        cmds.button(label="Install Hotkeys", c = uiFunc.edFixInstallHotkeys )        
        cmds.setParent("..") # frameLayout


        cmds.setParent("..") # ScrollLayout        






    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------
    #       MAIN LAYOUT
    #--------------------------------------------------------------------------------
    #--------------------------------------------------------------------------------




    @classmethod
    def script(self):



        #-------------------------------------------------------------------------------
        #       PANEL LAYOUT VERTICAL
        #-------------------------------------------------------------------------------


        verticalPanel = cmds.paneLayout( configuration='horizontal2' )
                

        #---------------------------
        #       Tabs
        #---------------------------

        cmds.tabLayout("edToolsTabs")
        
        self.edArnoldLayout() # Arnold Tab
        self.edCssLayout() # CSS Tab
        self.edFixLayout() # FIX Tab
        
        cmds.setParent("..") # Tabs
        
        cmds.tabLayout( "edToolsTabs", edit=True, tabLabel=[ "edArnoldLayout", 'Arnold'] )
        cmds.tabLayout( "edToolsTabs", edit=True, tabLabel=[ "edCssLayout", 'CSS'] )
        cmds.tabLayout( "edToolsTabs", edit=True, tabLabel=[ "edFixLayout", 'Fixing'] )


        #---------------------------
        #       Outliner
        #---------------------------

        outlinerPanel = cmds.outlinerPanel()
        outliner = cmds.outlinerPanel(outlinerPanel, query=True,outlinerEditor=True)
        cmds.outlinerEditor( outliner, edit=True, mainListConnection='worldList', selectionConnection='modelList', showShapes=False, showAttributes=False, showConnected=False, showAnimCurvesOnly=False, autoExpand=False, showDagOnly=True, ignoreDagHierarchy=False, expandConnections=False, showCompounds=True, showNumericAttrsOnly=False, highlightActive=True, autoSelectNewObjects=False, doNotSelectNewObjects=False, transmitFilters=False, showSetMembers=True, setFilter='defaultSetFilter' )
        cmds.setParent("..") # outlinerPanel


        cmds.setParent("..") # panelVertical


