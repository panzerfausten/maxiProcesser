from sklearn import svm
X = [[-1,2.5641035167489541,2.3575090136681283,[-1]],[2,2.6871875802672665,2.3575090136681283,[0]]] 
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)  


svm.SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
shrinking=True, tol=0.001, verbose=False)
print clf.predict( [2,3.1683541727603446,2.7388593553507725])
