'''
一个不含0的数，如果它能被它的每一位除尽，则它是一个自除数。
例如128是一个自除数，因为128能被1、2、8整除。
编写函数selfDivisor(num)判断num是否为自除数，使用该函数输出不大于N的所有自除数。
输出为一行，是不大于N的所有自除数，每个数后面有一个空格。
22
1 2 3 4 5 6 7 8 9 11 12 15 22
'''
class Solution:
    def selfDivisor(self, num):
        ans = []
        for i in range(1,num+1):
            cur, ok =i, True
            while cur and ok:
                ok = not((t := cur % 10) == 0 or i % t != 0)
                cur //= 10
            if ok:
                ans.append(i)
        return ans


if __name__ == '__main__':
    answer = Solution().selfDivisor(eval(input()))
    for ans in answer:
        print(ans, end=' ')