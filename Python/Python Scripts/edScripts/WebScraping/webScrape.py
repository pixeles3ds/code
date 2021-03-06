import requests
import os
import sys
from urllib.parse import urlparse
from bs4 import BeautifulSoup


root = "c:/webscrape/pcgames-download.com/"



'''
====================================================

	System Methods

====================================================
'''


def printc( str ):
	print( str, end='', flush=True)


def printl(list):
	for i in list:
		print(i)


'''
====================================================

	CLASS WEB

====================================================
'''

class web:

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	def __init__(self, urlDomain = "", localPath = "",  code = "", soup = None ):

		self.urlDomain = urlDomain
		self.localPath = localPath
		self.code = code
		self.soup = soup 


	#------------------------------------------------------
	#	Soup
	#------------------------------------------------------

	def makeSoup( self ):
		print("Making Soup... ")
		self.soup = BeautifulSoup( self.code, 'html.parser')

	def resetSoup( self ):
		print("\nReseting to Original Soup... \n")
		self.soup = BeautifulSoup( self.code, 'html.parser')

	#------------------------------------------------------
	#	Setters
	#------------------------------------------------------

	def setSoup( self, soup ):
		self.soup = soup



	#------------------------------------------------------
	#	Getters
	#------------------------------------------------------

	def getHtmlCode( self, url):
		
		print("Downloadidng Code... ")
		
		try:			
			self.code = requests.get(url, headers = self.headers).text
			self.makeSoup()

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
		


	def getImgData(self, url):
		
		# get the url root ej: "https://pcgames-download.com/"
		urlRoot = self.getDomainUrl( url )

		url = url.replace( urlRoot ,"")
		array = url.split("/")
		folders = root +'/'.join( array[:-1] ) + "/"
		filename = array[-1:][0]
		
		if "?" in filename: 
			filename = filename.split("?")[0]

		return (folders,filename)


	def getDomainUrl(self, url):
		data = urlparse( url )
		return data.scheme + "://" + data.netloc + "/"


	def getSoup(self):
		return self.soup		

	def getCode(self):
		return self.code


	#------------------------------------------------------
	#	Utils
	#------------------------------------------------------


	def convertToLocal( self, data ):		
		return data.replace( self.getDomainUrl( self.urlDomain ), self.localPath )

	def createFolder( self, name ):
	    if not os.path.exists( name ):
	        os.makedirs( name )

	
	#------------------------------------------------------
	#	Downloaders
	#------------------------------------------------------

	def writeHtml( self, data, folder, name ):

		print("Saving HTML... ")

		data = self.convertToLocal( str( data ) )

		f = open( folder + name, "w", encoding="utf-8")
		f.write( data )
		f.close()


	def writeFile(self, url, folder, name ):
		
		print("--> Saving File: " + url)

		try:
			
			file = requests.get( url, headers = self.headers ).content			
			with open( folder + name ,"wb") as f:
				f.write( file )
				f.close()

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




	def saveHtml( self, folder, name ):
		self.createFolder( folder )		
		self.writeHtml( self.soup, folder, name)


	def saveImages( self ):			

		soupWrapper = self.soup.findAll("div", {"class": "wrapper"})[0]	

		for link in soupWrapper.select("img"):
			
			urlImg = link["src"]
			folderImg,fileName = self.getImgData(urlImg)			

			# If file not exist
			if not os.path.isfile(folderImg + fileName ):
				self.createFolder( folderImg )
				self.writeFile( urlImg, folderImg, fileName )


			
	def saveWeb( self, folderHtml, nameHtml ):
				
		downloadHtml( folderHtml, nameHtml )	
		downloadImages()

'''
====================================================

	END CLASS WEB

====================================================
'''



'''
====================================================

	CLASS pcGamesDownloads EXTEND Web

====================================================
'''

# Extend for https://pcgames-download.com/
class pcGamesPages(web):
	
	def __init__(self, urlDomain = "", localPath = ""):
		self.urlDomain = urlDomain
		self.localPath = localPath
	

	#------------------------------------------------------
	#	HTML EDITIONS
	#------------------------------------------------------

	def deleteTags( self ):
		
		print("Editing -> Deleting Tags... ")

		listDelete = []

		# Delete scripts tags, analytics and pops BY TEXT inside tag	
		listDelete.append( [self.soup.find(lambda tag:tag.name=="script" and "GoogleAnalyticsObject" in tag.text)] )
		listDelete.append( [self.soup.find(lambda tag:tag.name=="script" and "_pop" in tag.text)] )

		# Delete <link> TAG  google fonts CSS
		listDelete.append( self.soup.select("link[id=baskerville_googleFonts-css]") )	

		# Delete Content Layout
		listDelete.append( self.soup.findAll("h3", {"class": "blog-description"}) )
		listDelete.append( self.soup.findAll("div", {"class": "navigation"}) )
		listDelete.append( self.soup.findAll("div", {"class": "metaslider"}) )
		listDelete.append( self.soup.findAll("div", {"class": "sidebar"}) )
		listDelete.append( self.soup.findAll("div", {"class": "post-meta-container"}) )
		listDelete.append( self.soup.findAll("div", {"class": "comments"}) )
		listDelete.append( self.soup.findAll("iframe", {"id": "mgiframe"}) )
		listDelete.append( self.soup.findAll("div", {"class": "footer"}) )
		listDelete.append( self.soup.findAll("div", {"class": "credits"}) )
		listDelete.append( self.soup.findAll("div", {"class": "yarpp-related"}) )		
		listDelete.append( self.soup.findAll("img", {"class": "avatar"}) )

		
		# DELETING TAGS
		for listItems in listDelete:
			for tag in listItems:
				tag.decompose()




		

	def editNumNav( self ):

		print("Editing -> Changing numbers nav menu links... ")

		nav = self.soup.find("div", {"class": "wp-pagenavi"})	
		buttonsList = nav.findAll("a")

		for a in buttonsList:			

			if not "page" in a['href']:
				aUrl = root + "page1.html"
			else:
				aUrl = "page"+a['href'].split("/")[-2] + ".html"

			a['href'] = aUrl



	def editPostUrl( self ):
		
		print("Editing -> Changing post games links... ")

		postList = self.soup.find("div", {"class": "posts"})
		buttonsPosts = postList.findAll("a")

		for a in buttonsPosts:
			aUrl = a['href'][:-1] + ".html"
			a['href'] = aUrl
		
	

	#------------------------------------------------------
	#	Getters and Setters
	#------------------------------------------------------

	def getUrlPosts( self ):
		return self.soup.findAll("a", {"class": "more-link"})


	def setNumberPage( self, n):
		self.nPage = n

	
	#------------------------------------------------------
	#	Saving Posts
	#------------------------------------------------------

	def savePosts( self ):

		appPost = pcGamesPages( urlDomain = "https://pcgames-download.com/", localPath = "../../")

		pagesList = self.getUrlPosts()
		

		for gameUrlSrc in pagesList:

			gameUrl = gameUrlSrc["href"]			
			gameUrlData = gameUrl.replace("https://pcgames-download.com/","").split("/")
			
			folderPost = gameUrlData[0] + "/" + gameUrlData[1] + "/"
			namePost = gameUrlData[2] + ".html"
			
			print( "-"*30+"\n["+self.nPage+"] -> Downloading post: " + namePost)


			# Create another instance for post pages
			appPost.getHtmlCode( gameUrl )
			appPost.deleteTags()
			appPost.saveHtml( root + folderPost, namePost )	
			appPost.saveImages( )	

			print( "-"*30)



'''
====================================================

	END  CLASS PcGamesDownloads

====================================================
'''





def initCustomPcGames( ini, fin, mult):


	ini = ini
	fin = fin	


	def pInit():
		print("\n"*2 +"="*80+"\n" + "\n STARTED\n\n" + "="*80+ "\n" )
	
	def pEnd():
		print("\n"*5 + "="*80+"\n" + "\n END\n\n" + "="*80 + "\n")

	def pPage(str):
		print("\n"*3+"="*80+"\n" +  "Working page: " + str + "\n" + "="*80)



	def customSoup(soup):
		soupPosts = soup.find("div", {"class": "posts"})
		soupPosts.clear() # Delete content from sopupTag
		return soupPosts


	def appSinlePage():


		app = pcGamesPages( urlDomain = "https://pcgames-download.com/", localPath = "" )


		for i in range(ini,fin+1):
		
			i = str(i)
			url = 'https://pcgames-download.com/page/' + i + '/'
			namePage = "page" + i + ".html"

			pPage(namePage)	


			#-------------------------------------------------------
			# Scraping Procces
			#-------------------------------------------------------

			# Get html code from web
			app.getHtmlCode( url )			

			'''
			# Editing html
			app.deleteTags()		
			app.editPostUrl()
			app.editNumNav()


			# Save html and images
			app.saveHtml( root, namePage)
			app.saveImages()

			'''
			
			# Download all Post per page
			#app.resetSoup() # Reseting soup changes
			app.setNumberPage(str(i))			
			app.savePosts()


			#-------------------------------------------------------
			# END Scraping Procces
			#-------------------------------------------------------



	def appMultiplePageBy( mult ):

		mult = mult
		
		bigList = []

		app = pcGamesPages( urlDomain = "https://pcgames-download.com/", localPath = "" )

		for i in range(ini,fin+1):
		
			i = str(i)
			url = 'https://pcgames-download.com/page/' + i + '/'
			namePage = "page" + i + ".html"

			pPage(namePage)	


			

			#-------------------------------------------------------
			# Scraping Procces
			#-------------------------------------------------------

			# Get html code from web
			app.getHtmlCode( url )

			# save images
			app.saveImages()

			#-------------------------------------------------------
			# END Scraping Procces
			#-------------------------------------------------------


			bigList.append( app.getSoup().findAll("div", {"class": "post-container"}) )


			# Multiplos de 10
			if (int(i)%mult) == 0 or int(i) == fin:

				print("Editing html data...")

				namePage = "big" + i + ".html"
				soupPosts = app.getSoup().find("div", {"class": "posts"})
				nav = app.getSoup().find("div", {"class": "wp-pagenavi"})

				soupPosts.clear() # Delete content from sopupTag


				for itemBiglist in bigList:
					for itemPageBotton in itemBiglist:
						soupPosts.append(itemPageBotton)



				nav.clear() # Delete content from nav

				for j in range(ini,fin+1):

					j = str(j)

					if (int(j)%mult) == 0 or int(j) == fin:
						if j == i:
							nav.append( BeautifulSoup('<span class="current">'+j+'</span>', 'html.parser') )
						else:
							nav.append( BeautifulSoup('<a class="page larger" href="big'+j+'.html" >'+j+'</a>', 'html.parser') )

				

				# Editing html
				app.deleteTags()		
				app.editPostUrl()				

				# Save html and images
				app.saveHtml( root, namePage)

				
				bigList = []

					


	



	pInit()

	appSinlePage()
	#appMultiplePageBy(mult)

	pEnd()



	


initCustomPcGames(228,296,10) #( inicio, final, multiplos ) => Multiplos sirve para unificar paginas
