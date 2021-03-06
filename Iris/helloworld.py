from sklearn.datasets import load_iris
import numpy as np
from sklearn.externals.six import StringIO
import pydot
from sklearn import tree
iris=load_iris()
print(iris.feature_names)
print(iris.target_names)
test_idx = [0,50,100]

#training data
train_target = np.delete(iris.target, test_idx)
train_data= np.delete(iris.data,test_idx,axis=0)

#testing data
test_target =iris.target[test_idx]
test_data=iris.data[test_idx]

clf=tree.DecisionTreeClassifier()
clf= clf.fit(train_data,train_target)
print(test_target)
print(clf.predict(test_data))
print("Generating as irisTree.dot...")
tree.export_graphviz(clf,
out_file="irisTree.dot",  feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True) 
