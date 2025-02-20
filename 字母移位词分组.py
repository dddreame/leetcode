def groupAnagrams(strs):
    # 初始化一个字典用于存储分组结果
    mp = {}
    for str in strs:
        # 对字符串进行排序
        sorted_str = ''.join(sorted(str))
        if sorted_str not in mp:
            mp[sorted_str] = []
        mp[sorted_str].append(str)
    # 将字典中的值转换为二维列表
    ans = list(mp.values())
    return ans

if __name__ == "__main__":
    # 输入字符串列表
    input_str = input()
    input_str = input_str.strip('[]')
    # 将输入的字符串转换为列表
    strs = input_str.split(',')
    # 调用 groupAnagrams 函数进行分组
    result = groupAnagrams(strs)
    # 输出分组结果
    print(result)
