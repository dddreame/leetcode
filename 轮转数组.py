import ast
def rotate(nums,k):
    n = len(nums)
    ans = []
    for i in range(n):
        ans.append(nums[(n-k+i)%n])
    nums[:] = ans


nums = ast.literal_eval(input())
k = int(input())
rotate(nums,k)
print(nums)