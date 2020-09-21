# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:23:44 2019

@author: savin
"""

from matplotlib import pylab
from pylab import math
import matplotlib.pyplot as plt
def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
def graph( ynew, h):                               # функция графика         
    # Интервал изменения переменной по оси X
    xmin = a
    xmax = b
    dx = 0.01 # Шаг между точками
    # список координат по оиси X на отрезке [-xmin; xmax]
    xlist = pylab.frange (xmin, xmax, h)
    xlist2 = pylab.frange (xmin, xmax, dx)
    # значение функции в заданных точках
    ylist = ynew               # построенная
    ylist2 = [real(x) for x in xlist2]             # реальная
    # рисуем графики
    pylab.plot (xlist, ylist)
    pylab.plot (xlist2, ylist2)
    plt.grid(True)
    pylab.show() #  Покажем  график
    
def set_m_d(u0,u1,m,a,h,d,x):
    for i in range (1,N-1):
        m[i][i-1]=1/h**2
        m[i][i+0]=-2/h**2-g(a+h*i)
        m[i][i+1]=1/h**2
        d[i]=z(a+h*(i))
        x[i]=a+h*i
    m[0][0]=1
    m[N-1][N-1]=1
    d[0]=u0
    d[N-1]=u1
    x[0]=a
    x[N-1]=b
def set_m_d_1(u0,u1,m,a,h,d):
     for i in range (1,N-1):
         m[i][i-1]= 1/h**2  -  g(a+h*(i-1))/12 
         m[i][i+0]= ( -2/h**2  +  g(a+h*i)/6  -  g(a+h*i))
         m[i][i+1]=  ( 1/h**2  -  g(a+h*(i+1))/12)
         d[i]=( z(a+h*(i+1))  +10*z(a+h*(i)) +z (a+h*(i-1))   )/12
         
     m[0][0]=1
     m[N-1][N-1]=1
     d[0]=u0
     d[N-1]=u1
     

    
    
def progonka(m, d):
    x = [0] * len(m[1])  # create massives
    a = [0] * len(m[1])
    b = [0] * len(m[1])
    y = [0] * len(m[1])

    y[0] = m[0][0]  # n=0
    a[0] = m[0][1] / y[0] * -1
    b[0] = d[0] / y[0]

    for i in range(0, (len(m[1]) - 1)):  # algo
        y[i] = m[i][i] + a[i - 1] * m[i][i - 1]
        a[i] = m[i][i + 1] / y[i] * -1
        b[i] = (d[i] - m[i][i - 1] * b[i - 1]) / y[i]
    i = len(m[1]) - 1
    y[i] = m[i][i] + a[i - 1] * m[i][i - 1]
    b[i] = (d[i] - m[i][i - 1] * b[i - 1]) / y[i]

    x[len(m[1]) - 1] = b[len(m[1]) - 1]  # обратный ход

    while i != -1:
        i = i - 1
        x[i] = x[i + 1] * a[i] + b[i]

    return x
def error(x, y ):                                   # функция вычисл глоб погрешность
    e=0;
    for i in range(0,len(x)):
        if(  math.fabs(real(x[i])-y[i]) > e   ):
            e=math.fabs(real(x[i])-y[i]);
    return e; 
def real(x):
    return (1-x)*math.exp(-x*x)
    
def g(x):
    return 1+x*x;
def z(x):
    return (-3*x*x*x+3*x*x+7*x-3)*math.exp(-x*x)
f2 = open("input.txt", 'r')   #         открывем файл на чтение 
a=int(f2.readline()[:2])
b=int(f2.readline()[:2])      #         считываем данные 
y0=int(f2.readline()[:2])
y1=int(f2.readline()[:2])
N=int(f2.readline()[:4])
f2.close()                    #         закрываем
h=(b-a)/N
N=N+1
d=[0]*(N)
x=[0]*(N)
m = [[0] * (N  ) for i in range(N )]

open("output1.txt", 'w').close()   #      очищаем файл и записываем верх 

with open("output1.txt",'a',encoding = 'utf-8') as f:  
       f.write("{0:<6}   {1:<15}       {2:<15}    {3:<15}   {4:<15}   {5:<15}   {6:<11}  ".format("j", "x", "y", "y_increase", "exact", "error", "error_incr")+'\n'*2) 

set_m_d_1(y0,y1,m,a,h,d)
y_1=progonka(m, d)
m = [[0] * (N  ) for i in range(N )]
set_m_d(y0,y1,m,a,h,d,x)
y=progonka(m, d)


for j in range(0, N):    
    with open("output1.txt",'a',encoding = 'utf-8') as f:  #  записываем данные 
        f.write("{0:<6}   {1:<15}       {2:<15}    {3:<15}   {4:<15}   {5:<15}   {6:<11}  ".format(j, toFixed(x[j],10), toFixed(y[j],10),  toFixed(y_1[j],10),  toFixed(real(x[j]),10),  toFixed(math.fabs(y[j]-real(x[j])),10),  toFixed(math.fabs(y_1[j]-real(x[j])),10))  +'\n') 
with open("output1.txt",'a',encoding = 'utf-8') as f:
    f.write("\n\nGlobal error of m_Euler = {0:<6}  \n\nGlobal error of increased m_Euler = {1:<15} \n\nK = {2:<6}".format(error(x,y),error(x,y_1),error(x,y)/error(x,y_1)))
    
     
f.close()
graph(y_1,h);