'''
某城市出租车计费标准如下：
（1）起步里程为3公里(含3公里)，起步费13元；
（2）载客里程3~15公里范围的，除起步费外，超过3公里的部分按基本单价2.3元/公里计算；
（3）载客里程超过15公里的，15公里内的按照（2）计算，超过15公里的基本单价加收50%的费用；
（4）时速低于12公里/小时的慢速行驶时间计入等待时间，每等待1分钟加收1元；
请输入乘车里程（整数）、等待时间，输出车费。
'''

def Taxi(distance, waitTime):
    if distance <= 3:
        return 13 + waitTime
    elif distance <= 15:
        return 13 + (distance - 3) * 2.3 + waitTime
    else:
        return 13 + (15 - 3) * 2.3 + (distance - 15) * 2.3 * 1.5 + waitTime

distance, waitTime = input().split(',')
distance = int(distance)
waitTime = int(waitTime)
print(int(Taxi(distance, waitTime)))
