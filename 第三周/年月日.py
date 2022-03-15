#输入年/月/日（用斜杠分隔），输出该日期是这一年的第几天（题目保证年、月、日都是合法输入）？
#输入:2018/2/1
#输出:2018年2月1日是2018年第32天

class Solution:
    def __init__(self,string: str) -> None:
        self.str = string

    def formation(self) -> None:

        a,b,c=self.str.split('/')

        a = int(a)
        b = int(b)
        c = int(c)


        ls=[31,28,31,30,31,30,31,31,30,31,30,31]

        d=0

        for i in range(1,b):

            d=int(ls[i-1]+d)

        if b>2:

            if a%4==0 and a%100!=0 or a%400==0 :

                print(str(a)+'年'+str(b)+'月'+str(c)+'日是'+str(a)+'年第'+str(c+d+1)+'天')

            else:

                print(str(a)+'年'+str(b)+'月'+str(c)+'日是'+str(a)+'年第'+str(c+d)+'天')
        else:

            print(str(a)+'年'+str(b)+'月'+str(c)+'日是'+str(a)+'年第'+str(c+d)+'天')




Solution(str(input())).formation()



