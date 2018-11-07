import os, logging

class CountsFile:
    def __init__(self,filename):
        self.filename = filename
        self.count = 0

    def Write(self):
        try:
            f = open(self.filename,"w")
            f.write("{}".format(self.count))
            f.close()
        except Exception as e:
            logging.error(e)

    def Read(self):
        if not os.path.exists(self.filename):
           if not self.Write():
               return False
        try:
            f = open(self.filename,"r")
            self.count = int(f.read()[0])
        except Exception as e:
            self.count = 0
            logging.error(e)
            return False
        
        return True