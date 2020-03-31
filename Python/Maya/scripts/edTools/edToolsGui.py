import maya.cmds as cmds
import edToolsGuiFunc as f


#------------------------------------------------------------------------------------------------
#          UI Layout
#------------------------------------------------------------------------------------------------


class layout():

    def __init__(self):
        reload(f)
        self.f=f.uiFunc()  
        


    def script(self):



        #win = cmds.window(title="Tabbed Layout", widthHeight=(300, 500))

 

        def tBox( id, data ):
            cmds.columnLayout( bgc=[0.2,0.2,0.2], adjustableColumn=True )
            cmds.frameLayout(mw=12, mh=12, lv=False )
            cmds.scrollField( id, height=200, editable=False, wordWrap=True, bgc=[0.2,0.2,0.2], text=data )
            cmds.setParent("..")
            cmds.setParent("..")

        colArgs = {"adjustableColumn":True}
        scrollArgs = {"childResizable":True}
        frameArgs = {"collapsable":True, "bgs":True, "mw":20, "mh":20}
        cssChkBox = { "cc" : lambda *args : self.f.edCssDone(0) }


        tabs = cmds.tabLayout()


        #--------------------------------------------------------------------------------
        # Arnold Tab
        #--------------------------------------------------------------------------------
        arnoldTab = cmds.scrollLayout( **scrollArgs )

        cmds.frameLayout( label='Buttons', **frameArgs)
        cmds.columnLayout( **colArgs )
        cmds.text("Test")
        cmds.setParent("..") #columnLayout
        cmds.setParent("..")    #frameLayout

        cmds.setParent("..")

        #--------------------------------------------------------------------------------
        # CSS Tab
        #--------------------------------------------------------------------------------
        cssTab = cmds.scrollLayout( **scrollArgs )

        cmds.separator( height=8, style='none' )        
        cmds.text( label='Maya to CSS Exporter' )
        cmds.separator( height=20, style='in' )

        cmds.columnLayout( columnOffset=["both",10],**colArgs )
        cmds.checkBox( "edCssJavascript",label='Javascript', value=True, **cssChkBox )
        cmds.checkBox( "edCssHtml", label='Html', value=True, **cssChkBox )
        cmds.setParent("..") #colLayout

        cmds.separator( height=8, style='none' )

        cmds.rowLayout( numberOfColumns=2, columnWidth2=(50, 40), adjustableColumn=1, columnAlign=(1, 'right'), columnAttach=[(1, 'left', 10), (2, 'both', 0)] )
        cmds.textField( "edCssPathFolder", text="C:/CSS3DEngine/", bgc=[0.22,0.22,0.22], rfc = lambda *args : self.f.edCssDone(0) )
        cmds.iconTextButton( style='iconOnly', image1='openScript.png', al="center", label='Choose Folder', command=lambda *args : self.f.cssSetFolder("edCssPathFolder") )
        cmds.setParent("..") #rowLayout

        cmds.separator( height=10, style='none' )
        
        cmds.rowLayout( "edCssDoneContainer", numberOfColumns=2, columnWidth2=(50, 1), adjustableColumn=1, columnAlign=(1, 'left'), columnAttach=[(1, 'both', 10), (2, 'both', 0)] )
        cmds.button(label="Export Project", command = self.f.exportCssProject )
        cmds.picture( image='confirm.png' )
        cmds.setParent("..") #rowLayout

        
        cmds.frameLayout(mw=10, mh=10,lv=False)                
        cmds.separator( height=20, style='in' )
        tBox( "edCssMsgBox", self.f.msgCssInstruction() )
        cmds.setParent("..") #frameLayout


        cmds.setParent("..")#scrollLayout

        #--------------------------------------------------------------------------------
        # FIX Tab
        #--------------------------------------------------------------------------------
        fixTab = cmds.scrollLayout( **scrollArgs )

        cmds.button(label="Button")


        cmds.setParent("..")


        cmds.tabLayout(tabs, edit=True, tabLabel=[arnoldTab, 'Arnold'])
        cmds.tabLayout(tabs, edit=True, tabLabel=[cssTab, 'CSS'])
        cmds.tabLayout(tabs, edit=True, tabLabel=[fixTab, 'Fixing'])

        #cmds.tabLayout(tabs, edit=True, selectTabIndex=2)



        #cmds.showWindow()