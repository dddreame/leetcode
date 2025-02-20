# 定义 threeSum 函数用于找出数组中所有和为 0 的不重复三元组
def threeSum(nums):
    # 首先对输入的数组进行排序
    nums.sort()
    n = len(nums)
    ans = []
    # 遍历数组，因为要找三元组，所以只需要遍历到倒数第三个元素
    for i in range(n - 2):
        # 跳过重复的元素，避免结果中出现重复的三元组
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 优化一：如果当前元素和其后两个元素的和大于 0，由于数组已排序，后续组合和必然大于 0，可直接跳出循环
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break
        # 优化二：如果当前元素和数组最后两个元素的和小于 0，说明当前元素过小，跳过当前元素
        if nums[i] + nums[n - 2] + nums[n - 1] < 0:
            continue
        # 初始化左右指针
        j, k = i + 1, n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s > 0:
                # 和大于 0，右指针左移
                k -= 1
            elif s < 0:
                # 和小于 0，左指针右移
                j += 1
            else:
                # 和等于 0，找到一个符合条件的三元组
                ans.append([nums[i], nums[j], nums[k]])
                # 跳过重复元素，避免结果中出现重复的三元组
                while j + 1 < k and nums[j] == nums[j + 1]:
                    j += 1
                while k - 1 > j and nums[k] == nums[k - 1]:
                    k -= 1
                # 移动左右指针继续寻找其他可能的组合
                j += 1
                k -= 1
    return ans

# 从用户输入获取数组元素，元素之间用逗号分隔
input_str = input()
input_str = input_str.strip('[]')
# 将输入的字符串按逗号分割并转换为整数列表
nums = [int(x) for x in input_str.split(',')]
# 调用 threeSum 函数找出所有和为 0 的不重复三元组
result = threeSum(nums)
# 输出结果
print("和为 0 的不重复三元组是:", result)
