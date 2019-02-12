
if __name__ == '__main__':
    print('Welcome to the world of high and low dimensions!')
    # The entire code should be able to run from this file!
    import FileHandler
    import bayes
    import nn
    import numpy as np
    from sklearn.metrics import classification_report, confusion_matrix
    from projections import randomProjection
    X=[]
    Y=[]
    X_D=[]
    dataName =''


    
    def preProcessText():
        
        global X,Y,dataName
        trainPath='twitter.txt'
        dataName=trainPath[:trainPath.find('.txt')]
        labelPath='twitter_label.txt'
        X=FileHandler.loadDataText(path=trainPath)
        Y=FileHandler.loadDataText(path=labelPath,type='label')
        twitterMAT()

        
    def twitterMAT():#Converts word matrix to n X D matrix.
        #pre-process
        global X_D,X,Y
        UniqueDict={}   
        for a in X:
            for t in a:
                    if t not in UniqueDict:
                            UniqueDict[t]=0
                    UniqueDict[t]+=1

        #KNN stuff--- creating N X D matrix for knn
        X_D=np.zeros((len(X),len(UniqueDict)),dtype=int)
        keys=list(UniqueDict.keys())
        for a,c in zip(X, [ i for i in range(len(X))]):
            for t in a:
                    if t not in keys:
                            continue#security check
                    X_D[c][keys.index(t)]+=1
        #X=X_D
        #sk_fold_crossValidate(X_D,Y,MNB_X_D)
        
    def MNB_X_D(X_train, X_test, Y_train, Y_test):
        Classes={}
        X_train=np.array(X_train)
        X_test=np.array(X_test)
        for i in Y_train:
            if i not in Classes:
                    Classes[i]=0
            Classes[i]+=1
        print(Classes)
        
        cls=list(Classes.keys())
        print(cls)
        LocalDicts=np.zeros((len(cls),X_train.shape[1]))
        print(LocalDicts.shape)
        for a,c in zip(X_train,Y_train):
            ind=cls.index(c)
            #print(ind, end=' ')
            LocalDicts[ind]+=np.array(a)

        correct=0
        from math import log
        for a,c in zip(X_test,Y_test):
            bestClass=0
            bestProb=0
            for i in cls:
                likelihood=0
                prioriY=Classes[i]
                ind=cls.index(i)
                alpha=1e-3
                summ=sum(LocalDicts[ ind])
                ti= ( sum(list(Classes.values()))/prioriY)
              #  print(summ,prioriY,ind)
                for t in range(len(a)):
                    #print(t)
                        likelihood+= (log(1+a[t])*log((LocalDicts[ind][t]+1)/(alpha*(summ+ X_train.shape[1]))))  
                    
                    #print(likelihood)
                postYgivX=likelihood+ log(prioriY)
                
               # print(postYgivX,likelihood)
                if(postYgivX>bestProb):
                    bestProb=postYgivX
                    bestClass=i
            if(bestClass==c):
                correct+=1
        return correct/len(X_test)
          
       

        
    def MNB(X_train, X_test, Y_train, Y_test):
        #pre-process
        X=X_train
        Y=Y_train
        Classes={}
        for i in Y:
            if i not in Classes:
                    Classes[i]=0
            Classes[i]+=1


        UniqueDict={}   
        for a in X:
            for t in a:
                    if t not in UniqueDict:
                            UniqueDict[t]=0
                    UniqueDict[t]+=1

        LocalDicts={ i:{} for i in Classes}
        for key in UniqueDict.keys():#Assumming DIct are Insertion ORdered
            for i in Classes:
                LocalDicts[i][key]=0
        for i in Classes:
             list(LocalDicts[i].keys())==list(UniqueDict.keys())
        for a,c in zip(X,Y):
            for t in a:
                    if t not in LocalDicts[c]:
                            LocalDicts[c][t]=0
                    LocalDicts[c][t]+=1        
        

        #MNB CODE-----
        correct=0
        for a,c in zip(X_test,Y_test):
            bestClass=0
            bestProb=0
            for i in Classes:
                likelihood=1
                prioriY=Classes[i]
                for t in a:
                    if t not in UniqueDict.keys():
                        likelihood*= ((0+1)/(sum(LocalDicts[i].values())+ len(UniqueDict.keys())  )) 
                    else:
                        likelihood*= ((LocalDicts[i][t]+1)/(sum(LocalDicts[i].values())+ len(UniqueDict.keys()) )) 
                postYgivX=likelihood*prioriY
                if(postYgivX>bestProb):
                    bestProb=postYgivX
                    bestClass=i
            if(bestClass==c):
                correct+=1
        return correct/len(X_test)
            
            

        
    def init(testPath='pubmed.csv',labelPath='pubmed_label.csv',dN='pubmed'):
        global X,Y,X_D,dataName
        dataName=dN
        print('Please provide the training data with the very same name on the very destination where this code exists!')
            
        if(dataName=='twitter'):
            print('WOrking on twitter dataset!!')
            
            preProcessText()
            rpLoop(X_D,X_D.shape[1],dataName)
            print('Naive Bayes for twitter:-')
            sk_fold_crossValidate(X,Y,MNB)
            print('KNN for twitter:-')
            sk_fold_crossValidate(X_D,Y,KNN_2)
            
        
        else:
            X=FileHandler.loadData(path='{0}.csv'.format(dataName))
            Y=FileHandler.loadData(path='{0}_label.csv'.format(dataName),type='label')
            X=np.array(X)
            rpLoop(X,X.shape[1],dataName)
            X_test=FileHandler.loadData(path=testPath)
            Y_test=FileHandler.loadData(path=labelPath,type='label')
            
            print('Naive Bayes for {0}:-'.format(dataName))
            
            #a,b,c,d=train_test_split(X,Y)
            print('acc:',naiveClass(X,X_test,Y,Y_test))
            print('KNN for {0}:-'.format(dataName))
        
            print('acc:',KNN_2(X,X_test,Y,Y_test))
        
        
               
    def sk_fold_crossValidate(X,Y,model,K=10):
        import random
        random.seed(42)
        X_S=[]
        assert dataName=='twitter' or dataName=='pubmed' or dataName=='dolphins'
        if(dataName!='twitter'):
            from sklearn.preprocessing import StandardScaler
            scaler = StandardScaler()
            X_S=scaler.fit_transform(X)
        else:
            X_S=X
                
            
        from sklearn.model_selection import StratifiedKFold
        skf = StratifiedKFold(n_splits=K,random_state=42) # Define the split - into K folds 
        skf.get_n_splits(X_S,Y) # returns the number of splitting iterations in the cross-validator
        print(skf)
        best_acc=0
        count=0
        for train_index, test_index in skf.split(X_S,Y):
             X_train,X_test,Y_train,Y_test=[],[],[],[]   
             if type(X[0])!= type(2):
                 for ind in train_index:
                     X_train.append(X[ind])
                 for ind in test_index:
                     X_test.append(X[ind])
                
             else:    
                 X_train, X_test = X[train_index], X[test_index]
             Y_train, Y_test = Y[train_index], Y[test_index]
             tmp=model(X_train, X_test, Y_train, Y_test)
             print('counter:- ',count+1,'ACC:',tmp)
             best_acc+=tmp
             count+=1
        print("Test ACC:=",best_acc/count,'\n')
        return best_acc/count

    
    def testForDiffDim(X,Y,model,task):
        global dataName
        res={}
        D=2
        K=X.shape[1]
        while(D<K):
           X_D=randomProjection(X,D,dataName)
           res[D]=sk_fold_crossValidate(X_D,Y,model,K=3)
           D*=2
        #print(res)
        #res=np.array(res)
        import matplotlib.pyplot as plt
        plt.plot(res.keys(),res.values())
        plt.title('output_plots/task_{3}_{0}_{1}_{2}'.format(dataName,K,model.__qualname__,task))
        plt.ylabel('accuracy')
        plt.xlabel('D')		
	
        plt.savefig('output_plots/task_{3}_{0}_{1}_{2}'.format(dataName,K,model.__qualname__,task))
        
        plt.show()
        
        #np.save('res_{0}.npy'.format(dataName),res)
        print(res)
        
    def rpLoop(X,K,dataName):
        D=2
        while(D<K):
           randomProjection(X,D,dataName)
           
           D*=2
        randomProjection(X,K,dataName)
           
    
    def train_test_split(X,Y):
        #Cross-validation -- to be done via k-fold later.
        from sklearn.model_selection import train_test_split  
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)
        return X_train, X_test, Y_train, Y_test

    def naiveClass(X_train, X_test, Y_train, Y_test):
        global dataName
        bae=bayes.naiveBayes(X_train,  Y_train,X_test, Y_test,dataName)
        bae.getProbabilities()
        #print(confusion_matrix(Y_test, y_pred))  
        #print(classification_report(Y_test, y_pred)) 
        return bae.testModel()

    def sknaiveClass(X_train, X_test, Y_train, Y_test):
        from sklearn.naive_bayes import GaussianNB 
        gnb = GaussianNB() 
        gnb.fit(X_train,Y_train) 

        # making predictions on the testing set 
        y_pred = gnb.predict(X_test) 

        # comparing actual response values (y_test) with predicted response values (y_pred) 
        from sklearn import metrics 
        #print("Naive Bayes model accuracy(in %):", metrics.accuracy_score(Y_test, y_pred)*100)
        #print(confusion_matrix(Y_test, y_pred))  
        #print(classification_report(Y_test, y_pred)) 
        return  metrics.accuracy_score(Y_test, y_pred)


    def skMNB(X_train, X_test, Y_train, Y_test):
        from sklearn.naive_bayes import MultinomialNB
        clf = MultinomialNB()
        clf.fit(X_train, Y_train)
        MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
        y_pred=(clf.predict(X_test))
        #print(confusion_matrix(Y_test, y_pred))  
        #print(classification_report(Y_test, y_pred)) 
        from sklearn import metrics 
        return  metrics.accuracy_score(Y_test, y_pred)

    
    def KNN(X_train, X_test, Y_train, Y_test):
        #KNN stuff.
        #print(nn.findBestK(5,X_train,Y_train,X_test, Y_test))
        y_pred=nn.K_NN(X_train,Y_train,X_test,3)
        #print(confusion_matrix(Y_test, y_pred))  
        #print(classification_report(Y_test, y_pred)) 
        from sklearn import metrics 
        return  metrics.accuracy_score(Y_test, y_pred)
    def KNN_2(X_train, X_test, Y_train, Y_test):
        #KNN stuff.
        #print(nn.findBestK(5,X_train,Y_train,X_test, Y_test))
        y_pred=nn.mainNN(np.insert(X_train,len(X_train[0]),Y_train,axis=1),np.insert(X_test,len(X_test[0]),Y_test,axis=1))
        #print(confusion_matrix(Y_test, y_pred))  
        print(classification_report(Y_test, y_pred)) 
        from sklearn import metrics 
        return  metrics.accuracy_score(Y_test, y_pred)
    
    def skKNN(X_train, X_test, Y_train, Y_test):
        #KNN SkLearn
        from sklearn.neighbors import KNeighborsClassifier  
        classifier = KNeighborsClassifier(n_neighbors=3)  
        classifier.fit(X_train, Y_train)
        y_pred = classifier.predict(X_test)
        #print(confusion_matrix(Y_test, y_pred))  
        #print(classification_report(Y_test, y_pred)) 
        from sklearn import metrics 
        return  metrics.accuracy_score(Y_test, y_pred)



    
    def call(a,b,c):
        print(a,b,c)
        assert a!="" and b!="" and c!=""
        init(a,b,c)
    #call('aa')

    import argparse        
    #parser starts
    parser = argparse.ArgumentParser(description='Problem 1')
    parser.add_argument('testdata', metavar='<test-data.csv>', type=str,
                            help='file name.txt for the problem1')
    parser.add_argument('testlabel', metavar='<test-label.csv>', type=str,
                            help='file name.txt for the problem1')
    parser.add_argument('dataset', metavar='<dataset>', type=str,
                            help='file name.txt for the problem1')

    parser.add_argument(  dest='func', action='store_const',
                            const=call,
                            help='execution of Problem1')


    args = parser.parse_args()
    args.func(args.testdata,args.testlabel,args.dataset)
    #parser ends

    # Calculating error for K values between 1 and 40
    '''for i in range(1, 40):  
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, Y_train)
        pred_i = knn.predict(X_test)
        error.append(np.mean(pred_i != Y_test))
    import matplotlib.pyplot as plt
    plt.figure(figsize=(12, 6))  
    plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',  
         markerfacecolor='blue', markersize=10)
    plt.title('Error Rate K Value')  
    plt.xlabel('K Value')  
    plt.ylabel('Mean Error')
    '''
