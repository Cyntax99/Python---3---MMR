
from Data import Data #importing Data class from data module
from extractData import extractData #importing extractData class from extractData module

data=Data('mmr.csv')#Reading CSV FILE
lis=data.getData() #Data as lists from Data Class
extData=extractData(lis)#data to lists
inp=5 #for true
#main loop
while inp!=0: #End if user types 0

    inp=int(input('Enter your choice: 1) Country Wise 2) State Wise 0) To Exit  '))
    if(int(inp==1)):#For Whole US Analysis
        #getting public,private and charter schools total MMR and their counts to calculate MMR RATE
        publ,pri,chart,publTot,priTot,chartTot=extData.mmrForSchool(1,41000)
        print('Overall US Immunization Rate',round((pri+publ+chart)/41000,3)) #Round to 3 digit MMR Rate
        print('Private Schools Immunization Rate',round(pri/priTot,3))#Round to 3 digit MMR Rate
        print('Pulic Schools Immunization Rate',round(publ/publTot,3))#Round to 3 digit MMR Rate
        print('Charter Schools Immunization Rate',round(chart/chartTot,3))#Round to 3 digit MMR Rate
        
        
    elif inp==2:#FOR SPEFIC STATE ANALYSIS
        st=input('Enter State: ')   #Taking State Name from User
        stInd,endInd=extData.stateToIndex(st) #State name to Start Index and End Index in Data for bound analysis
        publ,pri,chart,publTot,priTot,chartTot=extData.mmrForSchool(stInd,endInd)#getting public,private and charter schools total MMR and their counts to calculate MMR RATE
        print('Overall State Immunization Rate',round((pri+publ+chart)/(endInd-stInd),3))
        print('Private Schools Immunization Rate',round(pri/(priTot+1),3))
        print('Public Schools Immunization Rate',round(publ/(publTot+1),3))
        print('Charter Schools Immunization Rate',round(chart/(chartTot+1),3))