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
	
	if ext == "mkv":
		replace = {
			"path":path,
			"name":name,
			"ext":ext
		}
		command = 'C:/Users/Edwin/Desktop/mkv/StaxRip-x64-2.0.2.0-stable/Apps/Encoders/NVEnc/NVEncC64.exe --avhw cuda --output-thread 1 --cuda-schedule spin --preset performance --vbr 1000 -i "{path}{name}.{ext}" --audio-copy 1 -o "{path}{name}.mp4"'.format( **replace )
		print( "\n" + command + "\n" )
		os.system( command )


	
getFilesAndDo()

input("\n\n\nDone!!!\n\n\n")

