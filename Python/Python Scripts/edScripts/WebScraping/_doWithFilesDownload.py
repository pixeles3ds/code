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
	if ext != "py":
		url = "https://dahz.daffyhazan.com/kitring/wp-content/uploads/2019/02/"+name+"."+ext
		print( "downloading: "+url)
		#downloadFile(url,fullPath)
		


	
getFilesAndDo()
input("Finished")