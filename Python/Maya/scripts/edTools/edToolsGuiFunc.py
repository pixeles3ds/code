import maya.cmds as cmds
import edCore as edCore
import Maya2CSS3D

'''
btn.setLabel("Uncheck")
'''

#------------------------------------------------------------------------------------------------
#          UI Functions
#------------------------------------------------------------------------------------------------

class uiFunc():

    def __init__(self):

        self.fileDialogPath = "C:/"

        reload(edCore)
        reload(Maya2CSS3D)

        self.ecs = edCore.system() 
        self.ech = edCore.helpers() 
        self.m2css = Maya2CSS3D.webApp() 
        
    
    def getControlByName( self, name ):
        if( type(name) == "str" ): return cmds.control( name, query=True , fullPathName=True)
        else:  return name
    
    def getVal(self, control ):

        control = self.getControlByName( control )
        
        if cmds.objectTypeUI( control ) == "field":
            return cmds.textField( control, query=True, text=True)

        elif cmds.objectTypeUI( control ) == "checkBox":
            return cmds.checkBox( control, query=True, value=True)

        else:
            return False
        


    def btn2Fun(self,id):
        print( id)
        print( cmds.textField( "ala", query=True, text=True) )
        print( getVal(id))

        print(cmds.checkBox( "chkk", query=True))
        print(cmds.checkBox("chkk", query=True))




    #--------------------------------------
    #   Maya2CSS
    #--------------------------------------
    

    def cssSetFolder(self,idTextField):
        self.edCssDone(0)
        path = self.ecs.folderPicker( path = self.fileDialogPath )
        if( path):
            path = self.ech.uni2Str(path[0])
            self.fileDialogPath = path
            cmds.textField( "edCssPathFolder", edit=True, text=path )            

    def exportCssProject(self,*args):        
        pathFolder = self.getVal( "edCssPathFolder" )
        jsVal = self.getVal( "edCssJavascript" )
        htmlVal = self.getVal( "edCssHtml" )

        self.m2css.createProject( pathFolder , html=htmlVal, js=jsVal)
        self.edCssDone(1)

    def msgCssInstruction(self,*args):
        msg = "INSTRUCCIONES\n\n"
        msg += "1. Los objs deben estar en la RAIZ o agrupados por solo un grupo\n\n"
        msg += "2. El script exportara objetos juntos si estan agrupados, recibiran el nombre del grupo y tendran la misma textura\n\n"
        msg += "3. Solo exporta planos estaticos, no animaciones\n\n"
        return msg

    def edCssDone(self,opt):
                
        ctr = cmds.control( "edCssDoneContainer", query=True , fullPathName=True)
        if(opt):
            cmds.rowLayout( ctr, edit=True, columnWidth=(2, 30))
        else:
            cmds.rowLayout( ctr, edit=True, columnWidth=(2, 1))
        




        
        