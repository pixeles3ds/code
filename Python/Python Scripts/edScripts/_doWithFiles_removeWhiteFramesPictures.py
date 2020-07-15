import os, shutil, cv2
import numpy as np
import argparse

def removePictureFrame( path, ext ):

	# Load image, grayscale, Otsu's threshold 
	image = cv2.imread(path)
	original = image.copy()
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	
	
		
	thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]	

	# Find contours, obtain bounding box, extract and save ROI
	ROI_number = 0	
	cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = cnts[0] if len(cnts) == 2 else cnts[1]
	lst_contours = []
	for c in cnts:
	
		ctr = cv2.boundingRect(c)
		lst_contours.append(ctr)
		
		x,y,w,h = ctr
		cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)		
	
	
	x,y,w,h = sorted(lst_contours, key = lambda coef: coef[3])[-1]	
	result = original[y:y+h, x:x+w]
	cv2.imwrite( path, result)
	
	
	#cv2.imshow('image', thresh );cv2.waitKey();
	#cv2.imshow('image', result );cv2.waitKey();	
	#cv2.imshow('image', result );cv2.waitKey();
	
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
