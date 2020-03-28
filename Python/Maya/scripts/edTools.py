'''

How install:
    
1. Crear archivo userSetup.py:
    import maya.cmds as cmds
    import edTools as e
2. Guardar edTools en C:\Users\Edwin\Documents\maya\2018\scripts
3. Cargar con:

import edTools as e

'''

import maya.cmds as cmds
import maya.mel as mel
from shutil import copyfile
import os
import sys







'''
//////////////////////////////

            GETTERS

//////////////////////////////
'''


# return shape of a transform node, full = "transfor|shape"
def getShape( nodo, full = 0 ):
    res = cmds.listRelatives( nodo , shapes = True)
    if res:
        name = nodo+"|"+res[0] if full else res[0]
        return name
    else:
        return False
        
        
# return type of a node
def getType( nodo ):
    return cmds.objectType(nodo)
    
    
# return all childs 
def getChilds( nodo ):
    return cmds.listRelatives( nodo )


# return parents of a node
def getParents( nodo ):
    return cmds.listRelatives( nodo , parent = True)

# return all objects, tipo = all objects of a type
def getObjs( tipo = "" ):    
    if tipo == "": return cmds.ls()
    else: return cmds.ls( type=[ tipo ])

# return the transform of all original shapes (geometry), without surfaceShape mesh nodes
def getGeometries():
    list = []
    for tr in getObjs("transform"):
          
        child = getShape(tr,full=1)
        if child:
            tipo = getType(child)            
            if tipo == "mesh":
                list.append(tr)
    return list


# return all groups nodes, (transform) without shapes
def getGroups():
    
    groups = []
    
    transforms = cmds.ls( type=[ "transform" ])
    
    for obj in transforms:
       parents = cmds.listRelatives( obj , parent = True)
       childrens = cmds.listRelatives( obj , shapes = True)
       if( parents is None and  childrens is None):
           groups.append(obj)
    
    return groups


# Seleccionar objetos desde una lista
def sel(lista):
    cmds.select(lista);









'''
//////////////////////////////

    TOOLS INTERNAL CORE

//////////////////////////////
'''

# Media de N cantidad de objs   
def centro(list):

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
def obj2Obj():
      
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
def pivot2center():
    mel.eval(" xform -cpc; ")

# Mover pivot hacia otro objeto
def pivot2Obj():
              
    selObj = cmds.ls(sl=True,type="transform")
    

    if sel:

        shape = selObj[0]

        if len(selObj) == 1:
            sel(shape)
            mel.eval(" xform -cpc; ")  
        if len(selObj)>1:
            point = centro( selObj[1:] )
        
        cmds.move(point[0], point[1], point[2], shape+".scalePivot", shape+".rotatePivot", absolute=True)

        sel(shape)







'''
//////////////////////////////

            SYSTEM

//////////////////////////////
'''

def createFolder( name ):
    if not os.path.exists( name ):
        os.makedirs( name )

def copyF( src, dst ):
    copyfile(src, dst)

def getPath():
    return os.path.dirname(os.path.realpath(__file__))+"/"
    
def readFile( path ):
    f = open( path,"r")       
    data = f.read()
    f.close()
    return data

def writeFile( pathName, data ):
    f = open( pathName, "w") 
    f.write( data ) 
    f.close() 

# Get texture system path from transform node
def getTexture( node ):
    shadingGrps = cmds.listConnections(getShape( node ),type='shadingEngine')
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

# Stop ejecucution
def stop():
    sys.exit("Stoping")