class Solution:
    def __init__(self, n: int):
        self.n = n

    def solver(self) -> None:
    

        m = self.n-5000

        if -5000 <= m <= 0:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' % (0), '%.2f' % (self.n)))

        elif 0 < m <= 3000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.03), '%.2f' % (self.n-m*0.03)))

        elif 3000 < m <= 12000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.1-210), '%.2f' % (self.n-m*0.1+210)))

        elif 12000 < m <= 25000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.2-1410), '%.2f' % (self.n-m*0.2+1410)))

        elif 25000 < m <= 35000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.25-2660), '%.2f' % (self.n-m*0.25+2660)))

        elif 35000 < m <= 55000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.3-4410), '%.2f' % (self.n-m*0.3+4410)))

        elif 55000 < m <= 80000:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.35-7160), '%.2f' % (self.n-m*0.35+7160)))

        elif 80000 < m:

            print('应缴税款{}元，实发工资{}元。'.format('%.2f' %
                  (m*0.45-15160), '%.2f' % (self.n-m*0.45+15160)))

        else:

            print('error')


Solution(eval(input())).solver()
