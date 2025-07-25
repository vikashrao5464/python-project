# -*- coding: utf-8 -*-
"""project 05(loan prediction).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Px06w18mfDMdjURd69Eed-1zHfWT6TVV
"""

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

loan_dataset=pd.read_csv('/content/train_u6lujuX_CVtuZ9i (1).csv')

loan_dataset.head()

loan_dataset.shape

# some statical message
loan_dataset.describe()

loan_dataset.isnull().sum()

loan_dataset=loan_dataset.dropna()

loan_dataset.isnull().sum()

print(loan_dataset.columns)

print("Unique values before cleaning:", loan_dataset['Loan_Status'].unique())

loan_dataset.head()

loan_dataset['Loan_Status'] = loan_dataset['Loan_Status'].replace({'N': 0, 'Y': 1})

loan_dataset.head()

loan_dataset['Dependents'].unique()

loan_dataset=loan_dataset.replace(to_replace='3+',value=4)

loan_dataset['Dependents'].unique()

"""data visulization

"""

# education and loan status
sns.countplot(x='Education',hue='Loan_Status',data=loan_dataset)

#marital status ans loan status
sns.countplot(x='Married',hue='Loan_Status',data=loan_dataset)

loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},
                      'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)

loan_dataset.head()

#seperating tha data and label
X=loan_dataset.drop(columns=['Loan_ID','Loan_Status'],axis=1)
Y=loan_dataset['Loan_Status']

print(X)

print(Y)

# train test and split the data
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1,stratify=Y,random_state=2)

print(X.shape,X_train.shape,X_test.shape)

# model training

classifier=svm.SVC(kernel='linear')

classifier.fit(X_train,Y_train)

#model evaluation

X_train_prediction=classifier.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction,Y_train)

print('accuracy on training data:',training_data_accuracy)

X_test_prediction=classifier.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction,Y_test)

print('accuracy on test data:',test_data_accuracy)

def predict_loan_approval(input_data ):

    # Convert to NumPy array
    input_array = np.asarray(input_data).reshape(1, -1)



    # Predict
    prediction = classifier.predict(input_array)

    if prediction[0] == 1:
        return "✅ Loan Approved"
    else:
        return "❌ Loan Not Approved"

#predictive system

from inspect import indentsize
gender = int(input("Enter Gender (1=Male, 0=Female): "))
married = int(input("Married (1=Yes, 0=No): "))
dependents=int(input("Dependents: "))
education = int(input("Education (1=Graduate, 0=Not Graduate): "))
self_employed = int(input("Self Employed (1=Yes, 0=No): "))
applicant_income = int(input("Applicant Income: "))
coapplicant_income = int(input("Coapplicant Income: "))
loan_amount = int(input("Loan Amount: "))
loan_term = int(input("Loan Term (in days): "))
credit_history = int(input("Credit History (1 or 0): "))
property_area = int(input("Property Area (0=Rural, 1=Semiurban, 2=Urban): "))

user_input = [
    gender, married,dependents, education, self_employed,
    applicant_income, coapplicant_income,
    loan_amount, loan_term, credit_history, property_area
]

result = predict_loan_approval(user_input)
print("\nPrediction:", result)

