def getOver80Data(filename):
    over80ls = []
    with open(filename, "r") as fp:
        s = fp.readline()
        s = fp.readline()
        while s:
            l = s.strip().split(",")
            if eval(l[-1]) >= 0.8:
                over80ls.append(l)
            s = fp.readline()
    return over80ls


def getOver90orBelow70(filename):
    over90ls = []
    below70ls = []
    with open(filename, "r") as fp:
        s = fp.readline()
        s = fp.readline()
        while s:
            l = s.strip().split(",")
            if eval(l[-1]) >= 0.9:
                over90ls.append(l)
            if eval(l[-1]) <= 0.7:
                below70ls.append(l)
            s = fp.readline()
    return over90ls, below70ls


n = input()
if n == '1':
    ls = getOver80Data("admit2.csv")
    count = 0  # 用于记录排名大于4的个数
    for row in ls:
        if eval(row[1]) >= 4:
            count += 1
    print(f"Top University in >=80%:{(count/len(ls)*100):.2f}%")
elif n == 'Research':
    ls1, ls2 = getOver90orBelow70("admit2.csv")
    # print(ls1)
    count1 = len([i for i in ls1 if i[-4] == '1'])  # 大于90%，且有研究经历的个数
    count2 = len([i for i in ls2 if i[-4] == '1'])  # 小于70%，且有研究经历的个数
    print(f"Reseach in >=90%:{(count1/len(ls1)*100):.2f}%")
    print(f"Reseach in <=70%:{(count2/len(ls2)*100):.2f}%")
elif n == '2':
    ls = getOver80Data("admit2.csv")
    l = []  # 保存所有TOEFL分数
    for i in ls:
        l.append(float(i[3]))
    print(f"TOEFL Average Score:{sum(l)/len(l):.2f}")
    print(f"TOEFL Max Score:{max(l):.2f}")
    print(f"TOEFL Min Score:{min(l):.2f}")
elif n == '3':
    over80ls = getOver80Data("admit2.csv")
    ls = []  # 保存所有绩点分数
    for i in over80ls:
        ls.append(float(i[-5]))
    print(f"CGPA Average Score:{(sum(ls)/len(ls)):.3f}")
    print(f"CGPA Max Score:{max(ls):.3f}")
    print(f"CGPA Min Score:{min(ls):.3f}")
else:
    print("ERROR")
