import shutil
import errno
import os


'''
To ignore files or folders:
	
	'file.pyc' 	= Exacly the file
	'folder'	= Exacly the folder
	'*.pyc'		= Files with specific extension 
	'folder*'	= Folder with a string

	copy(src,dst, ignoreFiles = [ "*.pyc", "file.py", "Maya2CSS3D", "*lder" )

'''

gitBackup = "D:/_Diario/codigo/Python/"

def copy(src, dest, ignoreFiles = False ):

	def createFolder( name ):
		if not os.path.exists( name ):
			os.makedirs( name )

	def isFolder(path):
		if os.path.isdir(path): 
			return True

	def fixFolderPath(path):
		if( path[-1:] == "/" ): return path[:-1]
		else: return path


	# Delete '/' from folders path string
	src = fixFolderPath(src)
	dest = fixFolderPath(dest)

	if( isFolder(src) ):
		folderName = os.path.basename( src )
		dest = dest + "/" + folderName	
		try:
			if os.path.exists(dest):
				shutil.rmtree(dest)
			if(ignoreFiles):
				shutil.copytree(src, dest, ignore = shutil.ignore_patterns( *ignoreFiles ) )				
			else:
				shutil.copytree(src, dest )
		except OSError as e:
			# If the error was caused because the source wasn't a directory
			if e.errno == errno.ENOTDIR:
				shutil.copy(src, dest)
				print(src)
			else:
				print('Directory not copied. Error: %s' % e)
		print( dest )
	else:
		createFolder(dest)
		shutil.copy(src, dest)
		print( dest +"/"+ os.path.basename( src ) )
		


def p(msg):
	print( "\n"+"-"*30+"\n"+msg+"\n"+"-"*30 )



#---------------------------------------------------------
# Copying this file itself
#---------------------------------------------------------

p("This File Itself")
copy(
	"C:/Users/Edwin/Desktop/backupData.py",
	gitBackup + "Python Scripts/"
	)

#---------------------------------------------------------
# Copying PYTHON scripts
#---------------------------------------------------------

p("Python Scripts")
copy(
	"C:/Python36/Scripts/edScripts",
	gitBackup + "Python Scripts/"
	)

#---------------------------------------------------------
# Copying PYTHON scripts
#---------------------------------------------------------

p("Wordpress Installator")
copy( "C:/xampp/htdocs/index.php","D:/_Diario/Codigo/Wordpress/Fast WP Copier on xampp/")
copy( "C:/xampp/htdocs/wp_creator.php","D:/_Diario/Codigo/Wordpress/Fast WP Copier on xampp/")


#---------------------------------------------------------
# Copying Maya Files
#---------------------------------------------------------

p("Maya")
copy(
	"C:/Users/Edwin/Documents/maya/2020/prefs/scripts/edTools/",
	gitBackup + "Maya/scripts/",
	ignoreFiles = [ "*.pyc" ] 
	)


input()