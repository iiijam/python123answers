#现有方程：0 = x^5-15x^4+85x^3-225x^2+274x-121, 已知f(x)在[1.5,2.4]区间单调下降，且在该区间f(x)==0有且只有一个根，用二分法求解该根。

def main():
    limitZero = 10 ** -(int(input()))
    startPoint = 1.5
    endPoint = 2.4
    while True:
        midPoint = (startPoint + endPoint) / 2
        functionValue = midPoint ** 5 - 15 * (midPoint ** 4) + 85 * (midPoint ** 3) - 225 * (midPoint ** 2) + 274 * midPoint - 121
        if abs(functionValue) < limitZero:
            print('%.6f' % midPoint)
            break
        else:
            if functionValue > 0:
                startPoint = midPoint
            else:
                endPoint = midPoint
    
main()