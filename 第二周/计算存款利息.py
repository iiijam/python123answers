'''在三行中依次输入初始存款金额，存款年限，年利率，每年末计一次利息并转为本金，计算并输出存款到期时的利息（不含本金，税前），结果保留2位小数。

复利法,每年末计算利息并自动转存：
F=P×(1+i)^N
F：复利终值
P：本金
i：利率
N：利率获取时间的整数倍(年限)'''

class Soultion:
    def calc(self, money, years, apr) -> float:
        return format(money * (1 + apr) ** years - money, '.2f')

a = eval(input())
b = eval(input())
c = eval(input())
print('利息=' + Soultion().calc(a, b, c))
