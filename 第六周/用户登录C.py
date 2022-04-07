'''
实现用户输入用户名和密码，当用户名为admin或administrator且密码为123456时，显示“登录成功”，否则显示“登录失败”，登录失败时允许重复输入三次。
'''

class Login:
    def __init__(self):
        self.user = 'admin'
        self.altUser = 'administrator'
        self.pwd = '123456'
        self.count = 0

    def login(self):
        while self.count < 3:
            name = input()
            pwd = input()
            if (name == self.user or name ==self.altUser) and pwd == self.pwd:
                print('登录成功')
                break
            else:
                print('登录失败')
                self.count += 1
        else:
            print('输入错误次数过多，程序退出')


if __name__ == '__main__':
    login = Login()
    login.login()
