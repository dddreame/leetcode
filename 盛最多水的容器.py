# 定义一个函数用于计算最大面积
def maxArea(height):
    # 初始化左右指针
    left, right = 0, len(height) - 1
    # 初始化最大面积为 0
    ans = 0
    # 当左指针小于右指针时进行循环
    while left < right:
        # 计算当前面积
        area = (right - left) * min(height[left], height[right])
        # 更新最大面积
        ans = max(area, ans)
        # 如果左指针指向的高度小于右指针指向的高度，左指针右移
        if height[left] < height[right]:
            left += 1
        # 否则，右指针左移
        else:
            right -= 1
    return ans

# 从用户输入获取高度列表
input_str = input("请输入高度列表，用逗号分隔每个高度值: ")
input_str = input_str.strip('[]')
# 将输入的字符串按逗号分割并转换为整数列表
height = [int(x) for x in input_str.split(',')]
# 调用 maxArea 函数计算最大面积
result = maxArea(height)
# 输出最大面积
print("最大面积是:", result)