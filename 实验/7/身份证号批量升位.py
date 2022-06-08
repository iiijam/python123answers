def upgradeId(id15: str) -> str:
    id18=list(id15)
    if int(id15[6:8])>=5:
        id18.insert(6,"1")
        id18.insert(7,"9")
    else:
        id18.insert(6,"2")
        id18.insert(7,"0")
    wi_ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    id_sum=sum([ int(id18[i])*wi_ls[i] for i in range(17) ])
    dictString="10X98765432"
    id18.append(dictString[id_sum%11])

    id18 = "".join(id18)
    return id18

n = int(input())
with open('id15.txt','r',encoding='utf-8') as file:
    for i in range(n):
        line = file.readline()   # line 的内容是文件中的一行，字符串类型
        # 在这里写你的代码
        id15, name = map(str, line.split())
        id18 = upgradeId(id15)
        # 本题输出时，身份证与姓名数据间的间隔为中文全角空格，可以复制使用以下的sep参数。
        print(id18 + '　'+ name)
        