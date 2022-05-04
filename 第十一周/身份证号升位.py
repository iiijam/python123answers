id15=input()

id18=list(id15)
'''
第一步，在原十五位数身份证的第六位数后面插入19 （1905年1月1日以后出生）或20（2000.1.1-2004.12.31出生），这样身份证号码即为十七位数；
'''
if int(id15[6:8])>=5:
    id18.insert(6,"1")
    id18.insert(7,"9")
else:
    id18.insert(6,"2")
    id18.insert(7,"0")

'''
第二步，按照国家规定的统一公式计算出第十八位数，作为校验码放在第二代身份证的尾号。
'''
wi_ls=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
id_sum=sum([ int(id18[i])*wi_ls[i] for i in range(17) ])
dictString="10X98765432"
id18.append(dictString[id_sum%11])

print("".join(id18))