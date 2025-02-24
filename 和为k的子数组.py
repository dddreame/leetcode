from collections import defaultdict

def subarraySum(nums,k):
    ans= s = 0
    cnt = defaultdict(int)
    cnt[0] = 1
    for i,v in enumerate(nums):
        s += v
        ans += cnt[s-k]
        cnt[s] += 1
    return ans

nums_str = input()
nums_str = nums_str.strip('[]')
nums = [int(num) for num in nums_str.split(',')]
k_str = input()
k = int(k_str)
result = subarraySum(nums,k)
print(result)