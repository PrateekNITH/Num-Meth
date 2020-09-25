import math

print("Input F(X) : ")
fxo = input()


def bisection(fxo):
    print(" Enter a and b : ")
    a = float(input())
    b = float(input())
    print(" Enter number of iterations : ")
    n = int(input())
    fa = fxn(fxo, a)
    fb = fxn(fxo, b)

    for i in range(1, n+1, 1):
        print("\nITERATION - ", i)
        xm = (a+b)/2
        print("\nXm = ", xm)
        fxm = fxn(fxo, xm)
        print("\n F(Xm) = ", fxm)
        if fxm*fa <= 0:
            b = xm
        else:
            a = xm


def regula(fxo):
    print(" Enter a and b : ")
    a = float(input())
    b = float(input())
    print(" Enter number of iterations : ")
    n = int(input())


    for i in range(1, n+1, 1):
        fa = fxn(fxo, a)
        fb = fxn(fxo, b)
        print("\nITERATION - ", i)
        xm = (a*fb-b*fa)/(fb-fa)
        print("\nXm = ", xm)
        fxm = fxn(fxo, xm)
        print("\n F(Xm) = ", fxm)
        if fxm * fa <= 0:
            b = xm
        else:
            a = xm


def fxn(fxo, x):
    x = str(x)
    fx = fxo.replace("x", x)
    code = compile(fx, "<string>", "eval")
    a = eval(code)
    return a


print("METHOD No. : ")
mn = input()
if mn == 1:
    bisection(fxo)
else:
    regula(fxo)


