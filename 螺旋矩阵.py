import ast
dirs = (0,1), (1,0), (0,-1), (-1,0)

def spiralOrder(matrix):
    m,n = len(matrix),len(matrix[0])
    size = m*n
    ans = []
    i,j,di = 0,-1,0
    while len(ans) < size:
        dx,dy = dirs[di]
        for _ in range(n):
            i += dx
            j += dy
            ans.append(matrix[i][j])
        di = (di+1)%4
        n,m = m-1,n
    return ans

matrix = ast.literal_eval(input())
print(spiralOrder(matrix))

