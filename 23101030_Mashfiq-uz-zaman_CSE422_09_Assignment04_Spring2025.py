import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report,roc_auc_score, roc_curve


heart = pd.read_csv("heart.csv")  
#print(heart.head(5))
#print(heart.isnull().sum())
#print(heart.describe())
#print(heart.dtypes)

from sklearn.impute import SimpleImputer
numerical_value= SimpleImputer(strategy='median')
heart[['cigsPerDay', 'BPMeds','BMI',  'totChol','heartRate','glucose']]=numerical_value.fit_transform(heart[['cigsPerDay', 'BPMeds','totChol','BMI',  'heartRate','glucose']])

catagory_value=SimpleImputer(strategy='most_frequent')
heart[['education']]=catagory_value.fit_transform(heart[['education']])

print(heart.isnull().sum())  #all null value gone now
heart['gender']=heart['gender'].map({'Male': 1, 'Female': 0})

x=heart.drop('Heart Disease (in next 10 years)', axis=1)
y=heart['Heart Disease (in next 10 years)']

x_train,x_test,y_train,y_test=train_test_split( x, y, test_size=0.3, random_state=44)
scaler = StandardScaler()

x_train_scale=scaler.fit_transform(x_train)
x_test_scale=scaler.fit_transform(x_test)
x_train_scale = pd.DataFrame(x_train_scale,columns=x_train.columns)
print("scaling done. scaled training data sample: ")
print(x_train_scale.head())

l_reg= LogisticRegression(random_state=44)
l_reg.fit(x_train_scale, y_train)
y_red_predict= l_reg.predict(x_test_scale)
print("Accuracy:", accuracy_score(y_test, y_red_predict))
print("\n Classification Report:\n", classification_report(y_test, y_red_predict))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_red_predict))

prob_y=l_reg.predict_proba(x_test_scale)[:,1]   
auc_l=roc_auc_score(y_test,prob_y)             

print(auc_l)

fpr_log, tpr_log, _ = roc_curve(y_test, prob_y)
plt.plot(fpr_log, tpr_log, label=f"AUC = {auc_l:.2f}")
plt.plot([0,1],[0,1],'--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve for Logistic Regression')
plt.legend()
plt.grid(True)
plt.show()