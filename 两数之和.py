def two_sum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i
    return None

if __name__ == "__main__":
 # 输入数组
 nums_str = input()
 nums_list = nums_str.split(',')
 nums = [int(num) for num in nums_list]
 target_str = input("请输入目标值: ")
 target = int(target_str)

 # 执行算法
 result = two_sum(nums, target)

 # 输出结果
 if result:
    print(f"输出: [{result[0]}, {result[1]}]")
else:
    print("没有找到解决方案")
