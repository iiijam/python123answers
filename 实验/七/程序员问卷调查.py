
#不允许修改。fopen函数打开文件，并返回包含文件数据一个列表ls，
def fopen(name):
    ls=[]
    with open(name,'r',encoding = 'UTF-8') as f:
       for i in f.readlines()[1:]:
           ls.append(i.strip().split(','))
    return ls





lt = fopen('survey.csv')   #不允许修改，打开题目文件，并将返回的数据列表赋值给lt
memo = {
    '程序员': 0,
    '程序爱好者': 0,
    '程序初学者': 0,
    '编程相关者': 0,
    '非程序员': 0,
    '空白': 0,
}
for i in range(len(lt)):
    if lt[i][1] == 'I am a developer by profession':
        memo['程序员'] += 1
    elif lt[i][1] == 'I code primarily as a hobby':
        memo['程序爱好者'] += 1
    elif lt[i][1] == 'I am a student who is learning to code':
        memo['程序初学者'] += 1
    elif lt[i][1] == '"I am not primarily a developer':
        #注意数据中有"
        memo['编程相关者'] += 1
    elif lt[i][1] == '"I used to be a developer by profession':
        memo['非程序员'] += 1
    elif lt[i][1] == 'NA':
        memo['空白'] += 1

command = input()
if command == '记录':
    print('总计:{}条'.format(len(lt))) # 64461
elif command in memo:
    print('{}:{}条'.format(command, memo[command]))
else:
    print('错误输入')
