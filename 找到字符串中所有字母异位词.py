from collections import Counter

def findAnagrams( s , p ) :
    ans = []
    cnt_p = Counter(p)  # 统计 p 的每种字母的出现次数
    cnt_s = Counter()  # 统计 s 的长为 len(p) 的子串 s' 的每种字母的出现次数
    for right, c in enumerate(s):
        cnt_s[c] += 1  # 右端点字母进入窗口 
        left = right - len(p) + 1
        if left < 0:  # 窗口长度不足 len(p)
            continue
        if cnt_s == cnt_p:  # s' 和 p 的每种字母的出现次数都相同    
            ans.append(left)  # s' 左端点下标加入答案
        cnt_s[s[left]] -= 1  # 左端点字母离开窗口
    return ans

nums_str1 = input()
nums_str2 = input()
result = findAnagrams(nums_str1,nums_str2)
print(result)
