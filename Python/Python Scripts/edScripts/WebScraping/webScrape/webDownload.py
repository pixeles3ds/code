from edtools import *
from edtools.Scrape import WebScrape
import sys


# Extend core
class DownloadWeb(WebScrape.WebScrape):
	# def __init__(self, root = "C:/xampp/htdocs/webscrape", folder = "", srfolder = "" ):
	# self.root = root
	# self.folder = folder
	# self.srcFolder = srcFolder

	pass


# Extend core
class BrowseWeb(WebScrape.browseWeb):
	# def __init__(self, root = "C:/xampp/htdocs/webscrape", folder = "", srfolder = "" ):
	# self.root = root
	# self.folder = folder
	# self.srcFolder = srcFolder

	pass


def scrape( url, folder, rewriteIMG=1, rewriteFiles=1, downloadFiles = 1, createFolders = 1, createExt = 0  ):


	def initScrape():

		app = DownloadWeb( url = url, folder=folder, rewriteIMG=rewriteIMG, rewriteFiles=rewriteFiles, downloadFiles = downloadFiles, createFolders = createFolders, createExt = createExt )

		# -------------------------------------------------------
		# Scraping Procces
		# -------------------------------------------------------


		#app.getHtmlCode(url) # Get html code from web
		app.loadCodeHtml(url)  # load html code from HDD

		app.loadResourcesFromJson() # load list of resources from file
		app.fixFoldersByReferers() # fix folders tree
		app.saveResources() # download requests

		app.makeCopyBackup() # create backups of files that need to be changed
		app.beautyWeb() # beautifying files
		app.saveHtml() # save index.html

		app.fixResourcesChanges() # Fix resources errors and make conversions
		app.convertWEbToLocal() # Convert web to local relative paths


		# -------------------------------------------------------
		# END Scraping Procces
		# -------------------------------------------------------

	initScrape()


def browser( url, folder, rwi, rwf, dF, cf, ce ):


	appd = DownloadWeb( url = url, folder = folder, rewriteIMG = rwi, rewriteFiles = rwf, downloadFiles = dF, createFolders = cf, createExt = ce  )

	appb = BrowseWeb( folder = folder ) # Launching Selenium and BrowserMobProxy
	appb.setUrl( url ) # Just set url but not execute

	def custom():

		requestsList = appb.getRequests()

		appd.setCode(appb.getCode(), url)
		appd.setResources(requestsList)



		# custom code from downloadweb( class )

		#appd.saveResources()
		# app.convertWEbToLocal()
		# appd.saveHtml()


	while True:

		data = input("--> ")

		if data in " \n":
			pass

		elif data == "9":
			custom()

		elif data in "close exit out finish stop" or data == "0":
			appb.exit()
			break

		elif "exec" in data:
			data = data.replace("exec ", "")
			try: exec(data)
			except: print("Unexpected error:", sys.exc_info()[0])

		else:
			appb.command(data)




def init( url, folder, rwi, rwf, system, downloadFiles, createFolders, createExt  ):


	def pInit():
		print("\n" * 2 + "=" * 80 + "\n" + "\n STARTED\n\n" + "=" * 80 + "\n")

	def kInfo():
		print( "\n 0 ) stop \n\n 1 ) start \n 2 ) getrequests \n 9 ) custom code \n\n\n" + "=" * 80 + "\n")

	def pEnd():
		print("\n" * 5 + "=" * 80 + "\n" + "\n ENDED\n\n" + "=" * 80 + "\n")

	def start():

		if system == "scrape":
			scrape(url, folder, rwi, rwf, downloadFiles, createFolders, createExt )

		if system == "browser":
			browser( url, folder, rwi, rwf, downloadFiles, createFolders, createExt )


	pInit()

	kInfo()

	start()

	pEnd()





# -------------------------------------------------------
#
#    ( rwi = 1 )    -> 1 Rewrite images, 0 don't rewrite
#    ( rwf = 1 )    -> 1 Rewrite files, 0 don't rewrite
#    ( system = "scrape" ) -> scrape with just BeautifulSoup
#    ( system = "browser" ) -> scrape with Selenium, BrowserMobProxy and BeautifulSoup
#    ( folder )     -> folder project
#
# -------------------------------------------------------


system = "scrape"
#system = "browser"


rwi = 0
rwf = 0
downloadFiles = 1       # Just for test purpose
createExt = 1           # Create a extension by typefile
createFolders =  0      # If folder not exist create it by type file


folder = "stripe"
url = "https://stripe.com"

#folder = "nytimes"
#url = "https://nytimes.com"
#url = "https://google.com"


'''
This app works with the files to work properly:
	logs/resources.json
	indexOriginal.html
	
Those file are generate by system = "browser"
'''

init( url, folder, rwi, rwf, system, downloadFiles, createFolders, createExt )



