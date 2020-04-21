import os
from edtools import *


def getFilesAndDo():

	path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"
	files = [f for f in os.listdir('.') if os.path.isfile(f)]

	for f in files:
		name, ext = getNameExt(f)
		fullPath = path + name + "." + ext
		
		do( fullPath, path, name, ext )


		
def do( fullPath, path, name, ext ):
	
	if ext in "mp4":
		replace = {
			"path":path,
			"name":name,
			"nameOut":name.replace(" new", "").replace("new",""),
			"ext":ext
		}
		command = 'ffmpeg -i "{path}{name}.{ext}" -vn -acodec copy "{path}{nameOut}.aac"'.format( **replace )
		print( "\n" + command + "\n" )
		os.system( command )
		
		# deleting new from input file
		os.rename( fullPath , fullPath.replace(" new", "").replace("new","") )


	
getFilesAndDo()

input("\n\n\nDone!!!\n\n\n")