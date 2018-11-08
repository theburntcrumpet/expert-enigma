from SearchTerms import *
import os, logging

class SearchTermsFile(SearchTerms):
    def __init__(self,filename="SearchTerms.txt"):
        super().__init__()
        self.filename = filename

    def WriteIfNotExist(self):
        try:
            if os.path.exists(self.filename):
                return True

            f = open(self.filename,"w")
            for term in self.terms:
                f.write("{}\n".format(term))
            f.close()

        except Exception as e:
            logging.info(e)
            return False

        return True
            
    def Read(self):
        if not self.WriteIfNotExist():
            logging.info("Failed to write the missing file")
            return False

        try:
            f = open(self.filename,"r")
            self.terms = []
            for line in f.readlines():
                self.terms.append(line)
            f.close()

        except Exception as e:
            logging.error(e)
            return False

        return True