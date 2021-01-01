import numpy as np
import pandas as pd


# # we can specify a delimiter by putting ("filedir", delimiter = " ")
df = pd.read_csv("~/Desktop/Coding/Python_Practice/SmallProject/input.csv")

# numpy array: single data type
# python list: multiple data types

# put a csv to a numpy array (then we can use the numpy library)
input_matrix = df.to_numpy()  # arrays (2D, 3D)

a = input_matrix[:-1]
b = input_matrix[-1]

# print(a, b)

x = np.linalg.solve(a, b)
print(x)
