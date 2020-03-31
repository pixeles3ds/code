'''

How install:
    
1. Guardar [edTools] carpera entera en:

    C:\Users\Edwin\Documents\maya\20xx\prefs\scripts

2. Ejecutar con:


import edTools.edTools as et

reload(et) # Reloading module
e = et.ui() # Instancing edTools

e.showUI() # Running UI


'''

import maya.cmds as cmds
import edToolsGui as edUILayout


#------------------------------------------------------------------------------------------------
#          UI Layout
#------------------------------------------------------------------------------------------------


class ui():

    def __init__(self):        
        self.winID = 'edTools'

    def getLayout(self):
        reload(edUILayout) # Reloading Module edUILayout when I run UI
        edUILayout.layout().script()
       
    def deleteUi(self):
       #cmds.workspaceControl(self.winID, edit = True, uiScript=uiBuild3)
        if cmds.workspaceControl(self.winID, q=True, exists=True):
            cmds.workspaceControl(self.winID, e=True, close=True)
        if cmds.workspaceControlState(self.winID, q=True, exists=True):
            cmds.workspaceControlState(self.winID, e=True, remove=True)   
        if cmds.window(self.winID, exists=True):
            cmds.deleteUI(self.winID)
        elif cmds.windowPref(self.winID, exists=True):
            cmds.windowPref(self.winID, remove=True)

    def showUI(self):            
        self.deleteUi()     
        cmds.workspaceControl(self.winID, tabToControl=('AttributeEditor', -1), retain=False, floating=True, l='EdTools', uiScript="e.getLayout()",iw=250,mw=250, r=True)
        