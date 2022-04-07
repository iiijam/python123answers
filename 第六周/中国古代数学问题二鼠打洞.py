'''
有一堵十尺厚的墙，两只老鼠从两边向中间打洞。大老鼠第一天打一尺，小老鼠也是一尺。
大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。
问它们几天可以相逢，相逢时各打了多少。
输入为1个整数wall，代表墙的厚度，单位为尺。
输出为两行，第一行输出1个整数，表示相遇时所需的天数。
第二行输出2个浮点数，分别为小鼠和大鼠打洞的距离，单位为尺，保留小数点后1位数字。
（提示：rouwalld(f,1)为浮点数f保留一位小数。）'''

'''
输入：10
输出：	
4
1.8 8.2
'''


wall=int(input())
big,small,day,time=1,1,0,1
distance_of_big,distance_of_small=0,0
while wall>0:
	# 单独考虑
    if wall-big-small<0:
        time=wall/(big+small)
    # 剩余洞长
    wall=wall-big-small
    distance_of_small=distance_of_small+small*time
    distance_of_big=distance_of_big+big*time
    big*=2
    small*=0.5
    day=day+1
print(day)
print(round(distance_of_small,1),round(distance_of_big,1))

