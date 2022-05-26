'''
设计程序，接收用户输入的省、直辖市、自治区和特别行政区名称，输出对应的省会名称，当输入错误时输出“输入错误”。程序可以重复接收用户输入，直接输入回车时退出程序。
'''

capitals = {'湖南': '长沙', '湖北': '武汉', '广东': '广州', '广西': '南宁', '河北': '石家庄', '河南': '郑州', '山东': '济南', '山西': '太原', '江苏': '南京', '浙江': '杭州', '江西': '南昌', '黑龙江': '哈尔滨', '新疆': '乌鲁木齐', '云南': '昆明', '贵州': '贵阳', '福建': '福州',
            '吉林': '长春', '安徽': '合肥', '四川': '成都', '西藏': '拉萨', '宁夏': '银川', '辽宁': '沈阳', '青海': '西宁', '海南': '海口', '甘肃': '兰州', '陕西': '西安', '内蒙古': '呼和浩特', '台湾': '台北', '北京': '北京', '上海': '上海', '天津': '天津', '重庆': '重庆', '香港': '香港', '澳门': '澳门'}

if __name__ == '__main__':
    while True:
        city = input()
        if city == '':
            break
        if city in capitals:
            print(capitals[city])
        else:
            print('输入错误')