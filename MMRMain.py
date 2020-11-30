#!/usr/bin/env python
# coding: utf-8

# In[29]:





# In[30]:





# In[1]:


from Data import Data #importing Data class from data module
from extractData import extractData #importing extractData class from extractData module


# In[3]:


data=Data('mmr.csv')
lis=data.getData()
extData=extractData(lis)#data to lists
inp=5
#main loop
while inp!=0:

    inp=int(input('Enter your choice: 1) Country Wise 2) State Wise 0) To Exit  '))
    if(int(inp==1)):
        publ,pri,chart,publTot,priTot,chartTot=extData.mmrForSchool(1,41000)
        print('Overall US Immunization Rate',round((pri+publ+chart)/41000,3))
        print('Private Schools Immunization Rate',round(pri/priTot,3))
        print('Pulic Schools Immunization Rate',round(publ/publTot,3))
        print('Charter Schools Immunization Rate',round(chart/chartTot,3))
        
        
    elif inp==2:
        st=input('Enter State: ')   
        stInd,endInd=extData.stateToIndex(st)
        publ,pri,chart,publTot,priTot,chartTot=extData.mmrForSchool(stInd,endInd)
        print('Overall State Immunization Rate',round((pri+publ+chart)/(endInd-stInd),3))
        print('Private Schools Immunization Rate',round(pri/(priTot+1),3))
        print('Public Schools Immunization Rate',round(publ/(publTot+1),3))
        print('Charter Schools Immunization Rate',round(chart/(chartTot+1),3))


# In[ ]:





# In[ ]:




