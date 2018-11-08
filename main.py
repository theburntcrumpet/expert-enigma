from SearchTermsFile import *
from ItemSearcher import *
from CountsFile import *
import logging,time,random,datetime

TERMS_FILE = "Terms.txt"
SLEEP_MIN = 7
SLEEP_MAX = 40
MIN_ITEMS_SELECT = 3
MAX_ITEMS_SELECT = 15


days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
WORK_DAYS = ["Tuesday","Wednesday","Thursday"]
WORK_START_TIME = datetime.time(hour=8,minute=40)
WORK_END_TIME = datetime.time(hour=16,minute=50)
LUNCH_HOUR = datetime.time(hour=12,minute=12)
LUNCH_HOUR_LENGTH = datetime.timedelta(hours=1)

def CurrentlyWorking():
    currentNow = datetime.datetime.now()
    # Is today a working day for you?
    if days[currentNow.weekday()] not in WORK_DAYS:
        return False
        
    # Are we outside of working hours?
    if currentNow.time() < WORK_START_TIME or currentNow.time() > WORK_END_TIME: 
        return False
    
    # Is it your lunch hour?
    if currentNow.time() > LUNCH_HOUR and datetime.datetime.combine(datetime.datetime.today(),currentNow.time()) < datetime.datetime.combine(datetime.datetime.today(),LUNCH_HOUR) + LUNCH_HOUR_LENGTH:
        return False

    return True

def CallBluff():
    SearchesMade = CountsFile("Searches.txt")
    ItemsBrowsed = CountsFile("Items.txt")

    if not (ItemsBrowsed.Read() and SearchesMade.Read()):
        logging.info("Failed to read Counts Files")

    while True:
        if not CurrentlyWorking():
            logging.warning("Out of working hours")
            time.sleep(60)
            continue
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