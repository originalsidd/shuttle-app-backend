from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')

x = df.iloc[:,:-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state=41)

labels = ['Random Forest', 'KNN', 'Logistic Regression', 'SVM', 'Naive Bayes']
accuracies = []
f1_scores = []

clf = RandomForestClassifier(n_estimators = 100, random_state=42)
clf.fit(X_train.values, y_train.values)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
accuracies.append(accuracy)
f1_scores.append(f1)
print("\nRandom Forest Accuracy:", accuracy)
print("Random Forest F1 Score:", f1)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
accuracies.append(accuracy)
f1_scores.append(f1)
print("\nKNN Accuracy:", accuracy)
print("KNN F1 Score:", f1)

lr = LogisticRegression(random_state=42)
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
accuracies.append(accuracy)
f1_scores.append(f1)
print("\nLogistic Regression Accuracy:", accuracy)
print("Logistic Regression F1 Score:", f1)

svc = SVC(random_state=42)
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
accuracies.append(accuracy)
f1_scores.append(f1)
print("\nSVM Accuracy:", accuracy)
print("SVM F1 Score:", f1)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
y_pred = gnb.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')
accuracies.append(accuracy)
f1_scores.append(f1)
print("\nNaive Bayes Accuracy:", accuracy)
print("Naive Bayes F1 Score:", f1)

# Chart
plt.bar(labels, accuracies)
plt.title('Model Accuracies')
plt.xlabel('Model')
plt.ylabel('Accuracy')
plt.show()

plt.bar(labels, f1_scores)
plt.title('Model F1 Scores')
plt.xlabel('Model')
plt.ylabel('F1 Score')
plt.show()

# Save the model as a file
joblib.dump(clf, 'model.joblib')