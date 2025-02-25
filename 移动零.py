import ast

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

nums = ast.literal_eval(input())
 
moveZeroes(nums)
print("移动零后的列表:", nums)

	

# class Solution:
# def moveZeroes(self, nums: list[int]) -> None:
# # 方法实现
# slow = 0
# for fast in range(len(nums)):
# if nums[fast] != 0:
# nums[slow], nums[fast] = nums[fast], nums[slow]
# slow += 1

# # 创建类的实例
# solution = Solution()
# nums = [0, 1, 0, 3, 12]
# solution.moveZeroes(nums)
# print(nums)