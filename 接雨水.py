# 定义 trap 函数用于计算能接住的雨水量
def trap(height):
    # 初始化左右指针、前缀最大高度、后缀最大高度和最终结果
    left, right = 0, len(height) - 1
    premax, sufmax, ans = 0, 0, 0
    # 当左指针小于右指针时进行循环
    while left < right:
        # 更新前缀最大高度
        premax = max(height[left], premax)
        # 更新后缀最大高度
        sufmax = max(height[right], sufmax)
        if premax < sufmax:
            # 如果前缀最大高度小于后缀最大高度
            # 则当前位置能接住的雨水量为前缀最大高度减去当前位置的高度
            ans += premax - height[left]
            # 左指针右移
            left += 1
        else:
            # 如果前缀最大高度大于等于后缀最大高度
            # 则当前位置能接住的雨水量为后缀最大高度减去当前位置的高度
            ans += sufmax - height[right]
            # 右指针左移
            right -= 1
    return ans

# 从用户输入获取高度列表，输入的高度值用逗号分隔
input_str = input()
input_str = input_str.strip('[]')
# 将输入的字符串按逗号分割并转换为整数列表
height = [int(x) for x in input_str.split(',')]
# 调用 trap 函数计算能接住的雨水量
result = trap(height)
# 输出能接住的雨水量
print("能接住的雨水量是:", result)