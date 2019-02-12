import csv
import numpy as np

def loadData(path=r'dolphins.csv',type='data',hasHeaders=False):   
    with open(path,'r') as f:
        reader=csv.reader(f,delimiter=',')
        if hasHeaders:headers=next(reader)#If Headers are provided
        data=list(reader)
        #print(data[0])
        if type=='data':
            data=[list(map(float,tmp[0].strip().split())) for tmp in data]
            
            data=np.array(data).astype(float)
        else:
            data=[list(map(int,tmp[0].strip().split()))[0] for tmp in data]
        #print(data)
            data=np.array(data).astype(int)
    #print(data.shape)
    #print(data[:3])
    return data

def loadDataX(path=r'dolphins.csv',hasHeaders=None):   
    import pandas as pd
    x=pd.read_csv(path,sep=' ',header=hasHeaders)
    return x

def loadDataText(path=r'twitter.txt',type='data',hasHeaders=False):   
    with open(path,'r') as f:
        reader=csv.reader(f,delimiter=',')
        if hasHeaders:headers=next(reader)#If Headers are provided
        data=list(reader)
        #print(data[0])
        #return data
        if type=='data':
            data=[list(map(str,tmp[0].strip().split(' '))) for tmp in data]
            
            #data=np.array(data).astype(str)
        else:
            data=[list(map(int,tmp[0].strip().split()))[0] for tmp in data]
        #print(data)
            data=np.array(data).astype(int)
    #print(data.shape)
    #print(data[:3])
    return data
