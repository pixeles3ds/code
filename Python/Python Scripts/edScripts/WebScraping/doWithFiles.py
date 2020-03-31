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

	print( fullPath)
	print( path, " - ", name, " - ", ext )


	
getFilesAndDo()
input()