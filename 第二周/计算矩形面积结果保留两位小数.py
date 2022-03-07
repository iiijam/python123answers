class Soultion:
    def calc(self, length, width) -> float:
        return format(length * width,  '.2f')

a = eval(input())
b = eval(input())
print(Soultion().calc(a, b))
