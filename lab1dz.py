from math import sqrt

a=float(input())
b=float(input())
c=float(input())
D=float(b**2-4*a*c)
if D>=0:
    m=(-b+sqrt(D))/2*a
    n=(-b-sqrt(D))/2*a
    print('Первый корень: ',m, '; Второй корень: ',n)
else:
    print('Дискриминант меньше нуля, корней нет')


