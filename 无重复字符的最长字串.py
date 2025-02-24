from collections import defaultdict

def longest(str):
    cnt = defaultdict(int)
    left, ans =0,0
    for right,v in enumerate(str):
        cnt[v] += 1
        while cnt[v] > 1:
            cnt[str[left]] -= 1
            left += 1
        ans = max(ans,right - left + 1) 
    return ans   

nums_str = input()
result = longest(nums_str)
print(result)
