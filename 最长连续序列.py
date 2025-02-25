import ast

def longestConsecutive(nums):
    num_set = set(nums)
    ans = 0
    for num in nums:
        # 检查是否是连续序列的起始数字
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            # 不断检查下一个连续数字
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            # 更新最长连续序列的长度
            ans = max(ans, current_streak)
    return ans

if __name__ == "__main__":
    # 自定义输入
    nums = ast.literal_eval(input())
     
    # 调用函数计算结果
    result = longestConsecutive(nums)
    # 输出结果
    print("最长连续序列的长度是:", result)