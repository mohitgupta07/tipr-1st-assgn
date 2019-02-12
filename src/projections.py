# Implement code for random projections here!
import numpy as np
def randomProjection(X,K,dataName):
        import os.path
        path='ReducedDataSets/{0}_dim_{1}.npy'.format(K,dataName)
        if(os.path.exists(path)):
            print('Loading Already Stored File')
            return np.load(path)
        from scipy.linalg import orth
        RM=np.random.randn(X.shape[1],K) / X.shape[1]
        O=orth(RM)
        X_K=np.dot(X,RM) # N X L . L X K == N X K
        np.save(path,X_K)# dataName== pubmed,twitter, dolphins
        return X_K
    