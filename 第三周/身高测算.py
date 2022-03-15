#身高测算
'''测算身高，单位为厘米，公式参考下列：
男性身高=(父亲身高+母亲身高)×1.08÷2
女性身高=(父亲身高×0.923+母亲身高)÷2
性别输入"男"或“女”，本题保证所有测试输入身高数据为整型，输出结果取整。
如果性别输入不符合要求，则输出“无对应公式”'''

class Solution:
    def __init__(self,fatherHeight:str,motherHeight:str,sex:str):

        self.fatherHeight = fatherHeight
        self.motherHeight = motherHeight
        self.sex = sex

    def solver(self) -> None:
        if self.sex == "男":
            h = (self.fatherHeight + self.motherHeight) * 1.08 / 2
            print(int(h))
        elif self.sex == "女":
            h = (self.fatherHeight * 0.923 + self.motherHeight) / 2
            print(int(h))
        else:
            print('无对应公式')

Solution(eval(input()),eval(input()),str(input())).solver()
