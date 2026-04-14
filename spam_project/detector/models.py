import pandas as pd
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv("titanic.csv")

df = df[['Survived','Pclass','Sex','Age','Fare']]

df['Age'].fillna(df['Age'].mean(),inplace = True)

df['Sex'] = df['Sex'].map({'male' : 0,'female': 1})

X = df[['Pclass', 'Sex', 'Age', 'Fare']]  
y = df['Survived']

model = GaussianNB()
model.fit(X,y)
