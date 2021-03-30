import numpy as np

# CREATE A MATRIX USING USER INPUT
# row = int(input("Enter number of rows:"))
# columns = int(input("Enter the number of columns:"))
# print("Enter the numbers in a single line separated by space")
# values = list(map(int, input().split()))
# matrix = np.array(values).reshape(row, columns)
# print(matrix)

# CREATE AN EMPTY MATRIX
# m = np.empty((0, 0))
# print(m)

# CREATE A MATRIX IN PYTHON 3
# m = np.matrix([[3, 4], [5, 2]])
# print("Matrix is:\n", m)

# MATRIX MULTIPLICATION
# mat1 = np.matrix([[2, 5], [4, 1]])
# mat2 = np.matrix([[6, 5], [4, 7]])
# matrix_result = np.multiply(mat1, mat2)
# print(matrix_result)

# CREATE A MATRIX USING A FOR LOOP
# c_size = int(input("Enter size of column: "))
# r_size = int(input("Enter size of row: "))
# x = []
# y = []
# for j in range(0, c_size):
#     y.append(0)
# for i in range(0, r_size):
#     x.append(y)
# print(x)

# CREATE A MATRIX USING A LIST
# mat = np.array([[1, 3, 2], [5, 6, 4]])
# print(mat)

# CREATE A MATRIX OF ZEROS
# zero_matrix = np.zeros((3, 7))
# print(zero_matrix)

# CREATE A MATRIX WITH RANDOM DATA
ran_matrix = np.random.randint(50, size = (6, 4))
print(ran_matrix)

