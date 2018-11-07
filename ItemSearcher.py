import urllib.request
from bs4 import BeautifulSoup
from Getter import *
class ItemSearcher:
    def __init__(self,strItem):
        self.strItem = strItem
        self.ItemLinks = []

    def Search(self):
        baseUrl = "https://www.amazon.co.uk/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords="
        response = Getter("{}{}".format(baseUrl,self.strItem))
        page = BeautifulSoup(response,features="lxml")
        for i in page.find_all("a"):
            link = i.get("href")
            if link and "dp" in link and "ref" in link and link.startswith("https://"):
                self.ItemLinks.append(link)
