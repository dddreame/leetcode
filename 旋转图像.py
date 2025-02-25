import copy
import ast
def rotate(matrix):
    n = len(matrix)
    tmp = copy.deepcopy(matrix)
    for i in range(n):
        for j in range(n):
            matrix[j][n - 1 - i] = tmp[i][j]

matrix = ast.literal_eval(input())
rotate(matrix)
print(matrix)