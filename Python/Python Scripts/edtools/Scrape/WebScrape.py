import requests
import os
import sys
import hashlib
import time
import json
import re

from bs4 import BeautifulSoup
import jsbeautifier

from browsermobproxy import Server


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



import urllib.request
from shutil import copyfile
from urllib.parse import urlparse
from edtools.Tools import EdTree
from edtools import *

class WebScrape:

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	def __init__( self, url = "", root = "C:/xampp/htdocs/webscrape/", folder = "", srcFolder = "", rewriteIMG = 1, rewriteFiles = 1, downloadFiles = 1, createFolders = 1, createExt = 0 ):

		self.urlDomain = url
		self.rootDomain = self.getDomainUrl(url)
		self.root = root + folder + "/"
		self.srcFolder = srcFolder

		self.code = ""
		self.codeFixed = ""

		self.resources = {}
		self.fixResources = []
		self.downloadsLog = {}
		self.filePathByUrl = {}
		self.referersList = {}
		self.resultFoldersReference = {}
		self.requestCallers = {}

		self.data = { "js": [], "css": [] }
		self.rewriteIMG = rewriteIMG
		self.rewriteFiles = rewriteFiles

		self.downloadFiles = downloadFiles
		self.createFolders = createFolders
		self.createExt = createExt

		#Create folder if not exist
		self.createFolder( root + folder )







	#------------------------------------------------------
	#	Getters
	#------------------------------------------------------
	# Download the html code
	def getHtmlCode( self, url):

		self.urlDomain = url
		self.rootDomain = self.getDomainUrl( url )

		print("Downloadidng Code... ")

		try:
			self.code = requests.get(url, headers = self.headers).text
			self.makeSoup()
			return self.code

		except requests.exceptions.Timeout as e:
			print("Error Timeout: ", e)
		except requests.exceptions.ConnectionError as e:
			print ("Error Connecting: ",e)
		except requests.exceptions.TooManyRedirects as e:
			print("Error, too many redirects", e)
		except requests.exceptions.HTTPError as e:
			print("Http Error", e)
		except requests.exceptions.RequestException as e:
			# catastrophic error. bail.
			print(e)
			sys.exit(1)



	def getFileData(self, url, typeFile, mime = "" ):

		fixResource = 0
		fixResourceName = ""

		baseDomainUrl = self.getDomainUrl(url) + "/"
		baseDomainUrlResult = self.resultFoldersReference[ baseDomainUrl ]
		data = url.replace( baseDomainUrl, baseDomainUrlResult )

		parts = data.split("/")

		folders =  self.root + '/'.join( parts[:-1]) + "/"
		newName = parts[-1:][0]



		# -----------------------------------------------
		# if there is a ? on url, delete it
		# -----------------------------------------------
		if "?" in newName:
			newName = newName.split("?")[0]



		#------------------------------------------------
		#       If file is on external server
		# -----------------------------------------------

		if self.urlDomain not in url: # External server

			# ---------------------------------------------------------------------
			# if file does not has name, create a md5 name according to url
			# ---------------------------------------------------------------------
			if newName == "":


				newName = hashlib.md5(url.encode()).hexdigest() + self.getExtFromMime( mime )
				fixResourceName += " No name binary,"
				fixResource = 1


			# ---------------------------------------------------------------------
			# if file name not has extension
			# ---------------------------------------------------------------------

			if not self.hastExtension( newName ):
				if self.createExt:
					if typeFile in "img doc": # add extension only for docs and images
						extension = self.getExtFromMime( mime )
						newName = newName + extension
						fixResource = 1
						fixResourceName += " No extension, "


		else: # own server
			pass





		# ------------------------------------------------------
		# IF there are things to fix
		# ------------------------------------------------------
		if fixResource:
			srcLink = folders.replace( self.root, "" ) + newName # convert to relative path for html src linking
			self.fixResources.append({
				"url" : url,
				"localfile" : srcLink,
				"error" : fixResourceName,
				"mime" : mime,
				"referer": self.getRefererByUrl( url )
			} )

		return (folders, newName)

		#--------------------------------------------------------------------------------------------------------------





		fixResource = 0
		fixResourceName = ""

		# get the url root ej: "https://pcgames-download.com/"
		urlRoot = self.getDomainUrl(url)


		modURL = url.replace( urlRoot ,"") # delete rootDomain to url
		array = modURL.split("/")
		array = list(filter(lambda a: a != "", array )) # deleting empty folders
		array.insert(0, "") # Giving empty space ath the begin to add a "/" before relative path


		folders = self.root + '/'.join( array[:-1] ) + "/"
		filename = array[-1:][0]
		newName = filename


		#------------------------------------------------
		#       If file is on external server
		# -----------------------------------------------

		if self.urlDomain not in url:
			fixResourceExternalServer = self.getDomainUrl(url)
			fixResource = 1
			fixResourceName += " External server,"

		# ------------------------------------------------------
		# if file is not inside folder, create one folder
		# ------------------------------------------------------

		if len(array) < 3:
			if self.createFolders:
				self.createFolder( self.root + typeFile )
				folders = self.root + "/" + typeFile + "/"
				fixResource = 1
				fixResourceName += " No folder,"

		# -----------------------------------------------
		# if there is a ? on url, delete it
		# -----------------------------------------------

		if "?" in filename:
			newName = filename.split("?")[0]
			#fixResource = 1
			#fixResourceName += " ? params,"




		# ---------------------------------------------------------------------
		# if file name not has extension
		# ---------------------------------------------------------------------

		if not self.hastExtension( newName ):
			if self.createExt:
				extension = self.getExtFromMime( mime )
				newName = newName + extension
				fixResource = 1
				fixResourceName += " No extension, "


		# ---------------------------------------------------------------------
		# if file already exist and not has extension, file overwritting folder
		# ---------------------------------------------------------------------

		if not self.hastExtension(newName):
			if os.path.isdir( folders + newName ): # If path is a folder
				newName = hashlib.md5(url.encode()).hexdigest()
				fixResource = 1
				fixResourceName += " File instead folder, "


		# ------------------------------------------------------
		# IF there are things to fix
		# ------------------------------------------------------
		if fixResource:
			srcLink = folders.replace( self.root, "" ) + newName # convert to relative path for html src linking
			self.fixResources.append( { "url" : url, "localfile" : srcLink, "error" : fixResourceName, "mime" : mime } )


		return ( folders, newName )

	def getRefererByUrl( self, url ):

		refList = self.referersList

		for parent in refList:
			for link in refList[ parent ]:
				if url == link:
					if parent == "none":
						parent = self.rd()
					return parent


	def getDomainUrl(self, url):
		data = urlparse( url )
		return data.scheme + "://" + data.netloc

	# return the root domain
	def rd( self ):
		return self.rootDomain + "/"

	def getSoup(self):
		return self.soup

	def getCode(self):
		return self.code

	def getCodeFromSoup(self):
		return self.getSoup()



	#---------------------------------
	# Resoruces Getters
	#---------------------------------


	def getLinks(self, tag, attr ):


		result = []
		tags = self.soup.findAll( tag )

		for tag in tags:
			if tag.has_attr( attr ):
				link = self.relativeToFull( tag[ attr ] )
				result.append( link )

		return result


	def getJS(self):
		result = self.getLinks( "script", "src" )
		self.resources["js"] = result
		return result

	def getIMG(self):
		result = self.getLinks("img","src")
		self.resources["img"] = result
		return result

	def getResources(self):

		self.getJS()
		self.getIMG()

	# Load resources JSON log from HDD
	def loadResourcesFromJson( self ):

		path = self.root + "logs/resources.json"
		data = json.loads( self.readFile( path) ) # JSON String to Python Obj
		self.setResources(data)

		print( "\n[ ! ] Resources Loaded" )

	# Load resources JSON log from HDD
	def loadCodeHtml( self, url ):

		path = self.root + "indexOriginal.html"

		if os.path.isfile( path ):
			data = self.readFile( path )
			self.setCode( data, url )
			print( "\n[ ! ] HTML Loaded" )
		else:
			print( "[ ! ] File NO exist: " + path )

		self.makeSoup()



	def urlDeleteFile( self, data):
		dataSplit = data.split("/")
		data = "/".join(dataSplit[:-1]) + "/"
		return data

	def urlGetBase( self, data):
		data = data.replace("http://", "#@@#").replace("https://", "#@@@#")
		data = data.split("/")[0] + "/"
		data = data.replace("#@@#","http://").replace("#@@@#", "https://")
		return data

	def urlToRelative( self, data):
		return data.replace("https://", "").replace("http://", "")


	def fixFoldersByReferers(self):


		print("\n Fixing Folder Tree...")


		har = self.readFile( self.root + "logs/har.json" )
		har = stringToJson( har )


		#--------------------------------------------------------------------
		#  Getting the referers list
		# --------------------------------------------------------------------
		referersList = {}

		for req in har:

			headers = req["request"]["headers"]
			url = req["request"]["url"]
			referer = ""

			for val in headers:
				if val["name"] == "Referer":
					referer = val["value"]
					break

			if referer == "":
				referer = "none"

			if referer in referersList: # Already exist

				exist = 0
				for urlItem in referersList[ referer ]:
					if url == urlItem:
						exist = 1
						break

				if not exist:
					referersList[ referer ].append( url )

			else: # First time
				referersList[referer] = [url]





		# --------------------------------------------------------------------
		#  Getting dictinoary with parents folders
		# --------------------------------------------------------------------


		baseFoldersReferencesList = {}  # dict with the baseDomain and his father domain

		# Adding the root domain to the folders reference
		baseFoldersReferencesList[ self.rd() ] = ""
		for parent in referersList:


			linksList = referersList[parent]

			parent = self.urlDeleteFile(parent)

			baseParent = self.urlGetBase( parent )

			# Add rootDomain to folders with parent = "/"
			if baseParent == "/":
				baseParent = self.urlDomain + "/"


			for linkItem in linksList:

				linkItemPathBase = self.urlGetBase( linkItem )

				# if parent domain is not in actual link request
				if not baseParent in linkItem:

					# Give "/" parent to root domain
					if linkItemPathBase == self.urlDomain + "/":
						baseParent = "/"

					baseFoldersReferencesList[ linkItemPathBase ] = baseParent



		#-----------------------------------------------------
		# REORGANIZE FOLDERS BY TREE
		# -----------------------------------------------------

		foldersTree = baseFoldersReferencesList.copy()
		for key in foldersTree:
			foldersTree[ key ] = {}

		tree = EdTree.Tree()
		tree.setTree(foldersTree)


		# Moving folders on tree
		pDict = baseFoldersReferencesList
		for key in pDict:
			tree.move( key, pDict[ key ] )



		deleteTerms = [ self.rd() ] #  deleting rootDomain from paths results
		resultFoldersReference = tree.getFullPath( deleteTerms = deleteTerms )


		treeMap = tree.printTree()

		self.referersList = referersList
		self.resultFoldersReference = resultFoldersReference



		self.saveLogTreeMap( treeMap )
		self.saveLogRequestSources()
		self.saveLogFoldersreferersList()










	#------------------------------------------------------
	#	Soup
	#------------------------------------------------------

	def makeSoup( self ):
		self.soup = BeautifulSoup( self.codeFixed, 'html.parser')
		self.soupOrig = BeautifulSoup( self.code, 'html.parser')


	def resetSoup( self ):
		print("\nReseting to Original Soup... \n")
		self.soup = BeautifulSoup( self.code, 'html.parser')

	#------------------------------------------------------
	#	Setters
	#------------------------------------------------------

	def setSoup( self, soup ):
		self.soup = soup

	def setCode( self, code, url ):
		self.code = code
		self.codeFixed = code
		self.urlDomain = url
		self.rootDomain = self.getDomainUrl( url )

		self.writeHtml(self.code, self.root, "indexOriginal.html") # SAVING ORIGINAL CODE ON DISK

		self.makeSoup()

	def setResources(self, data):
		self.resources = data
		self.saveLogResources()

	def setFixResources(self, data):
		self.fixResources = data

	def setDownloadedFiles(self, data):
		self.downloadsLog = data


	#------------------------------------------------------
	#	Utils
	#------------------------------------------------------

	def beautyCSS( self, data ):

		data = re.sub(' +', ' ', data)
		data = data.replace(";", ";\n")
		data = data.replace("}", "\n}\n")
		data = data.replace("{", "{\n")

		dataSplit = data.split("\n")

		counter = 0
		for i, line in enumerate(dataSplit):

			if "}" in line: counter = counter - 1
			dataSplit[i] = "\t" * counter + line
			if "{" in line: counter = counter + 1

		data = "\n".join(dataSplit)

		return data


	def beautyJS(self, data):
		return jsbeautifier.beautify(data)

	def beautyHTML( self, data ):

		if type(data).__name__ == "str":
			soup = BeautifulSoup(data, 'html.parser')
		else:
			soup = data

		# -------------------------------------------
		#  Javascript
		# -------------------------------------------
		scripts = soup.findAll('script')
		for tag in scripts:
			data = self.beautyJS(tag.text)
			if len(data) > 5:
				data = "\n" + data
				data = data.replace("\n", "\n\t\t")

				tag.string = data

		# -------------------------------------------
		#  CSS
		# -------------------------------------------
		styles = soup.findAll('style')
		for tag in styles:
			data = self.beautyCSS(tag.text)
			data = data.replace("\n", "\n\t\t")

			tag.string = data

		return soup.prettify()






	def makeCopyBackup( self ):

		print("\nMaking Backup of Files")

		listType = ("css","doc","js")
		downList = self.downloadsLog
		root = self.root

		for typeFile in  listType:
			filesList = downList[ typeFile ]
			for file in filesList:
				file = file[1]
				folderPath, fileName = self.getFolderAndName( file )
				if not os.path.exists( root + folderPath + "original_" + fileName ):
					copyfile( root + file, root + folderPath + "original_" + fileName )

		print("\n[ ! ] Backup Files Done")










	def beautyWeb(self):


		print("\nBeautifying Files...\n")

		listType = ("css","doc","js")
		downList = self.downloadsLog
		root = self.root

		for typeFile in  listType:
			filesList = downList[ typeFile ]
			for file in filesList:
				file = root + file[1]
				fileRewrite = file

				folderPath, fileName = self.getFolderAndName( file )
				if os.path.exists( folderPath + "original_" + fileName ):
					file = folderPath + "original_" + fileName


				data = self.readFile( file )


				size = sys.getsizeof(data)/1024
				if size < 1024:
					if typeFile == "css":
						data = self.beautyCSS( data )
					elif typeFile == "js":
						data = self.beautyJS( data )
					elif typeFile == "doc":
						data = self.beautyHTML( data )

					writeFile( data, fileRewrite )



		self.codeFixed = self.beautyHTML( self.codeFixed )


		print("\n[ ! ] Beauty Files Done")


	def fixResourcesChanges( self ):

		def findInQotation( term, data ):



			result = 0

			termTmp = '"' + term + '"'
			if termTmp in data:
				return termTmp

			termTmp = "'" + term + "'"
			if termTmp in data:
				return termTmp

			return result


		def errorFixed( url, fix, refer, i, data, path ):

			data = data.replace(url, fix)
			folder,name = self.getFolderAndName(path)

			# if request was made from index.html
			if refer == self.rd():
				self.codeFixed = data
			else:
				self.writeFile( data, folder, name, "doc" )

			del self.fixResources[i]

			print("<<< ! >>> ERROR: " + url)
			print("          Fixed: " + fix)
			print("          Refer: " + refer + "\n")


		for i,error in enumerate(self.fixResources):


			fix = error["localfile"]
			errorType = error["error"]
			url = error["url"]
			refer = error["referer"]

			term = url#.replace("http:","").replace("https:","")

			# if request was made from index.html
			if refer == self.rd():
				path = self.root + "index.html"
				data = self.codeFixed
			else:
				path = self.root + self.filePathByUrl[ url ]["path"]
				data = self.readFile( path )


			#url = self.urlToRelative( url )
			#if "?" in url:
				#url = url.split("?")[0]

			#------------------------------------------------------
			#       Algorithm Find and Fix errors on docs
			# ------------------------------------------------------


			# Deleting multple withe spaces and delete white space around quotation marks
			data = re.sub(' +', ' ', data ).strip()
			data = data.replace(' "', '"').replace('" ', '"')
			data = data.replace(" '", "'").replace("' ", "'")



			# Original term inside "quotations"
			termTmp = findInQotation( term, data )
			if termTmp:
				quot = termTmp[:1]
				fixTmp= quot + fix + quot
				errorFixed( termTmp, fixTmp, refer, i, data , path)
				continue

			# term without last / inside "quotations"
			termTmp0 = deleteLast("/", term ) # Test without last /
			termTmp = findInQotation( termTmp0, data )
			if termTmp:
				quot = termTmp[:1]
				fixTmp = quot + fix + quot
				errorFixed( termTmp, fixTmp, refer, i, data , path )
				continue

			# term without parameter but with ?
			if "?" in url:
				termTmp = term.split("?")[0] + "?"

				if termTmp in data:
					fixTmp = fix + "?"
					errorFixed( termTmp, fixTmp, refer, i, data , path)
					continue


		self.saveLogFixResources()
		self.saveHtml()



	def convertWEbToLocal(self):

		def makeRequestCallers():

			requestCallers = self.referersList
			result = {}
			# get requests callers
			for parent in requestCallers:
				if parent == "none": parent = self.rd()
				if not parent == self.rd():
					filePathData = {
						"path": self.filePathByUrl[ parent ]["path"],
						"mime": self.filePathByUrl[ parent ]["mime"]
					}
					result[ parent ] = filePathData

			self.requestCallers = result


		def changeCssRelativePos():

			cssList = self.downloadsLog["css"]
			for cssFile in cssList:

				posNumber = cssFile[3]
				path = self.root + cssFile[1]
				folder,name = self.getFolderAndName( path )

				data = self.readFile( path )

				data = data.replace( " (","(" ).replace( "( ","(" ).replace('" ','"')
				data = data.replace("url('/", "url('" + "../"*posNumber )
				data = data.replace('url("/', 'url("' + "../"*posNumber )
				data = data.replace("url(/", "url(" + "../"*posNumber )

				self.writeFile( data, folder, name, "css" )



		def toRelative( code, type = "" ):

			code = code.replace("https://","")
			code = code.replace("http://","")
			code = code.replace('"//','"')
			code = code.replace("'//","'")

			code = code.replace("crossorigin", "nothing")
			code = code.replace("integrity", "nothing2")


			if type == "doc":
				soup = BeautifulSoup(code, 'html.parser')

				for elm in soup():

					# -----------------------------------
					#       href
					# -----------------------------------
					if "href" in elm.attrs:
						val = elm.attrs["href"]
						val = deleteFirst("/", val )
						elm.attrs["href"] = val

					# -----------------------------------
					#       src
					# -----------------------------------
					if "src" in elm.attrs:
						val = elm.attrs["src"]
						val = deleteFirst("/", val )
						elm.attrs["src"] = val


				code = soup.prettify()

				code = code.replace('href="/','href="').replace("href='/","href='")


			elif type == "css":
				code = re.sub(' +', ' ', code ).strip()

			return code


		def getFileList():

			result = []
			downloadsList = self.downloadsLog

			for key in downloadsList:
				if key in "css js doc json":
					for item in downloadsList[ key ]:
						result.append( self.root + item[1][1:] )

			result.append( self.root + "indexOriginal.html") # Adding index html

			return result



		# ----------------------------------------------------------------------------------------------

		print("\nFixing to Relatives Urls\n")

		makeRequestCallers()

		files = getFileList()

		# Processing Pages who are doing requests
		for link in self.requestCallers:

			localPath = self.root + self.requestCallers[link]["path"]
			mimeFile = self.requestCallers[link]["mime"]

			data = self.readFile( localPath )
			data = toRelative( data, mimeFile )
			folderName = self.getFolderAndName( localPath )

			self. writeHtml(data, folderName[0], folderName[1] )


		# Fix css relative paths positions
		changeCssRelativePos()


		# Editing Index
		self.makeSoup()
		html = self.soup.prettify()
		#html = self.getCode()
		html = html.replace( self.rd(), "")
		html = toRelative( html, "doc" )

		self.codeFixed = html
		self.saveHtml()











	def getFolderAndName( self, path = "" ):
		pathSplit = path.split("/")
		name = pathSplit[-1:][0]
		folder = "/".join( pathSplit[:-1]) + "/"
		return ( folder, name )




	# convert relative urls to full
	def relativeToFull( self, url):
		if self.rootDomain in url:
			return url
		elif "//" in url:
			return url
		else:
			if not "/" in url[:1]: 
				url = "/" + url
			return self.rootDomain + url





	# convert full urls to relative
	def fullToRelative( self, data ):		
		return data.replace( self.rootDomain, self.srcFolder )

	def createFolder( self, name ):
		if name:
			if not os.path.exists( name ):
				os.makedirs( name )

	def hastExtension( self, name ):
		if "." in name: return 1
		else: return 0


	def getMime(self, url ):

		try:
			print(" Getting mimeType  ->  " + url)
			header = requests.head(url, allow_redirects=True, headers=self.headers)
			type = str(header.headers.get('content-type'))
			return type

		except requests.exceptions.Timeout as e:
			print("Error Timeout: ", e)
		except requests.exceptions.ConnectionError as e:
			print("Error Connecting: ", e)
		except requests.exceptions.TooManyRedirects as e:
			print("Error, too many redirects", e)
		except requests.exceptions.HTTPError as e:
			print("Http Error", e)
		except requests.exceptions.RequestException as e:
			# catastrophic error. bail.
			print(e)
			sys.exit(1)

	def getExtFromMime( self, mime ):

		extension = ""

		mime = mime.lower()

		if "jpeg" in mime: extension = "jpeg"
		elif "jpg" in mime: extension = "jpg"
		elif "png" in mime: extension = "png"
		elif "gif" in mime: extension = "gif"
		elif "ico" in mime: extension = "ico"
		elif "svg" in mime: extension = "svg"

		elif "woff2" in mime: extension = "woff2"
		elif "woff" in mime: extension = "woff"

		elif "html" in mime: extension = "html"
		elif "plain" in mime: extension = "txt"

		elif "css" in mime: extension = "css"
		elif "javascript" in mime: extension = "js"
		elif "json" in mime: extension = "json"

		return "."+extension

	def printResources( self ):
		return 0
		data = self.resources
		total = data["total"]

		del data["total"]

		for keys in data:

			print("="*40)
			print(keys)
			print("=" * 40)

			for item in data[keys]:
				print( item[1] + "  -  " + item[0]   )

		print("-" * 40)





	#------------------------------------------------------
	#	Writteners
	#------------------------------------------------------

	def writeHtml( self, data, folder, name ):

		f = open( folder + name, "w", encoding="utf-8")
		f.write( data )
		f.close()


	def writeFile( self, data, folder, name, fileType ):

		if fileType in "img font binary":
			f = open( folder + name, "wb")
			f.write( data )
			f.close()

		else:
			# if data is coming as a byte type of data decode to utf8 string
			if type(data).__name__ == "bytes":

				encodings = ['utf-8', 'cp1252', "ISO-8859-1" ]

				for e in encodings:
					try:
						data = data.decode( e )
					except UnicodeDecodeError:
						print('WriteFile: Got unicode error with %s , trying different encoding' % e)
					else:
						break


			f = open( folder + name, "w", encoding="utf-8")
			f.write( str( data ) )
			f.close()



			
	def readFile( self, pathFile ):
		f = open( pathFile, "r", encoding = "utf8" )
		data = f.read()
		f.close()
		return data



	#------------------------------------------------------
	#	Downloaders
	#------------------------------------------------------
	def downloadFile(self, url, typeFile, mime = "" ):

		def addDownloadToList(  url, folderFile, nameFile, typeFile ):

			logUrl = url
			logFile = folderFile.replace(self.root, "") + nameFile

			# adding downloaded files to file log
			if not typeFile in self.downloadsLog:
				self.downloadsLog[typeFile] = []

			dataInfo = [ logUrl, logFile, mime ]

			# get number of css locations move
			if typeFile == "css":
				folderTmp = folderFile.replace( self.root, "" )
				if self.urlDomain not in url:  # External server
					numberMoves = len(folderTmp.split("/")) - 2
				else: # own
					numberMoves = len(folderTmp.split("/")) - 1

				dataInfo.append( numberMoves )

			self.downloadsLog[ typeFile ].append( dataInfo )

			# adding the file path stored of a url
			filePathData = {
				"path": logFile,
				"mime": typeFile
			}
			self.filePathByUrl[logUrl] = filePathData

		
		def download( url, folderFile, nameFile, typeFile ):


			logUrl = url
			logFile = folderFile.replace(self.root, "") + nameFile

			self.createFolder(folderFile)

			if not self.downloadFiles:
				return 0
		
			try:
				print("--> Downloading: " + url )
				print("                 " + folderFile.replace( self.root, "" ) + nameFile)
				file = requests.get( url, headers = self.headers ).content
				self.writeFile(file, folderFile, nameFile, typeFile )

				if url in self.requestCallers:
					self.writeFile(file, folderFile, "Original_" + nameFile, typeFile)


	
			except requests.exceptions.Timeout as e:
				print("Error Timeout: ", e)
			except requests.exceptions.ConnectionError as e:
				print ("Error Connecting: ",e)
			except requests.exceptions.TooManyRedirects as e:
				print("Error, too many redirects", e)
			except requests.exceptions.HTTPError as e:
				print("Http Error", e)
			except requests.exceptions.RequestException as e:
				# catastrophic error. bail.
				print(e)
				sys.exit(1)
		
		
		
		folderFile, nameFile = self.getFileData( url, typeFile, mime )

		# Adding requests to download list
		addDownloadToList( url, folderFile, nameFile, typeFile)

		# if file already exist
		if os.path.isfile( folderFile + nameFile ):			
			if typeFile == "img" :
				if self.rewriteIMG: download( url, folderFile, nameFile, typeFile  )
			else:
				if self.rewriteFiles: download( url, folderFile, nameFile, typeFile  )
					
		else:			
			download( url, folderFile, nameFile, typeFile )





	def saveHtml( self, folder = "", name = "index.html" ):
		self.createFolder( self.root + folder )
		self.writeHtml( self.codeFixed, self.root + folder, name)
		self.writeHtml( self.code , self.root + folder, "indexOriginal.html")


	#===================================================================================

	def saveJS( self ):
		if "js" in self.resources:
			for link in self.resources["js"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "js" , mime = mime )
		else:
			print("No js links...")

	def saveJson( self ):
		if "json" in self.resources:
			for link in self.resources["json"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "json", mime = mime )
		else:
			print("No JSON links...")

	def saveCSS( self ):
		if "css" in self.resources:
			for link in self.resources["css"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "css" , mime = mime )
		else:
			print("No CSS links...")

	def saveFonts( self ):
		if "font" in self.resources:
			for link in self.resources["font"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "font" , mime = mime )
		else:
			print("No fonts links...")

	def saveDocs( self ):
		if "doc" in self.resources:
			for link in self.resources["doc"]:
				url = link[0]
				mime = link[1]
				if not self.rd() == url:
					self.downloadFile( url, typeFile = "doc"  , mime = mime )

		else:
			print("No documents links...")

	def saveBinaries( self ):
		if "binary" in self.resources:
			for link in self.resources["binary"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "binary", mime = mime )
		else:
			print("No binaries links...")

	def saveUnknown( self ):
		if "unknown" in self.resources:
			for link in self.resources["unknown"]:
				url = link[0]
				mime = link[1]
				self.downloadFile( url, typeFile = "unknown", mime = mime )
		else:
			print("No binaries links...")


	def saveImages( self ):
		
		if "img" in self.resources:

			for item in self.resources["img"]:
				url = item[0]
				mime = item[1]
				self.downloadFile( url, typeFile = "img" , mime = mime )

		else:
			print( "No images links..." )



	#====================================================================================

	def saveResources(self):

		self.fixResources = []
		self.downloadsLog = {}

		self.saveJS()
		self.saveJson()
		self.saveCSS()
		self.saveFonts()
		self.saveDocs()
		self.saveBinaries()
		self.saveImages()
		self.saveUnknown()

		self.saveLogResources()
		self.saveLogFixResources()
		self.saveLogFilesDownloaded()



	def saveLogTreeMap( self, data ):
		folder = self.root + "logs/"
		self.createFolder( folder )
		self.writeFile(  data , folder, "treeMap.txt", "json" )
		print( "\n[ ! ] LOG Tree Map Stored! " )

	def saveLogRequestSources( self ):
		folder = self.root + "logs/"
		self.createFolder( folder )
		self.writeFile( beauty( self.referersList ), folder, "requestSources.json", "json" )
		print( "\n[ ! ] LOG Requests Sources Stored! " )


	def saveLogFoldersreferersList( self ):
		folder = self.root + "logs/"
		self.createFolder( folder )
		self.writeFile( beauty( self.resultFoldersReference ), folder, "foldersReference.json", "json" )
		print( "\n[ ! ] LOG Folders Reference Stored! " )


	def saveLogResources( self ):
		folder = self.root + "logs/"
		self.createFolder( folder )
		self.writeFile( beauty( self.resources ), folder, "resources.json", "json" )
		print( "\n[ ! ] LOG Resources Stored! " )


	def saveLogFixResources(self):
		folder = self.root + "logs/"
		self.createFolder(folder)
		self.writeFile(beauty(self.fixResources), folder, "fixRsources.json", "json")
		print("\n[ ! ] LOG FIX Resources Stored! ")


	def saveLogFilesDownloaded(self):
		folder = self.root + "logs/"
		self.createFolder(folder)
		self.writeFile(beauty(self.downloadsLog), folder, "filesDownloaded.json", "json")
		print("\n[ ! ] LOG files downloaded Stored! ")

	def saveLogFixResults(self, data = "" ):
		folder = self.root + "logs/"
		self.createFolder(folder)
		if data == "":
			self.writeFile(beauty(self.fixResourcesResults), folder, "fixRsourcesResults.json", "json")
		else:
			self.writeFile( data, folder, "fixRsourcesResults.txt", "txt")

		print("\n[ ! ] LOG FIX Results Resources Stored! ")


	def saveWeb( self, folderHtml = "", nameHtml = "index.html" ):
				
		self.saveHtml( folderHtml, nameHtml )	
		self.saveImages()




class browseWeb:
	headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	def __init__( self, root = "C:/xampp/htdocs/webscrape/", folder = "" ):

		self.url = ""
		self.root = root + folder + "/"

		# Start browsermob proxy
		self.server = Server(r"C:\webdrivers\browsermob-proxy\bin\browsermob-proxy")
		self.server.start()
		self.proxy = self.server.create_proxy()

		# Setup Chrome webdriver - note: does not seem to work with headless On
		options = webdriver.ChromeOptions()
		options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
		options.add_argument( '--proxy-server=%s' % self.proxy.proxy)  # Setup proxy to point to our browsermob so that it can track requests


		self.w = webdriver.Chrome(r'C:/webdrivers/chromedriver.exe', chrome_options = options )
		self.proxy.new_har("Listener", options = { 'captureHeaders': True } )  # Request listener
		#self.proxy.new_har("Listener" )  # Request listener

		print("Browser and Server initialized...")





	
	#------------------------------------------------------
	#	GETTERS
	#------------------------------------------------------


	def getCode( self ):
		return self.w.page_source
		

	def getElement( self ):
		return self.element

	def getElements( self ):
		return self.elements


	def getElementCode( self,  element = None  ):

		if element: return element.get_attribute('outerHTML')
		else: return self.element.get_attribute('outerHTML')

	def getTypeParam( self, by ):

		byParam = None

		if by == "id": byParam = By.ID
		if by == "class": byParam = By.CLASS_NAME
		if by == "name": byParam = By.NAME
		if by == "tag": byParam = By.TAG_NAME
		if by == "text": byParam = By.PARTIAL_LINK_TEXT
		if by == "css": byParam = By.CSS_SELECTOR

		return byParam

	def getRequests(self):

		dataCollected = {}

		requestsList = {
			"js": [],
			"css": [],
			"img": [],
			"font": [],
			"json": [],
			"doc": [],
			"binary": [],
			"unknown": [],
			"total": {}
		}

		# Get list of All requests
		requestLog = self.proxy.har['log']["entries"]

		createFolder( self.root + "logs" )
		writeFile( data = beauty(requestLog), file = self.root + "logs/har.json" )
		print( "\n[ ! ] HAR Stored! " )

		for entry in requestLog:

			if 'request' in entry.keys():

				# Getting referers
				referer = ""
				headersList = entry['request']['headers']
				for item in headersList:
					if item["name"] == "Referer":
						referer = item["value"]


				url = entry['request']['url']

				obj = {
					"url": url,
					"type": entry['response']['content']['mimeType'],
					"size": entry['response']['bodySize'],
					"method": entry['request']['method'],
					"status": entry['response']['status'],
					"referer": referer
				}

				urlNew = url
				if "?" in url: urlNew = url.split("?")[0] # remove ? parameters from url

				dataCollected[ urlNew ] = obj

		# Clasifing resquests

		for key in dataCollected:
			type = dataCollected[key]["type"]
			url = dataCollected[key]["url"]
			referer = dataCollected[key]["referer"]
			status = str(dataCollected[key]["status"])

			# if status is available
			if not "204" in status:

				# Catching mymeType of empty mimeTypes or plain mime
				if type == "" or "plain" in type or "None" in type:

					try:
						print("--> (" + status + " - " + type +")Getting mimeType  ->  " + url )
						header = requests.head( url, allow_redirects = True, headers = self.headers  )
						type = str( header.headers.get('content-type') )
						print( "--> ( " + type + " )")

					except requests.exceptions.Timeout as e:
						print("Error Timeout: ", e)
					except requests.exceptions.ConnectionError as e:
						print("Error Connecting: ", e)
					except requests.exceptions.TooManyRedirects as e:
						print("Error, too many redirects", e)
					except requests.exceptions.HTTPError as e:
						print("Http Error", e)
					except requests.exceptions.RequestException as e:
						# catastrophic error. bail.
						print(e)
						sys.exit(1)



				if "image" in type:
					requestsList["img"].append( [ url, type ] )
				elif "css" in type:
					requestsList["css"].append( [ url, type ] )
				elif "font" in type:
					requestsList["font"].append( [ url, type ] )
				elif "javascript" in type:
					requestsList["js"].append( [ url, type ] )
				elif "json" in type:
					requestsList["json"].append( [ url, type ] )
				elif "html" in type or "plain" in type:
					requestsList["doc"].append( [ url, type ] )
				elif "octet-stream" in type:
					requestsList["binary"].append( [ url, type ] )
				else:
					requestsList["unknown"].append( [ url, type ] )


		# Counting resquests
		total = 0
		for key in requestsList:
			subtotal = len(requestsList[key])
			requestsList["total"][key] = subtotal
			total = total + subtotal

			requestsList["total"]["total"] = total

		self.request = requestsList

		return requestsList


	#------------------------------------------------------
	#	SETTERS
	#------------------------------------------------------

	def setUrl( self, url ):
		self.url = url

	def setElement( self, by, name ):

		byParam = self.getTypeParam( by )
		self.element = self.w.find_element( byParam, name )
		return self.element

	def setElements( self, by, name ):

		byParam = self.getTypeParam( by )
		self.elements = self.w.find_elements( byParam, name )
		return self.elements


	#------------------------------------------------------
	#	FUNCTIONS
	#------------------------------------------------------


	def browseURL(self,url):

		print("--> Loading web  ->  " + url)

		t = time.time()
		self.w.implicitly_wait(30)
		self.w.set_page_load_timeout(30)

		try:
			self.w.get(url)

		except TimeoutException:
			print("Error loading something")
			print('Time consuming:', time.time() - t)
			self.w.execute_script("window.stop();")


		print("--> Loaded... ")



	#-------------------------------------------------------

	def click( self, selector = "" ):
		if selector: self.w.find_element_by_css_selector( selector).click()
		else: self.element.click()

	def enter( self, selector = "" ):
		if selector: self.w.find_element_by_css_selector( selector).send_keys( Keys.ENTER  )
		else: self.element.send_keys( Keys.ENTER  )

	def text( self, selector = "", text = "" ):
		if selector: self.w.find_element_by_css_selector( selector).send_keys( text )
		else: self.element.send_keys( text )
		
	def exit(self):

		self.server.stop()
		print("Closed Proxy Server...")
		self.w.close()
		print("Closed Browser...")
		self.w.quit()
		print("Quited app...")

		# Killing java and webdriver process
		os.system("taskkill /f /im java.exe")
		os.system("taskkill /f /im chromedriver.exe")
		print("Process killed...")

	# -------------------------------------------------------

	def waitEnableItem( self, delay = 10 ):
		
		try:
			# wait for button to be enabled
			WebDriverWait( self.w, delay ).until( EC.element_to_be_clickable((By.ID, 'getData')) )
			button = self.w.find_element_by_id('getData')
			button.click()

		except TimeoutException:
			print('Loading took too much time!')
		else:
			#html = browser.page_source
			pass
		finally:
			#browser.quit()
			pass
			
	def waitLoadedItem( self, delay = 10, cssSelector = "" ):
		
		try:		
			# wait for data to be loaded
			# e.g:  cssSelector = '#dataTarget > div'
			WebDriverWait( self.w, delay).until( EC.presence_of_element_located(( By.CSS_SELECTOR, cssSelector )) )
		except TimeoutException:
			print('Loading took too much time!')
		else:
			#html = self.w.page_source
			pass
		finally:
			#browser.quit()
			pass



	# -------------------------------------------------------

	def command(self, data):

		library = {
			"1": "start",
			"2": "getrequests"
		}

		# getCode from library
		if data.isdigit():  # if the command is a number
			if data in library:  # if the number exist in the library
				data = library[data]

		if "start" in data:
			self.browseURL(self.url)

		elif "getrequests" in data:
			self.getRequests()
			print("-" * 30)
			printo(self.request)
			print("-" * 30)


		elif "click" in data:
			array = data.split(" ")
			if len(array) > 1:
				self.click(array[1])

		elif "getcode" in data:
			code = self.getCode()
			print(code)




