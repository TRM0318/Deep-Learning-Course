print("求一元二次方程ax²+bx+c=0（a≠0）解，请依次输入对应a,b,c的值")
a = input("输入a的值：")
b = input("输入b的值：")
c = input("输入c的值：")
a = float(a)
b = float(b)
c = float(c)
Delta = b * b - 4 * a * c
if Delta < 0:
    print("该一元二次方程无实根！")
elif Delta == 0:
    print("该一元二次方程有一个实根！")
    x = (-b) / (2 * a)
    print("该方程的解是：", x)
elif Delta > 0:
    print("该一元二次方程有两个实根！")
    Delta_sqrt = Delta ** 0.5
    x1 = (-b + Delta_sqrt) / (2 * a)
    x2 = (-b - Delta_sqrt) / (2 * a)
    print("该方程的解是：", x1, x2)

