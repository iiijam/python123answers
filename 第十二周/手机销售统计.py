setDataOf2018=set() 
setDataOf2019=set() 
with open('sale2018.csv', 'r', encoding='utf-8') as f: 
    for line in f: 
        x=line.split(sep=',')[0] 
        setDataOf2018.add(x) 
with open('sale2019.csv', 'r', encoding='utf-8') as t: 
    for line in t: 
        x=line.split(sep=',')[0] 
        setDataOf2019.add(x) 
num = int(input()) 
if num == 1: 
    m=list(setDataOf2018) 
    m.sort() 
    n=list(setDataOf2019) 
    n.sort() 
    print(n) 
    print(m) 
if num == 2: 
    m=list(setDataOf2018&setDataOf2019) 
    m.sort() 
    print(m) 
if num == 3: 
    m=list(setDataOf2018|setDataOf2019) 
    m.sort() 
    print(m) 
if num == 4: 
    m=list(setDataOf2019-setDataOf2018) 
    m.sort() 
    print(m) 
if num == 5: 
    m=list((setDataOf2019-setDataOf2018)|(setDataOf2018-setDataOf2019)) 
    m.sort() 
    print(m)