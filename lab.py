
import pandas as pd
import numpy as np
# Sample data
data = {
    'Name': ['rahim','karim','sumaiya','rahim','nabila','hasan','farhan','mim'],
    'Age': [25, 30,np.nan,25,120,-5,28,35],
    'Department': ['cse', 'eee', 'cse', 'cse',
                   'bba', 'eee', 'cse', 'bba'],
    'Salary': [50000, 60000, 75000, 50000,45000,55000,np.nan,65000]
}

df = pd.DataFrame(data)
print("Original DataFrame")
print(df)
# Display first five rows
print("First five rows:")
print(df.head(5))
# Display shape
print("\nShape:")
print(df.shape)
# Display column names
print("\nColumn names:")
print(df.columns.tolist())
# Question 2: Remove duplicate rows
df = df.drop_duplicates()
print("After removing duplicates:")
print(df)
# Question 3: Identify missing values
print("\nMissing values before filling :")
print(df.isnull().sum())
# Fill missing Age and Salary with their means
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("\nAfter filling missing values:")
print(df)
# Question 4: Convert Name and Department to uppercase
df["Name"]=df['Name'].str.upper()
df['Department']=df['Department'].str.upper()
#Remove Salary column
df=df.drop(columns=['Salary'])
print("\nAfter uppercase conversion and removing Salary:")
print(df)
# Question 5: Convert Age to integer
df['Age'] = df['Age'].astype(int)
# Remove invalid ages
df = df[(df['Age'] > 0) & (df['Age'] < 100)]
df=df.reset_index(drop=True)
print("\nRemaining missing values:")
print(df.isnull().sum())
print("Final Cleaned Data :")
print(df)
