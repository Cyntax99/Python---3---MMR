import csv
#Data Class for Importing data and csv data to list
class Data:
    def __init__(self, filename):
        self.file=filename
    def getData(self):
        items=list()
        with open(self.file, 'r') as file:
            r = csv.reader(file, delimiter = '\t')
            for x in r:
                items.append(x)
            return items