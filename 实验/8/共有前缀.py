'''在一行中输入以空格间隔的若干以字母数字字符组成的字符串（字符串之间不包含其他字符）
定义一个函数，找出这些字符串的最长的共有前缀并输出
如果不存在共有前缀，输出‘NOT FOUND’'''

def f(strs:list) -> str:
    if not strs:
        return "NOT FOUND"
    
    length, count = len(strs[0]), len(strs)
    for i in range(length): # 共有前缀的长度
        char = strs[0][i] # 共有前缀的字符
        for j in range(1, count): # 纵向扫描
            if i == len(strs[j]) or strs[j][i] != char: # 如果不存在共有前缀，输出‘NOT FOUND’
                return strs[0][:i] if i else "NOT FOUND" # 返回
    
    return strs[0]



strs = list(input().split())
print(f(strs))