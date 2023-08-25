#ToniP
#103INF
#webScrapingExampleA

def main():
	from urllib.request import urlopen as uReq
	from bs4 import BeautifulSoup as soup

	##make a varable to hold the request
	#downloads a web page
	 my_url = 'https://www.amazon.com/s?k=jordan+1&ref=nb_sb_noss_1'
	 #opens a connection to web page and donwloads it
	 uClient = uReq(my_url)

	 #read webpage
	 webPage_rawHTML = uClient.read()

	 #close conneciton
	 uClient.close()

	 #HTML parsing: taking in HTML code and extracting relevant information
	 webPage_soup = soup(webPage_rawHTML, "html.parser")

	 #grabs each procudt
	 #containers = webPage_soup.findAll("div",{"class":"item-container"})







main ()