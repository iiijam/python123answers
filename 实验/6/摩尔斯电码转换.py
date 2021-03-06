'''
编写程序，把输入的英文句子转换成摩尔斯电码并输出电码字符串。
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.", "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
本题只需要对英文字母（不区分大小写）进行编码转换，其他字符原样输出。
'''

if __name__ == '__main__':
    inputString = input()
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.", "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    outputString = ''
    for i in inputString:
        if i.isupper():
            outputString += morse_code[ord(i) - ord('A')]
        elif i.islower():
            outputString += morse_code[ord(i) - ord('a')]
        else:
            outputString += i
    print(outputString)