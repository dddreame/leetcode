import ast

def productExceptSelf(nums):
    n = len(nums)
    sufsum = [1]*n
    for i in range(n-2,-1,-1):
        sufsum[i] = sufsum[i+1] * nums[i+1]

    presum = 1
    for i in range(n):
        sufsum[i] = sufsum[i] * presum
        presum *= nums[i]
    return sufsum

nums = ast.literal_eval(input())
print(productExceptSelf(nums))