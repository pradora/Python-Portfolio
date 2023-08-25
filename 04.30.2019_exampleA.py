python3
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.cartoonnetwork.com'
uClient = uReq(my_url)
webPage_rawHTML = uClient.read()
uClient.close()#hi dad
webPage_soup = soup(webPage_rawHTML, "html.parser")
webPage_soup