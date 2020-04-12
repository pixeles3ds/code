'''

How install:
    
1. Guardar [edTools] carpera entera en:

    C:\Users\Edwin\Documents\maya\scripts

2. Ejecutar con:


import edToolsMaya.edTools as edTools
reload( edTools ) # Reloading module

edTools.ui.showUI()


'''


import maya.cmds as cmds
import maya.mel as mel
import edToolsGui 
import edCore 

reload( edToolsGui )
reload( edCore )



mel.eval( ' source manipMoveOrient; ') # Importing the Maya manipAxis MEL module
hotkeys = edCore.hotkeys # Assign class hotkeys to global obj



#------------------------------------------------------------------------------------------------
#          Running The ScriptJobs
#------------------------------------------------------------------------------------------------

# Run Once, only when the edTools module is loaded at first time
edCore.scriptJobs.installJobsAtStarting()


#------------------------------------------------------------------------------------------------
#          UI Layout
#------------------------------------------------------------------------------------------------

class ui:
    
    winID = 'edTools'
    winIDShelf = 'edToolsShelf'
    

    @classmethod
    def getLayout(self):
        edToolsGui.layout.script()

    @classmethod
    def getLayoutShelf(self):        
        edToolsGui.layout.scriptShelf()        

    @classmethod
    def deleteUI(self):
        # Main UI
        if cmds.workspaceControl(self.winID, q=True, exists=True):
            cmds.workspaceControl(self.winID, e=True, close=True)            
            cmds.deleteUI(self.winID)
            cmds.workspaceControlState(self.winID, e=True, remove=True)
        # Main UI Shelf
        if cmds.workspaceControl(self.winIDShelf, q=True, exists=True):
            cmds.workspaceControl(self.winIDShelf, e=True, close=True)            
            cmds.deleteUI(self.winIDShelf)
            cmds.workspaceControlState(self.winIDShelf, e=True, remove=True)


    @classmethod
    def showUI(self ):

        self.deleteUI()

        cmds.workspaceControl( self.winID, dockToControl=( 'ToolBox', "right"), retain=True, floating=True, l='EdTools', uiScript="edTools.ui.getLayout()", r=True, iw=320,mw=320, initialHeight = 300, heightProperty="free", collapse=False )
        cmds.workspaceControl( self.winIDShelf, dockToControl=( 'AttributeEditor', "left"), retain=True, floating=True, l='Ed', uiScript="edTools.ui.getLayoutShelf()", r=True, iw=50,mw=50,  heightProperty="free" )        


