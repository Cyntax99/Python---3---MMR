#For giving different results on data
class extractData:
    def __init__(self, data): #Constructor that takes data list as an argument
        self.data=data
        self.state=[]
     #convert whole state string to money tokens    
    
    def mmrForState(self,ind): #MMR for a state
        mmr=0
        for i in range(ind,ind+200):
            self.state=self.data[ind][0].split(',')
            mmr=mmr+int(self.state[9])
        return mmr
    #MMR for all school types
    def mmrForSchool(self,stInd,enInd):
        pulicMMR=0
        privateMMR=0
        charterMMR=0
        priTot=0
        publTot=0
        chartTot=0
        for i in range(stInd,stInd+enInd):
            sch=self.data[i][0].split(',')
            mmr=self.data[i][0].split(',')
            mmr=mmr[8]
            if sch[4]=='Public':#School is Public then calculate its MMR
                if mmr=='' or mmr=='-1':
                    pulicMMR=pulicMMR+0
                else:
                    pulicMMR=pulicMMR+int(mmr)
                publTot=publTot+1    
            if sch[4]=='Charter':
                if mmr=='' or mmr=='-1':
                    charterMMR=charterMMR+0
                else:
                    charterMMR=charterMMR+int(mmr)
                chartTot=chartTot+1    
            if sch[4]=='Private':
                if mmr=='' or mmr=='-1':
                    privateMMR=privateMMR+0
                else:
                    privateMMR=privateMMR+int(mmr)
                priTot=priTot+1    
                    
                
        return  pulicMMR,privateMMR,charterMMR,publTot,priTot,chartTot
    #Convert state name to its start Index and End Index in file
    def stateToIndex(self,st):
        startIndex=0
        endIndex=0
        isCome=False
        for i in range(0,len(self.data)):
            self.state=self.data[i][0].split(',')
            
            for j in range(0,len(self.state)):
                if self.state[j]==st:
                    endIndex=endIndex+1
                    if isCome==False:
                        startIndex=i
                        isCome=True
        return startIndex,endIndex           