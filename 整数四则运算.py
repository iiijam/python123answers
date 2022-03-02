class intCalc:
    def calculate(a, b):
        print(str(a) + " + " + str(b) + " = " + str(a+b))
        print(str(a) + " - " + str(b) + " = " + str(a-b))
        print(str(a) + " * " + str(b) + " = " + str(a*b))
        print(str(a) + " / " + str(b) + " = " + str(a/b))

varA = eval(input())
varB = eval(input())

intCalc.calculate(varA, varB)
