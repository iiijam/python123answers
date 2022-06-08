import string

def caesar_cipher(text):
    """接收一个字符串为参数，采用字母表和数字中后面第3个字符代替当前字符的方法
    对字符串中的字母和数字进行替换，实现加密效果，返回值为加密的字符串。
    例如：2019 abc 替换为5342 def """
    result = ''
    for i in text:
        if i.isalpha():
            if i.isupper():
                result += chr(ord('A') + (ord(i) - ord('A') + 3) % 26)
            else:
                result += chr(ord('a') + (ord(i) - ord('a') + 3) % 26)
        elif i.isdigit():
            result += chr(ord('0') + (ord(i) - ord('0') + 3) % 10)
        else:
            result += i
    return result

if __name__ == '__main__':
    plaintext = input()
    print(caesar_cipher(plaintext))