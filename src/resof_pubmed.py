Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: D:\workspace\tipr\tipr-first-assignment\src\main.py ========
Welcome to the world of high and low dimensions!
>>> init()
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
>>> sk_fold_crossValidate(X,Y,KNN,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
              precision    recall  f1-score   support

           0       0.25      0.01      0.03       444
           1       0.42      0.23      0.30       819
           2       0.40      0.79      0.53       809

   micro avg       0.40      0.40      0.40      2072
   macro avg       0.36      0.35      0.29      2072
weighted avg       0.38      0.40      0.33      2072

counter:-  1 ACC: 0.402992277992278
              precision    recall  f1-score   support

           0       0.19      0.01      0.03       444
           1       0.39      0.22      0.28       818
           2       0.39      0.77      0.52       809

   micro avg       0.39      0.39      0.39      2071
   macro avg       0.32      0.33      0.28      2071
weighted avg       0.35      0.39      0.32      2071

counter:-  2 ACC: 0.3901496861419604
              precision    recall  f1-score   support

           0       0.39      0.02      0.03       444
           1       0.42      0.26      0.32       818
           2       0.40      0.76      0.53       809

   micro avg       0.41      0.41      0.41      2071
   macro avg       0.40      0.35      0.29      2071
weighted avg       0.41      0.41      0.34      2071

counter:-  3 ACC: 0.4056011588604539
              precision    recall  f1-score   support

           0       0.18      0.01      0.02       444
           1       0.41      0.25      0.31       818
           2       0.39      0.76      0.52       809

   micro avg       0.40      0.40      0.40      2071
   macro avg       0.33      0.34      0.28      2071
weighted avg       0.36      0.40      0.33      2071

counter:-  4 ACC: 0.39546112988894255
              precision    recall  f1-score   support

           0       0.16      0.01      0.02       443
           1       0.42      0.23      0.30       818
           2       0.41      0.81      0.54       809

   micro avg       0.41      0.41      0.41      2070
   macro avg       0.33      0.35      0.29      2070
weighted avg       0.36      0.41      0.33      2070

counter:-  5 ACC: 0.40869565217391307
              precision    recall  f1-score   support

           0       0.14      0.01      0.01       443
           1       0.41      0.22      0.29       818
           2       0.40      0.79      0.53       809

   micro avg       0.40      0.40      0.40      2070
   macro avg       0.31      0.34      0.28      2070
weighted avg       0.35      0.40      0.32      2070

counter:-  6 ACC: 0.39806763285024155
              precision    recall  f1-score   support

           0       0.16      0.01      0.02       443
           1       0.41      0.24      0.30       818
           2       0.39      0.76      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.32      0.34      0.28      2069
weighted avg       0.35      0.39      0.33      2069

counter:-  7 ACC: 0.39342677622039635
              precision    recall  f1-score   support

           0       0.35      0.01      0.03       443
           1       0.39      0.21      0.27       818
           2       0.39      0.77      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.38      0.33      0.27      2069
weighted avg       0.38      0.39      0.32      2069

counter:-  8 ACC: 0.3895601739971
              precision    recall  f1-score   support

           0       0.09      0.00      0.01       443
           1       0.41      0.23      0.30       818
           2       0.40      0.78      0.53       808

   micro avg       0.40      0.40      0.40      2069
   macro avg       0.30      0.34      0.28      2069
weighted avg       0.33      0.40      0.32      2069

counter:-  9 ACC: 0.3958434026099565
              precision    recall  f1-score   support

           0       0.07      0.00      0.01       443
           1       0.38      0.22      0.28       818
           2       0.39      0.77      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.28      0.33      0.27      2069
weighted avg       0.32      0.39      0.31      2069

counter:-  10 ACC: 0.38569357177380376
Best Result:= 0.39654914625090465 

{'best_acc:': 0.39654914625090465}
>>> 
sk_fold_crossValidate(X,Y,naiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
no. of classes: 3 Data Shape: (18629, 128)
Traceback (most recent call last):
  File "<pyshell#3>", line 2, in <module>
    sk_fold_crossValidate(X,Y,naiveClass,10)
  File "D:\workspace\tipr\tipr-first-assignment\src\main.py", line 40, in sk_fold_crossValidate
    tmp=model(X_train, X_test, Y_train, Y_test)
  File "D:\workspace\tipr\tipr-first-assignment\src\main.py", line 77, in naiveClass
    print(confusion_matrix(Y_test, y_pred))
NameError: name 'y_pred' is not defined
>>> 
======== RESTART: D:\workspace\tipr\tipr-first-assignment\src\main.py ========
Welcome to the world of high and low dimensions!
>>> init()
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
>>> sk_fold_crossValidate(X,Y,naiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
no. of classes: 3 Data Shape: (18629, 128)
counter:-  1 ACC: 0.4025096525096525
no. of classes: 3 Data Shape: (18630, 128)
counter:-  2 ACC: 0.40994688556253017
no. of classes: 3 Data Shape: (18630, 128)
counter:-  3 ACC: 0.4398841139546113
no. of classes: 3 Data Shape: (18630, 128)
counter:-  4 ACC: 0.4505070014485756
no. of classes: 3 Data Shape: (18631, 128)
counter:-  5 ACC: 0.4444444444444444
no. of classes: 3 Data Shape: (18631, 128)
counter:-  6 ACC: 0.45169082125603865
no. of classes: 3 Data Shape: (18632, 128)
counter:-  7 ACC: 0.4485258579023683
no. of classes: 3 Data Shape: (18632, 128)
counter:-  8 ACC: 0.4224262928951184
no. of classes: 3 Data Shape: (18632, 128)
counter:-  9 ACC: 0.41324311261478974
no. of classes: 3 Data Shape: (18632, 128)
counter:-  10 ACC: 0.403093281778637
Best Result:= 0.42862714643667654 

{'best_acc:': 0.42862714643667654}
>>> sk_fold_crossValidate(X,Y,sknaiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
Gaussian Naive Bayes model accuracy(in %): 39.285714285714285
[[ 94 168 182]
 [155 351 313]
 [159 281 369]]
              precision    recall  f1-score   support

           0       0.23      0.21      0.22       444
           1       0.44      0.43      0.43       819
           2       0.43      0.46      0.44       809

   micro avg       0.39      0.39      0.39      2072
   macro avg       0.37      0.37      0.37      2072
weighted avg       0.39      0.39      0.39      2072

counter:-  1 ACC: 0.39285714285714285
Gaussian Naive Bayes model accuracy(in %): 39.2563978754225
[[107 164 173]
 [175 314 329]
 [149 268 392]]
              precision    recall  f1-score   support

           0       0.25      0.24      0.24       444
           1       0.42      0.38      0.40       818
           2       0.44      0.48      0.46       809

   micro avg       0.39      0.39      0.39      2071
   macro avg       0.37      0.37      0.37      2071
weighted avg       0.39      0.39      0.39      2071

counter:-  2 ACC: 0.392563978754225
Gaussian Naive Bayes model accuracy(in %): 43.74698213423467
[[109 152 183]
 [136 380 302]
 [131 261 417]]
              precision    recall  f1-score   support

           0       0.29      0.25      0.27       444
           1       0.48      0.46      0.47       818
           2       0.46      0.52      0.49       809

   micro avg       0.44      0.44      0.44      2071
   macro avg       0.41      0.41      0.41      2071
weighted avg       0.43      0.44      0.43      2071

counter:-  3 ACC: 0.4374698213423467
Gaussian Naive Bayes model accuracy(in %): 45.48527281506519
[[116 169 159]
 [134 400 284]
 [127 256 426]]
              precision    recall  f1-score   support

           0       0.31      0.26      0.28       444
           1       0.48      0.49      0.49       818
           2       0.49      0.53      0.51       809

   micro avg       0.45      0.45      0.45      2071
   macro avg       0.43      0.43      0.43      2071
weighted avg       0.45      0.45      0.45      2071

counter:-  4 ACC: 0.45485272815065186
Gaussian Naive Bayes model accuracy(in %): 45.507246376811594
[[139 151 153]
 [133 369 316]
 [103 272 434]]
              precision    recall  f1-score   support

           0       0.37      0.31      0.34       443
           1       0.47      0.45      0.46       818
           2       0.48      0.54      0.51       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.43      0.44      2070
weighted avg       0.45      0.46      0.45      2070

counter:-  5 ACC: 0.45507246376811594
Gaussian Naive Bayes model accuracy(in %): 45.94202898550724
[[132 144 167]
 [155 380 283]
 [134 236 439]]
              precision    recall  f1-score   support

           0       0.31      0.30      0.31       443
           1       0.50      0.46      0.48       818
           2       0.49      0.54      0.52       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.44      0.43      2070
weighted avg       0.46      0.46      0.46      2070

counter:-  6 ACC: 0.45942028985507244
Gaussian Naive Bayes model accuracy(in %): 43.64427259545674
[[118 157 168]
 [153 366 299]
 [147 242 419]]
              precision    recall  f1-score   support

           0       0.28      0.27      0.27       443
           1       0.48      0.45      0.46       818
           2       0.47      0.52      0.49       808

   micro avg       0.44      0.44      0.44      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.44      0.43      2069

counter:-  7 ACC: 0.4364427259545674
Gaussian Naive Bayes model accuracy(in %): 42.67762203963267
[[126 136 181]
 [141 351 326]
 [146 256 406]]
              precision    recall  f1-score   support

           0       0.31      0.28      0.29       443
           1       0.47      0.43      0.45       818
           2       0.44      0.50      0.47       808

   micro avg       0.43      0.43      0.43      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.43      0.43      2069

counter:-  8 ACC: 0.42677622039632673
Gaussian Naive Bayes model accuracy(in %): 40.50265828902852
[[104 144 195]
 [152 332 334]
 [141 265 402]]
              precision    recall  f1-score   support

           0       0.26      0.23      0.25       443
           1       0.45      0.41      0.43       818
           2       0.43      0.50      0.46       808

   micro avg       0.41      0.41      0.41      2069
   macro avg       0.38      0.38      0.38      2069
weighted avg       0.40      0.41      0.40      2069

counter:-  9 ACC: 0.40502658289028515
Gaussian Naive Bayes model accuracy(in %): 37.554374093765105
[[101 163 179]
 [173 312 333]
 [179 265 364]]
              precision    recall  f1-score   support

           0       0.22      0.23      0.23       443
           1       0.42      0.38      0.40       818
           2       0.42      0.45      0.43       808

   micro avg       0.38      0.38      0.38      2069
   macro avg       0.35      0.35      0.35      2069
weighted avg       0.38      0.38      0.38      2069

counter:-  10 ACC: 0.375543740937651
Best Result:= 0.42360256949063857 

{'best_acc:': 0.42360256949063857}
>>> setseed(42)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    setseed(42)
NameError: name 'setseed' is not defined
>>> set.seed(42)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set.seed(42)
AttributeError: type object 'set' has no attribute 'seed'
>>> set(42)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    set(42)
TypeError: 'int' object is not iterable
>>> seed(42)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    seed(42)
NameError: name 'seed' is not defined
>>> 
======== RESTART: D:\workspace\tipr\tipr-first-assignment\src\main.py ========
Welcome to the world of high and low dimensions!
>>> init()
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
>>> sk_fold_crossValidate(X,Y,naiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
no. of classes: 3 Data Shape: (18629, 128)
counter:-  1 ACC: 0.4025096525096525
no. of classes: 3 Data Shape: (18630, 128)
counter:-  2 ACC: 0.40994688556253017
no. of classes: 3 Data Shape: (18630, 128)
counter:-  3 ACC: 0.4398841139546113
no. of classes: 3 Data Shape: (18630, 128)
counter:-  4 ACC: 0.4505070014485756
no. of classes: 3 Data Shape: (18631, 128)
counter:-  5 ACC: 0.4444444444444444
no. of classes: 3 Data Shape: (18631, 128)
counter:-  6 ACC: 0.45169082125603865
no. of classes: 3 Data Shape: (18632, 128)
counter:-  7 ACC: 0.4485258579023683
no. of classes: 3 Data Shape: (18632, 128)
counter:-  8 ACC: 0.4224262928951184
no. of classes: 3 Data Shape: (18632, 128)
counter:-  9 ACC: 0.41324311261478974
no. of classes: 3 Data Shape: (18632, 128)
counter:-  10 ACC: 0.403093281778637
Best Result:= 0.42862714643667654 

{'best_acc:': 0.42862714643667654}
>>> sk_fold_crossValidate(X,Y,sknaiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
Gaussian Naive Bayes model accuracy(in %): 39.285714285714285
[[ 94 168 182]
 [155 351 313]
 [159 281 369]]
              precision    recall  f1-score   support

           0       0.23      0.21      0.22       444
           1       0.44      0.43      0.43       819
           2       0.43      0.46      0.44       809

   micro avg       0.39      0.39      0.39      2072
   macro avg       0.37      0.37      0.37      2072
weighted avg       0.39      0.39      0.39      2072

counter:-  1 ACC: 0.39285714285714285
Gaussian Naive Bayes model accuracy(in %): 39.2563978754225
[[107 164 173]
 [175 314 329]
 [149 268 392]]
              precision    recall  f1-score   support

           0       0.25      0.24      0.24       444
           1       0.42      0.38      0.40       818
           2       0.44      0.48      0.46       809

   micro avg       0.39      0.39      0.39      2071
   macro avg       0.37      0.37      0.37      2071
weighted avg       0.39      0.39      0.39      2071

counter:-  2 ACC: 0.392563978754225
Gaussian Naive Bayes model accuracy(in %): 43.74698213423467
[[109 152 183]
 [136 380 302]
 [131 261 417]]
              precision    recall  f1-score   support

           0       0.29      0.25      0.27       444
           1       0.48      0.46      0.47       818
           2       0.46      0.52      0.49       809

   micro avg       0.44      0.44      0.44      2071
   macro avg       0.41      0.41      0.41      2071
weighted avg       0.43      0.44      0.43      2071

counter:-  3 ACC: 0.4374698213423467
Gaussian Naive Bayes model accuracy(in %): 45.48527281506519
[[116 169 159]
 [134 400 284]
 [127 256 426]]
              precision    recall  f1-score   support

           0       0.31      0.26      0.28       444
           1       0.48      0.49      0.49       818
           2       0.49      0.53      0.51       809

   micro avg       0.45      0.45      0.45      2071
   macro avg       0.43      0.43      0.43      2071
weighted avg       0.45      0.45      0.45      2071

counter:-  4 ACC: 0.45485272815065186
Gaussian Naive Bayes model accuracy(in %): 45.507246376811594
[[139 151 153]
 [133 369 316]
 [103 272 434]]
              precision    recall  f1-score   support

           0       0.37      0.31      0.34       443
           1       0.47      0.45      0.46       818
           2       0.48      0.54      0.51       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.43      0.44      2070
weighted avg       0.45      0.46      0.45      2070

counter:-  5 ACC: 0.45507246376811594
Gaussian Naive Bayes model accuracy(in %): 45.94202898550724
[[132 144 167]
 [155 380 283]
 [134 236 439]]
              precision    recall  f1-score   support

           0       0.31      0.30      0.31       443
           1       0.50      0.46      0.48       818
           2       0.49      0.54      0.52       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.44      0.43      2070
weighted avg       0.46      0.46      0.46      2070

counter:-  6 ACC: 0.45942028985507244
Gaussian Naive Bayes model accuracy(in %): 43.64427259545674
[[118 157 168]
 [153 366 299]
 [147 242 419]]
              precision    recall  f1-score   support

           0       0.28      0.27      0.27       443
           1       0.48      0.45      0.46       818
           2       0.47      0.52      0.49       808

   micro avg       0.44      0.44      0.44      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.44      0.43      2069

counter:-  7 ACC: 0.4364427259545674
Gaussian Naive Bayes model accuracy(in %): 42.67762203963267
[[126 136 181]
 [141 351 326]
 [146 256 406]]
              precision    recall  f1-score   support

           0       0.31      0.28      0.29       443
           1       0.47      0.43      0.45       818
           2       0.44      0.50      0.47       808

   micro avg       0.43      0.43      0.43      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.43      0.43      2069

counter:-  8 ACC: 0.42677622039632673
Gaussian Naive Bayes model accuracy(in %): 40.50265828902852
[[104 144 195]
 [152 332 334]
 [141 265 402]]
              precision    recall  f1-score   support

           0       0.26      0.23      0.25       443
           1       0.45      0.41      0.43       818
           2       0.43      0.50      0.46       808

   micro avg       0.41      0.41      0.41      2069
   macro avg       0.38      0.38      0.38      2069
weighted avg       0.40      0.41      0.40      2069

counter:-  9 ACC: 0.40502658289028515
Gaussian Naive Bayes model accuracy(in %): 37.554374093765105
[[101 163 179]
 [173 312 333]
 [179 265 364]]
              precision    recall  f1-score   support

           0       0.22      0.23      0.23       443
           1       0.42      0.38      0.40       818
           2       0.42      0.45      0.43       808

   micro avg       0.38      0.38      0.38      2069
   macro avg       0.35      0.35      0.35      2069
weighted avg       0.38      0.38      0.38      2069

counter:-  10 ACC: 0.375543740937651
Best Result:= 0.42360256949063857 

{'best_acc:': 0.42360256949063857}
>>> sk_fold_crossValidate(X,Y,skKNN,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
[[138 162 144]
 [235 310 274]
 [282 251 276]]
              precision    recall  f1-score   support

           0       0.21      0.31      0.25       444
           1       0.43      0.38      0.40       819
           2       0.40      0.34      0.37       809

   micro avg       0.35      0.35      0.35      2072
   macro avg       0.35      0.34      0.34      2072
weighted avg       0.37      0.35      0.36      2072

counter:-  1 ACC: 0.34942084942084944
[[139 152 153]
 [260 302 256]
 [244 269 296]]
              precision    recall  f1-score   support

           0       0.22      0.31      0.26       444
           1       0.42      0.37      0.39       818
           2       0.42      0.37      0.39       809

   micro avg       0.36      0.36      0.36      2071
   macro avg       0.35      0.35      0.35      2071
weighted avg       0.38      0.36      0.36      2071

counter:-  2 ACC: 0.355866731047803
[[136 166 142]
 [262 300 256]
 [256 279 274]]
              precision    recall  f1-score   support

           0       0.21      0.31      0.25       444
           1       0.40      0.37      0.38       818
           2       0.41      0.34      0.37       809

   micro avg       0.34      0.34      0.34      2071
   macro avg       0.34      0.34      0.33      2071
weighted avg       0.36      0.34      0.35      2071

counter:-  3 ACC: 0.34282955094157413
[[148 146 150]
 [225 323 270]
 [245 268 296]]
              precision    recall  f1-score   support

           0       0.24      0.33      0.28       444
           1       0.44      0.39      0.42       818
           2       0.41      0.37      0.39       809

   micro avg       0.37      0.37      0.37      2071
   macro avg       0.36      0.36      0.36      2071
weighted avg       0.39      0.37      0.38      2071

counter:-  4 ACC: 0.37035248672139065
[[132 150 161]
 [241 298 279]
 [236 267 306]]
              precision    recall  f1-score   support

           0       0.22      0.30      0.25       443
           1       0.42      0.36      0.39       818
           2       0.41      0.38      0.39       809

   micro avg       0.36      0.36      0.36      2070
   macro avg       0.35      0.35      0.34      2070
weighted avg       0.37      0.36      0.36      2070

counter:-  5 ACC: 0.35555555555555557
[[138 156 149]
 [242 296 280]
 [255 266 288]]
              precision    recall  f1-score   support

           0       0.22      0.31      0.26       443
           1       0.41      0.36      0.39       818
           2       0.40      0.36      0.38       809

   micro avg       0.35      0.35      0.35      2070
   macro avg       0.34      0.34      0.34      2070
weighted avg       0.37      0.35      0.35      2070

counter:-  6 ACC: 0.34879227053140094
[[155 154 134]
 [242 306 270]
 [255 277 276]]
              precision    recall  f1-score   support

           0       0.24      0.35      0.28       443
           1       0.42      0.37      0.39       818
           2       0.41      0.34      0.37       808

   micro avg       0.36      0.36      0.36      2069
   macro avg       0.35      0.36      0.35      2069
weighted avg       0.37      0.36      0.36      2069

counter:-  7 ACC: 0.35621072982116964
[[145 156 142]
 [269 278 271]
 [270 276 262]]
              precision    recall  f1-score   support

           0       0.21      0.33      0.26       443
           1       0.39      0.34      0.36       818
           2       0.39      0.32      0.35       808

   micro avg       0.33      0.33      0.33      2069
   macro avg       0.33      0.33      0.32      2069
weighted avg       0.35      0.33      0.34      2069

counter:-  8 ACC: 0.33107781536974384
[[145 149 149]
 [254 295 269]
 [275 256 277]]
              precision    recall  f1-score   support

           0       0.22      0.33      0.26       443
           1       0.42      0.36      0.39       818
           2       0.40      0.34      0.37       808

   micro avg       0.35      0.35      0.35      2069
   macro avg       0.35      0.34      0.34      2069
weighted avg       0.37      0.35      0.35      2069

counter:-  9 ACC: 0.34654422426292897
[[137 140 166]
 [285 267 266]
 [254 269 285]]
              precision    recall  f1-score   support

           0       0.20      0.31      0.24       443
           1       0.39      0.33      0.36       818
           2       0.40      0.35      0.37       808

   micro avg       0.33      0.33      0.33      2069
   macro avg       0.33      0.33      0.33      2069
weighted avg       0.35      0.33      0.34      2069

counter:-  10 ACC: 0.333011116481392
Best Result:= 0.3489661330153808 

{'best_acc:': 0.3489661330153808}
>>> 
======== RESTART: D:\workspace\tipr\tipr-first-assignment\src\main.py ========
Welcome to the world of high and low dimensions!
>>> init()
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
Loading Already Stored File
>>> sk_fold_crossValidate(X,Y,skKNN,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
[[138 162 144]
 [235 310 274]
 [282 251 276]]
              precision    recall  f1-score   support

           0       0.21      0.31      0.25       444
           1       0.43      0.38      0.40       819
           2       0.40      0.34      0.37       809

   micro avg       0.35      0.35      0.35      2072
   macro avg       0.35      0.34      0.34      2072
weighted avg       0.37      0.35      0.36      2072

counter:-  1 ACC: 0.34942084942084944
[[139 152 153]
 [260 302 256]
 [244 269 296]]
              precision    recall  f1-score   support

           0       0.22      0.31      0.26       444
           1       0.42      0.37      0.39       818
           2       0.42      0.37      0.39       809

   micro avg       0.36      0.36      0.36      2071
   macro avg       0.35      0.35      0.35      2071
weighted avg       0.38      0.36      0.36      2071

counter:-  2 ACC: 0.355866731047803
[[136 166 142]
 [262 300 256]
 [256 279 274]]
              precision    recall  f1-score   support

           0       0.21      0.31      0.25       444
           1       0.40      0.37      0.38       818
           2       0.41      0.34      0.37       809

   micro avg       0.34      0.34      0.34      2071
   macro avg       0.34      0.34      0.33      2071
weighted avg       0.36      0.34      0.35      2071

counter:-  3 ACC: 0.34282955094157413
[[148 146 150]
 [225 323 270]
 [245 268 296]]
              precision    recall  f1-score   support

           0       0.24      0.33      0.28       444
           1       0.44      0.39      0.42       818
           2       0.41      0.37      0.39       809

   micro avg       0.37      0.37      0.37      2071
   macro avg       0.36      0.36      0.36      2071
weighted avg       0.39      0.37      0.38      2071

counter:-  4 ACC: 0.37035248672139065
[[132 150 161]
 [241 298 279]
 [236 267 306]]
              precision    recall  f1-score   support

           0       0.22      0.30      0.25       443
           1       0.42      0.36      0.39       818
           2       0.41      0.38      0.39       809

   micro avg       0.36      0.36      0.36      2070
   macro avg       0.35      0.35      0.34      2070
weighted avg       0.37      0.36      0.36      2070

counter:-  5 ACC: 0.35555555555555557
[[138 156 149]
 [242 296 280]
 [255 266 288]]
              precision    recall  f1-score   support

           0       0.22      0.31      0.26       443
           1       0.41      0.36      0.39       818
           2       0.40      0.36      0.38       809

   micro avg       0.35      0.35      0.35      2070
   macro avg       0.34      0.34      0.34      2070
weighted avg       0.37      0.35      0.35      2070

counter:-  6 ACC: 0.34879227053140094
[[155 154 134]
 [242 306 270]
 [255 277 276]]
              precision    recall  f1-score   support

           0       0.24      0.35      0.28       443
           1       0.42      0.37      0.39       818
           2       0.41      0.34      0.37       808

   micro avg       0.36      0.36      0.36      2069
   macro avg       0.35      0.36      0.35      2069
weighted avg       0.37      0.36      0.36      2069

counter:-  7 ACC: 0.35621072982116964
[[145 156 142]
 [269 278 271]
 [270 276 262]]
              precision    recall  f1-score   support

           0       0.21      0.33      0.26       443
           1       0.39      0.34      0.36       818
           2       0.39      0.32      0.35       808

   micro avg       0.33      0.33      0.33      2069
   macro avg       0.33      0.33      0.32      2069
weighted avg       0.35      0.33      0.34      2069

counter:-  8 ACC: 0.33107781536974384
[[145 149 149]
 [254 295 269]
 [275 256 277]]
              precision    recall  f1-score   support

           0       0.22      0.33      0.26       443
           1       0.42      0.36      0.39       818
           2       0.40      0.34      0.37       808

   micro avg       0.35      0.35      0.35      2069
   macro avg       0.35      0.34      0.34      2069
weighted avg       0.37      0.35      0.35      2069

counter:-  9 ACC: 0.34654422426292897
[[137 140 166]
 [285 267 266]
 [254 269 285]]
              precision    recall  f1-score   support

           0       0.20      0.31      0.24       443
           1       0.39      0.33      0.36       818
           2       0.40      0.35      0.37       808

   micro avg       0.33      0.33      0.33      2069
   macro avg       0.33      0.33      0.33      2069
weighted avg       0.35      0.33      0.34      2069

counter:-  10 ACC: 0.333011116481392
Best Result:= 0.3489661330153808 

{'best_acc:': 0.3489661330153808}
>>> sk_fold_crossValidate(X,Y,naiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
no. of classes: 3 Data Shape: (18629, 128)
counter:-  1 ACC: 0.4025096525096525
no. of classes: 3 Data Shape: (18630, 128)
counter:-  2 ACC: 0.40994688556253017
no. of classes: 3 Data Shape: (18630, 128)
counter:-  3 ACC: 0.4398841139546113
no. of classes: 3 Data Shape: (18630, 128)
counter:-  4 ACC: 0.4505070014485756
no. of classes: 3 Data Shape: (18631, 128)
counter:-  5 ACC: 0.4444444444444444
no. of classes: 3 Data Shape: (18631, 128)
counter:-  6 ACC: 0.45169082125603865
no. of classes: 3 Data Shape: (18632, 128)
counter:-  7 ACC: 0.4485258579023683
no. of classes: 3 Data Shape: (18632, 128)
counter:-  8 ACC: 0.4224262928951184
no. of classes: 3 Data Shape: (18632, 128)
counter:-  9 ACC: 0.41324311261478974
no. of classes: 3 Data Shape: (18632, 128)
counter:-  10 ACC: 0.403093281778637
Best Result:= 0.42862714643667654 

{'best_acc:': 0.42862714643667654}
>>> sk_fold_crossValidate(X,Y,sknaiveClass,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
Gaussian Naive Bayes model accuracy(in %): 39.285714285714285
[[ 94 168 182]
 [155 351 313]
 [159 281 369]]
              precision    recall  f1-score   support

           0       0.23      0.21      0.22       444
           1       0.44      0.43      0.43       819
           2       0.43      0.46      0.44       809

   micro avg       0.39      0.39      0.39      2072
   macro avg       0.37      0.37      0.37      2072
weighted avg       0.39      0.39      0.39      2072

counter:-  1 ACC: 0.39285714285714285
Gaussian Naive Bayes model accuracy(in %): 39.2563978754225
[[107 164 173]
 [175 314 329]
 [149 268 392]]
              precision    recall  f1-score   support

           0       0.25      0.24      0.24       444
           1       0.42      0.38      0.40       818
           2       0.44      0.48      0.46       809

   micro avg       0.39      0.39      0.39      2071
   macro avg       0.37      0.37      0.37      2071
weighted avg       0.39      0.39      0.39      2071

counter:-  2 ACC: 0.392563978754225
Gaussian Naive Bayes model accuracy(in %): 43.74698213423467
[[109 152 183]
 [136 380 302]
 [131 261 417]]
              precision    recall  f1-score   support

           0       0.29      0.25      0.27       444
           1       0.48      0.46      0.47       818
           2       0.46      0.52      0.49       809

   micro avg       0.44      0.44      0.44      2071
   macro avg       0.41      0.41      0.41      2071
weighted avg       0.43      0.44      0.43      2071

counter:-  3 ACC: 0.4374698213423467
Gaussian Naive Bayes model accuracy(in %): 45.48527281506519
[[116 169 159]
 [134 400 284]
 [127 256 426]]
              precision    recall  f1-score   support

           0       0.31      0.26      0.28       444
           1       0.48      0.49      0.49       818
           2       0.49      0.53      0.51       809

   micro avg       0.45      0.45      0.45      2071
   macro avg       0.43      0.43      0.43      2071
weighted avg       0.45      0.45      0.45      2071

counter:-  4 ACC: 0.45485272815065186
Gaussian Naive Bayes model accuracy(in %): 45.507246376811594
[[139 151 153]
 [133 369 316]
 [103 272 434]]
              precision    recall  f1-score   support

           0       0.37      0.31      0.34       443
           1       0.47      0.45      0.46       818
           2       0.48      0.54      0.51       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.43      0.44      2070
weighted avg       0.45      0.46      0.45      2070

counter:-  5 ACC: 0.45507246376811594
Gaussian Naive Bayes model accuracy(in %): 45.94202898550724
[[132 144 167]
 [155 380 283]
 [134 236 439]]
              precision    recall  f1-score   support

           0       0.31      0.30      0.31       443
           1       0.50      0.46      0.48       818
           2       0.49      0.54      0.52       809

   micro avg       0.46      0.46      0.46      2070
   macro avg       0.44      0.44      0.43      2070
weighted avg       0.46      0.46      0.46      2070

counter:-  6 ACC: 0.45942028985507244
Gaussian Naive Bayes model accuracy(in %): 43.64427259545674
[[118 157 168]
 [153 366 299]
 [147 242 419]]
              precision    recall  f1-score   support

           0       0.28      0.27      0.27       443
           1       0.48      0.45      0.46       818
           2       0.47      0.52      0.49       808

   micro avg       0.44      0.44      0.44      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.44      0.43      2069

counter:-  7 ACC: 0.4364427259545674
Gaussian Naive Bayes model accuracy(in %): 42.67762203963267
[[126 136 181]
 [141 351 326]
 [146 256 406]]
              precision    recall  f1-score   support

           0       0.31      0.28      0.29       443
           1       0.47      0.43      0.45       818
           2       0.44      0.50      0.47       808

   micro avg       0.43      0.43      0.43      2069
   macro avg       0.41      0.41      0.41      2069
weighted avg       0.43      0.43      0.43      2069

counter:-  8 ACC: 0.42677622039632673
Gaussian Naive Bayes model accuracy(in %): 40.50265828902852
[[104 144 195]
 [152 332 334]
 [141 265 402]]
              precision    recall  f1-score   support

           0       0.26      0.23      0.25       443
           1       0.45      0.41      0.43       818
           2       0.43      0.50      0.46       808

   micro avg       0.41      0.41      0.41      2069
   macro avg       0.38      0.38      0.38      2069
weighted avg       0.40      0.41      0.40      2069

counter:-  9 ACC: 0.40502658289028515
Gaussian Naive Bayes model accuracy(in %): 37.554374093765105
[[101 163 179]
 [173 312 333]
 [179 265 364]]
              precision    recall  f1-score   support

           0       0.22      0.23      0.23       443
           1       0.42      0.38      0.40       818
           2       0.42      0.45      0.43       808

   micro avg       0.38      0.38      0.38      2069
   macro avg       0.35      0.35      0.35      2069
weighted avg       0.38      0.38      0.38      2069

counter:-  10 ACC: 0.375543740937651
Best Result:= 0.42360256949063857 

{'best_acc:': 0.42360256949063857}
>>> sk_fold_crossValidate(X,Y,skKNN,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    sk_fold_crossValidate(X,Y,skKNN,10)
  File "D:\workspace\tipr\tipr-first-assignment\src\main.py", line 46, in sk_fold_crossValidate
    tmp=model(X_train, X_test, Y_train, Y_test)
  File "D:\workspace\tipr\tipr-first-assignment\src\main.py", line 116, in skKNN
    y_pred = classifier.predict(X_test)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\neighbors\classification.py", line 149, in predict
    neigh_dist, neigh_ind = self.kneighbors(X)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\neighbors\base.py", line 455, in kneighbors
    for s in gen_even_slices(X.shape[0], n_jobs)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\parallel.py", line 917, in __call__
    if self.dispatch_one_batch(iterator):
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\parallel.py", line 759, in dispatch_one_batch
    self._dispatch(tasks)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\parallel.py", line 716, in _dispatch
    job = self._backend.apply_async(batch, callback=cb)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\_parallel_backends.py", line 182, in apply_async
    result = ImmediateResult(func)
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\_parallel_backends.py", line 549, in __init__
    self.results = batch()
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\parallel.py", line 225, in __call__
    for func, args, kwargs in self.items]
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\externals\joblib\parallel.py", line 225, in <listcomp>
    for func, args, kwargs in self.items]
  File "D:\Program Files\python\python36\lib\site-packages\sklearn\neighbors\base.py", line 292, in _tree_query_parallel_helper
    return tree.query(data, n_neighbors, return_distance)
KeyboardInterrupt

>>> sk_fold_crossValidate(X,Y,KNN,10)
StratifiedKFold(n_splits=10, random_state=None, shuffle=False)
              precision    recall  f1-score   support

           0       0.25      0.01      0.03       444
           1       0.42      0.23      0.30       819
           2       0.40      0.79      0.53       809

   micro avg       0.40      0.40      0.40      2072
   macro avg       0.36      0.35      0.29      2072
weighted avg       0.38      0.40      0.33      2072

counter:-  1 ACC: 0.402992277992278
              precision    recall  f1-score   support

           0       0.19      0.01      0.03       444
           1       0.39      0.22      0.28       818
           2       0.39      0.77      0.52       809

   micro avg       0.39      0.39      0.39      2071
   macro avg       0.32      0.33      0.28      2071
weighted avg       0.35      0.39      0.32      2071

counter:-  2 ACC: 0.3901496861419604
              precision    recall  f1-score   support

           0       0.39      0.02      0.03       444
           1       0.42      0.26      0.32       818
           2       0.40      0.76      0.53       809

   micro avg       0.41      0.41      0.41      2071
   macro avg       0.40      0.35      0.29      2071
weighted avg       0.41      0.41      0.34      2071

counter:-  3 ACC: 0.4056011588604539
              precision    recall  f1-score   support

           0       0.18      0.01      0.02       444
           1       0.41      0.25      0.31       818
           2       0.39      0.76      0.52       809

   micro avg       0.40      0.40      0.40      2071
   macro avg       0.33      0.34      0.28      2071
weighted avg       0.36      0.40      0.33      2071

counter:-  4 ACC: 0.39546112988894255
              precision    recall  f1-score   support

           0       0.16      0.01      0.02       443
           1       0.42      0.23      0.30       818
           2       0.41      0.81      0.54       809

   micro avg       0.41      0.41      0.41      2070
   macro avg       0.33      0.35      0.29      2070
weighted avg       0.36      0.41      0.33      2070

counter:-  5 ACC: 0.40869565217391307
              precision    recall  f1-score   support

           0       0.14      0.01      0.01       443
           1       0.41      0.22      0.29       818
           2       0.40      0.79      0.53       809

   micro avg       0.40      0.40      0.40      2070
   macro avg       0.31      0.34      0.28      2070
weighted avg       0.35      0.40      0.32      2070

counter:-  6 ACC: 0.39806763285024155
              precision    recall  f1-score   support

           0       0.16      0.01      0.02       443
           1       0.41      0.24      0.30       818
           2       0.39      0.76      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.32      0.34      0.28      2069
weighted avg       0.35      0.39      0.33      2069

counter:-  7 ACC: 0.39342677622039635
              precision    recall  f1-score   support

           0       0.35      0.01      0.03       443
           1       0.39      0.21      0.27       818
           2       0.39      0.77      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.38      0.33      0.27      2069
weighted avg       0.38      0.39      0.32      2069

counter:-  8 ACC: 0.3895601739971
              precision    recall  f1-score   support

           0       0.09      0.00      0.01       443
           1       0.41      0.23      0.30       818
           2       0.40      0.78      0.53       808

   micro avg       0.40      0.40      0.40      2069
   macro avg       0.30      0.34      0.28      2069
weighted avg       0.33      0.40      0.32      2069

counter:-  9 ACC: 0.3958434026099565
              precision    recall  f1-score   support

           0       0.07      0.00      0.01       443
           1       0.38      0.22      0.28       818
           2       0.39      0.77      0.52       808

   micro avg       0.39      0.39      0.39      2069
   macro avg       0.28      0.33      0.27      2069
weighted avg       0.32      0.39      0.31      2069

counter:-  10 ACC: 0.38569357177380376
Best Result:= 0.39654914625090465 

{'best_acc:': 0.39654914625090465}
>>> 
