import shutil
import fnmatch
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

def copy(src, dest, ignoreFiles = False, onlyFiles = False ):

	def createFolder( name ):
		if not os.path.exists( name ):
			os.makedirs( name )

	def isFolder(path):
		if os.path.isdir(path): 
			return True

	def fixFolderPath(path):
		if( path[-1:] == "/" ): return path[:-1]
		else: return path

	def include_patterns(*patterns):
		""" Function that can be used as shutil.copytree() ignore parameter that
		determines which files *not* to ignore, the inverse of "normal" usage.

		This is a factory function that creates a function which can be used as a
		callable for copytree()'s ignore argument, *not* ignoring files that match
		any of the glob-style patterns provided.

		"patterns" are a sequence of pattern strings used to identify the files to
		include when copying the directory tree.

		Example usage:

			copytree(src_directory, dst_directory,
					 ignore=include_patterns('*.sldasm', '*.sldprt'))
		"""
		def _ignore_patterns(path, all_names):
			# Determine names which match one or more patterns (that shouldn't be
			# ignored).
			keep = (name for pattern in patterns
							for name in fnmatch.filter(all_names, pattern))
			# Ignore file names which *didn't* match any of the patterns given that
			# aren't directory names.
			dir_names = (name for name in all_names if os.path.isdir(os.path.join(path, name)))
			return set(all_names) - set(keep) - set(dir_names)

		return _ignore_patterns

		
		
	# Delete '/' from folders path string
	src = fixFolderPath(src)
	dest = fixFolderPath(dest)

	if( isFolder(src) ):
		folderName = os.path.basename( src )
		dest = dest + "/" + folderName	
		try:
		
			if os.path.exists(dest):
				shutil.rmtree(dest)			
				
			if onlyFiles:
				shutil.copytree(src, dest, ignore = include_patterns( *onlyFiles ) )
			elif ignoreFiles:
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
# Nuke Files
#---------------------------------------------------------

p("Nuke Scripts")
copy("C:/Nuke/", "D:/_Diario/codigo/", ignoreFiles = [ "*.exr", "*.hdr", "*.nk~", "*.autosave" ] 	)

#---------------------------------------------------------
# FFMPEG Scripts
#---------------------------------------------------------

p("ffmpeg Scripts")
copy("C:/ffmpeg/", gitBackup + "Python Scripts/", onlyFiles = [ "*.py","*.bat" ])

#---------------------------------------------------------
# Copying PYTHON scripts
#---------------------------------------------------------

p("Python Scripts")
copy("C:/Python36/Lib/site-packages/edtools", gitBackup + "Python Scripts/", ignoreFiles = [ "*.pyc" ] 	)
copy("C:/Python36/Scripts/edScripts", gitBackup + "Python Scripts/", ignoreFiles = [ "*.pyc" ] 	)


#---------------------------------------------------------
# CodeIgniter App
#---------------------------------------------------------

p("CodeIgniter App")
copy( "C:/xampp/htdocs/ciDoth/","D:/_Diario/Portfolio/PHP/codeigniter/")

copy( "C:/xampp/htdocs/ciDoth/application","D:/_Diario/Codigo/php/codeigniter/")
copy( "C:/xampp/htdocs/ciDoth/DB.sql","D:/_Diario/Codigo/php/codeigniter/")
copy( "C:/xampp/htdocs/ciDoth/ci-installer.php","D:/_Diario/Codigo/php/codeigniter/")


#---------------------------------------------------------
# Copying Wordpress scripts
#---------------------------------------------------------

p("Wordpress Installator")
copy( "C:/xampp/htdocs/index.php","D:/_Diario/Codigo/Wordpress/Fast WP Copier on xampp/")
copy( "C:/xampp/htdocs/wp_creator.php","D:/_Diario/Codigo/Wordpress/Fast WP Copier on xampp/")




#---------------------------------------------------------
# Copying Maya Files
#---------------------------------------------------------

p("Maya")
#copy( "C:/Users/Edwin/Documents/maya/scripts/userSetup.mel","D:/_Diario/Codigo/Python/Maya/scripts")
copy(
	"C:/Users/Edwin/Documents/maya/scripts/edToolsMaya/",
	gitBackup + "Maya/scripts/",
	ignoreFiles = [ "*.pyc" ] 
	)



input()