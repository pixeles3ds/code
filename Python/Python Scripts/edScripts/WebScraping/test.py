from edtools import *

from browsermobproxy import Server
from selenium import webdriver



url = "https://google.com"



# Start browsermob proxy
server = Server(r"C:\webdrivers\browsermob-proxy\bin\browsermob-proxy")
server.start()
proxy = server.create_proxy()


# Setup Chrome webdriver - note: does not seem to work with headless On
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
options.add_argument('--proxy-server=%s' % proxy.proxy) # Setup proxy to point to our browsermob so that it can track requests


driver = webdriver.Chrome( r'C:/webdrivers/chromedriver.exe' , chrome_options = options )


proxy.new_har("Example") # Request listener
driver.get(url)


# collect resources data
dataCollected =[]
entries = proxy.har['log']["entries"]

for entry in entries:
	if 'request' in entry.keys():

		obj = {
			"url": entry['request']['url'],
			"type": entry['response']['content']['mimeType'],
			"size": entry['response']['bodySize'],
			"method": entry['request']['method'],
			"status": entry['response']['status']
		}


		dataCollected.append(obj)


print("-"*50)
printo(dataCollected)
print("-"*50)


server.stop()
driver.quit()


