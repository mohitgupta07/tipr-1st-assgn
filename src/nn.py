import numpy as np
def K_NN(red_data,red_label,test_data,K):
        '''
        red_data  <10000,M>
        red_label <10000,1>
        test_data <1000, M>
        '''
        #Self-citation: Using Code from Course LAP, assignment 2 Problem 2.
        #print(red_data.shape,red_label.shape,test_data.shape,K)
        test_label=[]
        for i in test_data:
            diff={}
            xt=np.array(i)
            for j in range(len(red_data)):
                xq=np.array(red_data[j])
                diff[j]=np.power(np.linalg.norm(xt-xq),2)
            diff=sorted(diff.items(),key=lambda kv: kv[1])#min_distance
            count={}
            #print(diff)
            for j in range(K):
                lab=red_label[diff[j][0]]
                #print(lab)
                if lab not in count:
                    count[lab]=(1,diff[j][1])
                else:
                    count[lab]+=(count[lab][0]+1,count[lab][1])
            #CHKPNT
            count=sorted(count.items(),key=lambda kv: (kv[0],-1*kv[1]),reverse=True)#max_count
            #print(count)
            test_label.append( count[0][0])
        return test_label


def findBestK(k,train_data,train_label,test_data,test_label):
    import time
    tacc={}
    Best_acc=0
    Best_K=0
    for j in range(2,k+1):
        print('starting for k=',j)
        start_time=time.time()
        calc_label=K_NN(train_data,train_label,test_data,j)
        tacc[j]=np.mean(test_label == calc_label)
        finish_time=time.time()-start_time
        print(j,tacc[j],finish_time,"sec")
        if(Best_acc<tacc[j]):
            Best_acc=tacc[j]
            Best_K=j
    return Best_K,Best_acc




import random
import math
import operator


def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist=np.power(np.linalg.norm(testInstance[:-1]-trainingSet[x][:-1]),2)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	
	countCLass = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in countCLass:
			countCLass[response] += 1
		else:
			countCLass[response] = 1
	sortedVotes = sorted(countCLass.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def mainNN(trainingSet,testSet,K=3):
	# prepare data
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	for x in range(len(testSet)):
		res = getNeighbors(trainingSet, testSet[x], K)
		predictions.append(res)
	return predictions
	
