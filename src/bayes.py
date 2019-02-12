# Implement Bayes Classifier here!

# Since Input Features are continuous so using Gaussian to calculate probability Density
import numpy as np
class naiveBayes:
    def __init__(self,trainX,trainY,testX,testY,dataName,method='continuous'):
        self.trainX=np.array(trainX)
        self.trainY=np.array(trainY)
        self.testX=np.array(testX)
        self.testY=np.array(testY)
        self.method=method
        self.dataName=dataName
    def getProbabilities(self):
        #prior prob..
        prioriY=dict()
        K=0#No. of Classes.
        for y in self.trainY:
            if y not in prioriY:
                prioriY[y]=0
                K+=1
            prioriY[y]+=1#keeping in counts...

        #Likelihood prob... 
        #Getting Mean and variance  
        #KmeanVectors==kmv
        #KVarianceVectors==kvv
        kmv=np.zeros((K,self.trainX.shape[1]))
        kvv=np.zeros((K,self.trainX.shape[1]))
        print('no. of classes:',K,'Data Shape:',self.trainX.shape)
        for (X,Y) in zip(self.trainX,self.trainY):
            #print(X,Y)
            kmv[int(Y)]+=X
            
        #print(kmv,kvv)
        key=list(prioriY.keys())
        for i in key:
            #print(i,kmv[i],prioriY[i])
            kmv[key.index(i)]/=prioriY[i]#MEAN
        for (X,Y) in zip(self.trainX,self.trainY):
            kvv[Y]+=np.power((X-kmv[Y]),2)
        kvv/=(prioriY[i]-1)
        self.kmv=kmv
        self.kvv=kvv
        self.K=K
        self.prioriY=prioriY
    def save(self):
    	np.save('Model_{0}_kmv.npy'.format(dataName),self.kmv)
    	np.save('Model_{0}_kvv.npy'.format(dataName),self.kvv)
    	np.save('Model_{0}_K.npy'.format(dataName),self.K)
    	np.save('Model_{0}_prioriY.npy'.format(dataName),self.prioriY)
    def load(self):
    	pass
    def testModel(self):
        correct=0
        for (X,Y) in zip(self.testX,self.testY):
            posterior=[0]*self.K
            for i in range(self.K):
                diff=X-self.kmv[i]
                diff=np.power(diff,2)
                ex=diff/self.kvv[i]
                ex=(ex/2) *(-1)
                exp=np.exp(ex)
                Like=exp/ (np.sqrt(2*np.pi*self.kvv[i]))
                Likelihood=1
                for likes in Like:#NEED TO VECTORIZE THIS LINE AS WELL...
                    Likelihood*=likes
                posterior[i]=self.prioriY[Y]*Likelihood
                #print(Like)
            Hy=np.argmax(posterior) 
            #print(posterior)
            #print(Hy,Y)
            if(Hy==Y):
                correct+=1  
                        
        return correct/self.testY.shape[0]
#Sample Dataset...
'''
X=[[6,180,12],[5.92,190,11],[5.58,170,12],[5.92,165,10],[5,100,6],[5.5,150,8],[5.42,130,7],[5.75,150,9]]
Y=[0,0,0,0,1,1,1,1]
tX=[[6,130,8]]
tY=[1]
bae=naiveBayes(X,Y,tX,tY)
bae.getProbabilities()
bae.testModel()
'''
