# 1 统计文件中出现的葡萄酒生产国家，输出不重复的国家名列表，按字母
#   表升序排序， 若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素
# 2 计算每个国家的葡萄酒的平均得分，返回值为国家名和得分的列表
# 3 计算每个国家的葡萄酒的平均得分，返回值为国家名和得分的列表，按评分由高到低降序排列
# 4 评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出
# 5 价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出
# 6 统计各个评分的葡萄酒数量是多少？输出包含评分和数量的列表
# 7 输出拥有葡萄酒数量最多的评分和数量
# 8 输出拥有葡萄酒数量最多的评分的葡萄酒的平均价格

import pandas as pd
import math

# 定义符号常量，用于索引，使之具有清晰的语义
NUMBER = 0
COUNTRY = 1
DESCRIPTION = 2
POINTS = 3
PRICE = 4
PROVINCE = 5


def csv_to_ls(file):
    """接收文件名为参数，用pandas读取数据为dataframe格式，
    再将其数据部分(values)用tolist()方法转为二维列表，
    返回这个二维列表。
    @参数 file：文件名，字符串类型
    """
    wine_list = pd.read_csv(file).values.tolist()
    # print(wine_list)
    return wine_list


def country_ls(wine_list):
    """接收列表格式的葡萄酒数据为参数，略过标题行，返回不重复的国家名列表，按字母表升序排序，
    若国家名数据缺失，略过该条数据，返回值中不包含空字符串元素。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    country_ls = set()
    for wine in wine_list[1:]:
        if wine[COUNTRY] != "":
            country_ls.add(wine[COUNTRY])
    country_ls = list(country_ls)  
    country_ls.sort()
    return country_ls


def avg_point(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    avg_point_ls = []
    for country_name in country:
        country_point = 0
        country_num = 0
        for wine in wine_list:
            if country_name == wine[COUNTRY]:
                country_point += float(wine[POINTS])
                country_num += 1
        avg_point_ls.append([country_name, round((country_point / country_num),2)])
    return avg_point_ls


def avg_point_sort(wine_list, country):
    """接收列表格式的葡萄酒数据和国家名列表为参数，计算每个国家的葡萄酒的平均得分，
    返回值为国家名和得分的列表，按评分由高到低降序排列。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 country：国家名，列表类型
    """
    avg_point_sort_ls = []
    for country_name in country:
        country_point = 0
        country_num = 0
        for wine in wine_list:
            if country_name == wine[COUNTRY]:
                country_point += float(wine[POINTS])
                country_num += 1
        avg_point_sort_ls.append([country_name, round((country_point / country_num),2)])
    avg_point_sort_ls.sort(key=lambda x: x[1], reverse=True)
    return avg_point_sort_ls



def top_10_point(wine_list):
    """接收列表格式的葡萄酒数据参数，返回评分最高的十款葡萄酒的编号、出产国、评分和价格，按评
    分降序输出。
    需要注意的是评分可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    top_10_point_ls = []
    for wine in wine_list:
        if math.isnan(float(wine[POINTS])) == False:
            top_10_point_ls.append([wine[NUMBER], wine[COUNTRY], wine[POINTS], wine[PRICE]])
    top_10_point_ls.sort(key=lambda x: x[2], reverse=True)
    return top_10_point_ls[:10]


def top_20_price(wine_list):
    """接收列表格式的葡萄酒数据参数，返回价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价
    格降序输出。
    @参数 wine_list：葡萄酒数据，列表类型
    需要注意的是价格可能有缺失值，此时该数据为nan
    if math.isnan(x) == False可用于判定x的值是不是nan
    nan的数据类型是float,不可以直接用字符串判定方法。
    """
    top_20_price_ls = []
    for wine in wine_list:
        if math.isnan(float(wine[PRICE])) == False:
            top_20_price_ls.append([wine[NUMBER], wine[COUNTRY], wine[POINTS], wine[PRICE]])
    top_20_price_ls.sort(key=lambda x: x[3], reverse=True)
    return top_20_price_ls[:20]


def amount_of_point(wine_list):
    """接收列表格式的葡萄酒数据参数，统计每个评分的葡萄酒数量，忽略没有评分的数据。
    返回二维列表，按评分升序排序。
    例如[...[84, 645], [85, 959],...]表示得分为84的葡萄酒645种，得分85的葡萄酒有959种。
    @参数 wine_list：葡萄酒数据，列表类型
    """
    pointsList = []
    answer = []
    for points in wine_list:
        if math.isnan(points[3]) == False:
            pointsList.append(points[3])
    pointsSingleList = list(set(pointsList))
    for point in pointsSingleList:
        num = pointsList.count(point)
        temp = [point, num]
        answer.append(temp)
    return answer


def most_of_point(amount_of_points):
    """接收每个评分的葡萄酒数量的列表为参数，返回获得该分数数量最多的评分和数量的列表。
    @参数 amount_of_points：每个评分的葡萄酒数量，列表类型
    """
    temp = amount_of_points[::]
    temp.sort(key=lambda x: x[1])
    return temp[-1]


def avg_price_of_most_point(wine_list, most_of_points):
    """接收列表格式的葡萄酒数据和获得最多的评分及数量的列表为参数
    忽略缺失价格的数据，返回这个分数的葡萄酒的平均价格，保留2位小数。
    @参数 wine_list：葡萄酒数据，列表类型
    @参数 most_of_points：获得最多的评分及数量，列表类型
    """
    ls = []
    for i in wine_list:
        if math.isnan(i[4]) == False and i[3] == most_of_points[0]:
            ls.append(i[4])
    return round(sum(ls) / len(ls), 2)


def judge(txt):
    """接收一个字符串为参数，根据参数值调用不同函数完成任务"""
    filename = './winemag-data.csv'
    wine = csv_to_ls(filename)
    country = country_ls(wine)
    if txt == '国家名列表':
        print(country)
    elif txt == '平均分':
        print(avg_point(wine, country))  # 每个国家的葡萄酒的平均得分
    elif txt == '平均分排序':
        print(avg_point_sort(wine, country))  # 每个国家的葡萄酒的平均得分降序输出
    elif txt == '评分最高':
        print(top_10_point(wine))  # 评分最高的十款葡萄酒的编号、出产国、评分和价格，按评分降序输出
    elif txt == '价格最高':
        print(top_20_price(wine))  # 价格最高的二十款葡萄酒的编号、出产国、评分和价格，按价格降序输出
    elif txt == '葡萄酒评分':
        amount_point = amount_of_point(wine)
        most_point = most_of_point(amount_point)
        print(amount_point)  # 各个评分的葡萄酒数量
        print(most_point)  # 拥有葡萄酒数量最多的评分和数量
        print(avg_price_of_most_point(wine, most_point))  # 拥有葡萄酒数量最多的评分的葡萄酒的平均价格
    else:
        print('输入错误')


if __name__ == '__main__':
    text = input()
    judge(text)
