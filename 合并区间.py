import ast

def merge(nums):
    nums.sort(key=lambda x: x[0])
    ans = []
    for p in nums:
        if ans and p[0] <= ans[-1][-1]:
            ans[-1][-1] = max(ans[-1][-1], p[1])
        else:
            ans.append(p)
    return ans

nums_str = input()
nums = ast.literal_eval(nums_str)  # 使用 ast.literal_eval 解析输入字符串
result = merge(nums)
print(result)
