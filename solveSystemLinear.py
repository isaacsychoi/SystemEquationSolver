import numpy as np
import pandas as pd


def list_formator(input_list):
    rtn_list = []

    for each in input_list:
        x = round(each, 3)
        rtn_list.append(x)
    return rtn_list


# size = int(input("Dimension: ?"))

# a delimiter by putting ("filedir", delimiter = " ")
df = pd.read_csv("./input.csv")

# put a csv to a numpy array
input_matrix = df.to_numpy()  # arrays (2D, 3D)

# (             |     )
# (      A      |  B  )
# (             |     )

# everything but the last column
a = input_matrix[:, :-1]
# last column
b = input_matrix[:, -1]

# debug print
print("The A matrix is: \n{}".format(a))
print("-----------------")
print("The B matrix is: \n{}".format(b))

x = np.linalg.solve(a, b)

print("Answers:")
print(list(df.columns[:-1]))
print(list_formator(x))
