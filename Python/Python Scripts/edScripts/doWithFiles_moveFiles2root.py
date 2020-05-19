import os, shutil


def getFilesAndDo():

	def getNameExt(data):
		path = "/".join( data.split("/")[:-1] )+"/"
		data = data.split("/")[-1:][0]
		splitData = data.split(".")
		ext = splitData[-1:][0]
		name = ".".join(splitData[:-1])		

		return path, name, ext

	def failed(exc):
	    raise exc

	filesResult = []

	path = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"	
	
	for dirpath, dirs, files in os.walk( path, topdown=True, onerror=failed):	
		for file in files:
			
			fullPathFile = dirpath+"/"+file
			fullPathFile = fullPathFile.replace("//","/").replace("\\","/")
			filesResult.append( fullPathFile )


	for f in filesResult:
		basePath, name, ext = getNameExt(f)				
		do( f, basePath, name, ext )

		
def do( fullPath, basePath, name, ext ):

	currentPath = os.path.dirname(os.path.abspath(__file__)).replace("\\","/")+"/"	

	if not basePath == currentPath:				
		shutil.move(fullPath, currentPath ) 
		print( name+"."+ext )
			


try:
	getFilesAndDo()
except BaseException as e:    
    print e

input("\n\n\nDone!!!\n\n\n")