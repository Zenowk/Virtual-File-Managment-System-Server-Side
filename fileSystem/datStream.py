import pickle
import os


class datStream:
    def dump(self, fileSystem):
        with open ('file.dat','wb') as output:
            pickle.dump(fileSystem,output,pickle.HIGHEST_PROTOCOL)
    
    def loadData(self): 
        with open('file.dat','rb') as input:
            db=pickle.load(input)
        return db

