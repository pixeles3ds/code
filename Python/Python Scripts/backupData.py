import shutil
import errno
import os


baseDest = "D:/_Diario/codigo/"

def copy(src, dest):

	# Delete '/' from folders path string
	src = fixFolderPath(src)
	dest = fixFolderPath(dest)

	if( isFolder(src) ):
		folderName = os.path.basename( src )
		dest = dest + "/" + folderName	
		try:
			if os.path.exists(dest):
				shutil.rmtree(dest)
			shutil.copytree(src, dest)		
		except OSError as e:
			# If the error was caused because the source wasn't a directory
			if e.errno == errno.ENOTDIR:
				shutil.copy(src, dest)
			else:
				print('Directory not copied. Error: %s' % e)
		print( dest )
	else:
		createFolder(dest)
		shutil.copy(src, dest)
		print( dest +"/"+ os.path.basename( src ) )
		

def copyList(lista,src,dst):
	for obj in lista:
		copy( src + obj, dst )		


def createFolder( name ):
	if not os.path.exists( name ):
		os.makedirs( name )

def isFolder(path):
	if os.path.isdir(path): 
		return True

def fixFolderPath(path):
	if( path[-1:] == "/" ): return path[:-1]
	else: return path

def p(msg):
	print( "\n"+"-"*30+"\n"+msg+"\n"+"-"*30 )



#---------------------------------------------------------
# Copying this file itself
#---------------------------------------------------------

src = "C:/Users/Edwin/Desktop/backupData.py"
dst = baseDest + "Python/Python Scripts/"

p("This File Itself")
copy(src,dst)


#---------------------------------------------------------
# Copying Maya Files
#---------------------------------------------------------

src = "C:/Users/Edwin/Documents/maya/2016/scripts/"
dst = baseDest + "Python/Maya/scripts/"
lista = [
	"edTools.py",
	"Maya2CSS3D.py",
	"Maya2CSS3D"
	]

p("Maya")
copyList(lista,src,dst)


input()