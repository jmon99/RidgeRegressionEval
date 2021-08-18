import numpy as np

from boxplot import boxplot
from evaluate import evaluate
from svm import Svm

from sklearn.datasets import load_boston

X, y = load_boston(return_X_y = True)
names, scores = evaluate(X, y, ridge_selected = True, lsqr_selected = True, svm_selected=True, kernel='linear')

for i,name in enumerate(names):
  print(name,": ", np.mean(scores[i]))

boxplot(names, scores)
