from math import inf

def maxsubarray(nums) :
    minsum,presum = 0,0
    ans = -inf
    for v in nums:
        presum += v
        ans = max(ans,presum - minsum)
        minsum = min(minsum,presum)
    return ans

nums_str = input()
nums_str = nums_str.strip('[]')
nums = [int(num) for num in nums_str.split(',')]
result = maxsubarray(nums)
print(result)
