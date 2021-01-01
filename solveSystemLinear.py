import numpy as np
import pandas as pd


# a delimiter by putting ("filedir", delimiter = " ")
df = pd.read_csv("./input.csv")

# put a csv to a numpy array 
input_matrix = df.to_numpy()  # arrays (2D, 3D)

# everything but the last column
a = input_matrix[:,:-1]
# last column
b = input_matrix[:,-1]

# debug print
print(a)
print("--------")
print(b)

x = np.linalg.solve(a, b)
print(x)
