import numpy as np

marks=np.array([23,65,98,97,54, 78])
print("Marks :",marks)
print("Total :",np.sum(marks))
print("Average :",round(np.mean(marks),2))
print("Highest :",np.max(marks))
print("Lowest :",np.min(marks))