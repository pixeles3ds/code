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
	
	if ext == "mov":
		replace = {
			"path":path,
			"name":name,
			"ext":ext
		}
		command = 'ffmpeg -i "{path}{name}.{ext}" -c:v copy -c:a copy "{path}{name}.mkv"'.format( **replace )
		print( "\n" + command + "\n" )
		os.system( command )


	
getFilesAndDo()

input("\n\n\nDone!!!\n\n\n")