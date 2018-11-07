from SearchTermsFile import *
from ItemSearcher import *
from CountsFile import *
import logging,time,random

TERMS_FILE = "Terms.txt"
SLEEP_MIN = 4
SLEEP_MAX = 30
MIN_ITEMS_SELECT = 3
MAX_ITEMS_SELECT = 15

def CallBluff():
    SearchesMade = CountsFile("Searches.txt")
    ItemsBrowsed = CountsFile("Items.txt")

    if not (ItemsBrowsed.Read() and SearchesMade.Read()):
        logging.info("Failed to read Counts Files")

    while True:
        searchTerms = SearchTermsFile(TERMS_FILE)
        searchTerms.Read()
        itemSearcher = ItemSearcher(random.choice(searchTerms.terms).replace(" ","+"))
        SearchesMade.count += 1
        SearchesMade.Write()
        itemSearcher.Search()
        time.sleep(random.randint(SLEEP_MIN,SLEEP_MAX))
        if len(itemSearcher.ItemLinks) == 0:
            continue
        for i in range(1,random.randint(MIN_ITEMS_SELECT,MAX_ITEMS_SELECT)):
            Getter(random.choice(itemSearcher.ItemLinks))
            ItemsBrowsed.count+=1
            ItemsBrowsed.Write()
            time.sleep(random.randint(SLEEP_MIN,SLEEP_MAX))

if __name__ == "__main__":
    CallBluff()