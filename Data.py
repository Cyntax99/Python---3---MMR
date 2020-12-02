import csv
#Data Class for Importing data and csv data to list
class Data:
    def __init__(self, filename):
        self.file=filename #Class var to filename
    def getData(self):#to get All data from CSV
        items=list() #list for storing all data
        with open(self.file, 'r') as file:
            r = csv.reader(file, delimiter = '\t')
            for x in r:
                items.append(x)#append csv line in list
            return items