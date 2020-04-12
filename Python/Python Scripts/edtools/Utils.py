import requests
import json
import os

# print object as a tree
def printo( o ):
	print( json.dumps( o , sort_keys=True, indent = 4 ) )

def beauty( o ):
	return json.dumps( o , sort_keys=True, indent = 4 )

# Print without a newline
def printc( str ):
	print( str, end='', flush=True)

# Print a list
def printl(list, separator = ""):
	for i in list:
		print(i)
		print(separator)


def stringToJson(data):
	obj = json.loads( data )
	return obj

def jsonToString( data ):
	str = beauty( data )
	return str

# Print Attributes inside obj
def getAttr(obj):
	print( dir( obj ) )

	

def createFolder( name ):
	if not os.path.exists( name ):
		os.makedirs( name )

def writeFile( data, file ):

	f = open( file, "w", encoding = "utf-8" )
	f.write( str( data ) )
	f.close()

def writeBinFile( data, file ):

	f = open( file, "wb" )
	f.write( data )
	f.close()

def getType(data):
	return type( data ).__name__

def downloadFile(url,dest):
	header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	file = requests.get( url, headers = header ).content
	writeBinFile(file,dest)

#-----------------------------------------
#           UTILS
#-----------------------------------------

def deleteFirst( termFrom, data ):
	result = data
	if data[:1] == termFrom:
		result = data[1:]
	return result

def deleteLast( termFrom, data ):
	result = data
	if data[-1:] == termFrom:
		result = data[:-1]
	return result

def getNameExt(data):
	splitData = data.split(".")
	ext = splitData[-1:][0]
	name = ".".join(splitData[:-1])
	return name, ext







