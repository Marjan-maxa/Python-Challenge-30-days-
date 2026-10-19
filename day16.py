import pandas as p

df=p.read_csv("students.csv")
print(df)

print("------------------------------")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df["name"])

print(df[df["department"]=="CSE"])
print("-------------------------------")
print(df[df["cgpa"]>=3.50])


print(df.isnull().sum())
print("------------------------")
clean_data=df.dropna(subset="cgpa")
print(df)
department_average = df.groupby("department")["cgpa"].mean()
print("Average CGPA :")
print(department_average)

sorted_value=df.sort_values(by="cgpa",ascending=False)
print(sorted_value)