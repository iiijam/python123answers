fileName = input()

with open(fileName, 'r', encoding='utf-8') as f:
    text = f.read()
    list_of_deldete = list('!"#$%&()*+,./:;<=>?@[\]^_‘{|}~\n')
    for i in list_of_deldete:
        text = text.replace(i, ' ')

    ls = text.split()
    print(len(ls))