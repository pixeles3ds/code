import maya.cmds as cmds
import maya.mel as mel
from shutil import copyfile
import os
import sys




#=====================================================================================================
#
#           GETTERS
#
#=====================================================================================================

class getters():
    
    def __init__(self):
        pass

    # return shape of a transform node, full = "transfor|shape"
    def getShape( self, nodo, full = 0 ):
        res = cmds.listRelatives( nodo , shapes = True)
        if res:
            name = nodo+"|"+res[0] if full else res[0]
            return name
        else:
            return False
            
            
    # return type of a node
    def getType( self,nodo ):
        return cmds.objectType(nodo)
        
        
    # return all childs 
    def getChilds( self,nodo ):
        return cmds.listRelatives( nodo )


    # return parents of a node
    def getParents( self,nodo ):
        return cmds.listRelatives( nodo , parent = True)

    # return all objects, tipo = all objects of a type
    def getObjs( self,tipo = "" ):   
        if tipo == "": return cmds.ls()
        else: return cmds.ls( type=[ tipo ])

    # return the transform of all original shapes (geometry), without surfaceShape mesh nodes
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
    def getPath( self, ):
        return os.path.dirname(os.path.realpath(__file__))+"/"

    # Get texture system path from transform node
    def getTexture( self, node ):
        shadingGrps = cmds.listConnections(self.getShape( node ),type='shadingEngine')
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
#           SETTERS
#
#=====================================================================================================


class setters():
    
    def __init__(self):
        pass


#=====================================================================================================
#
#           HELPERS
#
#=====================================================================================================

class helpers():
    
    def __init__(self):
        pass
    
    def uni2Str( self, data):
        return data.encode('utf-8')

    def confirm(self,msg):
        msg = "\n" + msg + "\n"
        return self.uni2Str( cmds.confirmDialog( title='Confirm', message=msg, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No' ) )

    def dialog( self, msg ):
        cmds.confirmDialog( title='EdTools', message='\n   %s     \n' % msg  )







#=====================================================================================================
#
#           SYSTEM
#
#=====================================================================================================

class system():
    
    def __init__(self):
        pass
            
    # Create a fileDialog to pick a folder and return the path
    def folderPicker(self, path="C:/"):    
        return cmds.fileDialog2( dialogStyle=1, fileMode=3, dir=path )

    def createFolder( self, name ):
        if not os.path.exists( name ):
            os.makedirs( name )

    def copyF( self, src, dst ):
        copyfile(src, dst)    
        
    def readFile( self, path ):
        f = open( path,"r") 
        data = f.read()
        f.close()
        return data

    def writeFile( self, pathName, data ):
        f = open( pathName, "w") 
        f.write( data ) 
        f.close() 

    # Stop ejecucution
    def stop( self ):
        sys.exit("Stoping")




#==========================================================================================================================================================================================================
#==========================================================================================================================================================================================================
#==========================================================================================================================================================================================================
#==========================================================================================================================================================================================================
#==========================================================================================================================================================================================================
#==========================================================================================================================================================================================================





#=====================================================================================================
#
#           TOOLS WORKFLOW
#
#=====================================================================================================


class workflow():
    
    def __init__(self):
        pass


    # Seleccionar objetos desde una lista
    def sel(self, lista):
        cmds.select(lista);



    # Media de N cantidad de objs   
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
    def obj2Obj(self):
          
        def aling(sel,cord):
            cmds.CreateLocator()
            loc = cmds.ls(sl=True)[0] 
            cmds.move( cord[0], cord[1], cord[2], loc, absolute = True )
            mel.eval( 'manipMoveAlignHandleToComponent("'+loc+'", {"'+ sel[0] +'"}, {""}, "none", 0);')
            cmds.delete( loc )
            
        sel = cmds.ls(sl=True)
        
        if sel:
            tmpCord = [0,0,0]
            if len(sel) == 2:
              tmpCord = cmds.xform(sel[1],q=1,ws=1,rp=1)    
            if len(sel)>2:
              tmpCord = centro( sel[1:] )
            
            aling( sel, tmpCord )

    # Mover pivot hacia otro objeto
    def pivot2center(self):
        mel.eval(" xform -cpc; ")

    # Mover pivot hacia otro objeto
    def pivot2Obj(self):
                
        selObj = cmds.ls(sl=True,type="transform")
        

        if sel:

            shape = selObj[0]

            if len(selObj) == 1:
              self.sel(shape)
              mel.eval(" xform -cpc; ")  
            if len(selObj)>1:
              point = centro( selObj[1:] )
            
            cmds.move(point[0], point[1], point[2], shape+".scalePivot", shape+".rotatePivot", absolute=True)

            self.sel(shape)




