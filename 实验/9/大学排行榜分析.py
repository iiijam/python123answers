def read_file(file,m):
    """读文件中的学校名到列表中，返回前m个记录的学校集合"""
    with open(file,'r',encoding='utf-8') as f:
        info_list = []
        for line in f:
            line = line.split()
            info_list.append(line[1])
        return info_list[:m]


def either_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在这两个排行榜中均在前m个记录的学校名，按照学校名称排序，
    返回排序后的列表
    """
    both_rank = []
    for i in alumni:
        if i in soft:
            both_rank.append(i)
    return sorted(both_rank)


def all_in_top(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在两个榜单中名列前m的所有学校名，按照学校名称排序，
    返回排序后的列表
    """
    alumni_set = set(alumni)
    soft_set = set(soft)
    both_rank = alumni_set | soft_set
    return sorted(list(both_rank))


def only_alumni(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni榜单中名列前m但soft榜单中未进前m的学校名，
    按照学校名称排序，返回排序后的列表
    """
    only_alumni_rank = []
    for i in alumni:
        if i not in soft:
            only_alumni_rank.append(i)
    return sorted(only_alumni_rank)


def only_once(alumni, soft):
    """接收两个排行榜前m高校名字集合，
    获得在alumni和soft榜单中名列前m，但不同时出现在两个榜单的学校名，
    按照学校名称排序，返回排序后的列表
    """
    alumni_set = set(alumni)
    soft_set = set(soft)
    only_once_rank = alumni_set ^ soft_set
    return sorted(only_once_rank)



def judge(n):
    if n in '1234':
        m=int(input())
        alumni_set = read_file('./alumni.txt',m)
        soft_set = read_file('./soft.txt',m)
        if n=='1':
            either_rank = either_in_top(alumni_set, soft_set)
            print(f'两榜单中均名列前{m}的学校：')
            print(either_rank)
        elif n=='2':
            all_rank = all_in_top(alumni_set, soft_set)
            print(f'两榜单名列前{m}的所有学校：')
            print(all_rank)
        elif n=='3':
            only_in_alumni_rank = only_alumni(alumni_set, soft_set)
            print(f'alumni中名列前{m}，soft中未进前{m}的学校：')
            print(only_in_alumni_rank)
        elif n=='4':
            alumni_soft_rank = only_once(alumni_set, soft_set)
            print(f'不同时出现在两个榜单前{m}的学校：')
            print(alumni_soft_rank)
    else:
        print('Wrong Option')
        

if __name__ == '__main__':
    num = input()
    judge(num)