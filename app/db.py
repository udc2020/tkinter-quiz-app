import json
import os


class Db:
    list_quizes: list

    def __init__(self):
        with open(os.getcwd()+'\db.json', "r") as read_files:
            # get data fro json file    
            self.list_quizes = list(json.load(read_files))

    def get_list_quizes(self):
        return self.list_quizeslist_quizes

    def get_list_len(self) -> int:
        print(len(self.list_quizes))
        return len(self.list_quizes)
     
    def get_list_index(self,i):
        return self.list_quizes[i]
     
    def get_list_quizes(self,i,quize):
        return self.list_quizes[i][quize]
