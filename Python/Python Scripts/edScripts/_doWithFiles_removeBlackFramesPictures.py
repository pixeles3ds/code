import os, shutil, cv2
import numpy as np

def removePictureFrame( path, ext ):

	img = cv2.imread( path )
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	_,thresh = cv2.threshold(gray,15,255,cv2.THRESH_BINARY)

	contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	# get contours with highest height
	lst_contours = []
	for cnt in contours:
		ctr = cv2.boundingRect(cnt)
		lst_contours.append(ctr)
	x,y,w,h = sorted(lst_contours, key=lambda coef: coef[3])[-1]

	offset = 0
	x,y,w,h = (x+offset,y+offset,w-offset*2,h-offset*2)

	crop = img[y:y+h,x:x+w]	
	cv2.imwrite( path, crop )
	
	#cv2.imshow('img',crop)
	
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
	
	if ext.lower() in ("jpg","jpeg","png"):	
		removePictureFrame( fullPath, ext )
		print(fullPath)



try:
	getFilesAndDo()
except BaseException as e:    
    print(e)

input("\n\n\nDone!!!\n\n\n")