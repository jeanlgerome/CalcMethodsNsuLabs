# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 17:31:36 2019

@author: savin
"""

import numpy
from matplotlib import pylab
from pylab import *
from matplotlib import mlab
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
     
def func(x, y):                                     # функция, которую интегрируем 
    # return math.exp(-x**2)*x -2*x*y;
    a=20;
    return a*math.exp(1-a*x)-a*y;
    #return -a*y;   
def real(x):                                        # решение диф уравнения
   #return math.exp(-x**2)*(x**2)/2;
   a=20;
   return (x*a)*math.exp(1-a*x);
   #return math.exp(-a*x);
def euler(x_j, y_j, h,a):                           #  метод Эйлера, который используем 
                                                    # для повышения точности 
         
         a[1]=y_j+ h *( func(x_j,y_j) + func(x_j+h,y_j+h*func(x_j,y_j) )  )/2;
         a[0]=x_j+h;   
def error(x, y ):                                   # функция вычисл глоб погрешность
    e=0;
    for i in range(0,len(x)):
        if(  math.fabs(real(x[i])-y[i]) > e   ):
            e=math.fabs(real(x[i])-y[i]);
    return e;  
def euler_mod(x0, y0, h, n, x, y):                  # модиф Эйлер вычисл на всех узлах
     y[0]=y0;                                       # не для повыш точности 
     x[0]=x0;
     for i in range(0,n-1):
         y[i+1]=y[i]+ h *( func(x[i],y[i]) + func(x[i]+h,y[i]+h*func(x[i],y[i]) )  )/2;
         x[i+1]=x[i]+h;    
        
        

    

f2 = open("input.txt", 'r')   #         открывем файл на чтение 
a=int(f2.readline()[:2])
b=int(f2.readline()[:2])      #         считываем данные 
y_a=int(f2.readline()[:2])
n=int(f2.readline()[:4])
f2.close()                    #         закрываем

h=(b-a)/n;
n=n+1              
x = [0] * n; 
y  = [0] * n; 
y_m  = [0] * n;               #         создаем массивы 
anew1=[0]*2;  
anew2=[0]*2;
ahh=[0]*2; 
x_j=a; y_j=y_a;               #         задаем начальные условия 
x[0]=a;
y[0]=y_a;  



open("output1.txt", 'w').close()   #      очищаем файл и записываем верх 

with open("output1.txt",'a',encoding = 'utf-8') as f:  
       f.write("{0:<6}   {1:<15}       {2:<15}    {3:<15}   {4:<15}   {5:<15}   {6:<11}  ".format("j", "x", "y", "y_increase", "exact", "error", "error_incr")+'\n'*2) 

euler_mod(a,y_a,h,n,x,y_m);      #       модиф эйлер без повыш точности 

for j in range(0,n-1):           #       модиф эйлер с повыш точности 
   euler(x_j, y_j, h,  anew1); 
   euler(x_j, y_j, h/2,  ahh);     
   euler(ahh[0], ahh[1], h/2, anew2); 
   # повышение точности 
   anew1[1]=anew2[1]+ ( anew2[1]-anew1[1])/3;   
    
   x_j=anew1[0];
   y_j=anew1[1];
   x[j+1]=x_j;
   y[j+1]=y_j;
   
 
for j in range(0, n):    
    with open("output1.txt",'a',encoding = 'utf-8') as f:  #  записываем данные 
        f.write("{0:<6}   {1:<15}       {2:<15}    {3:<15}   {4:<15}   {5:<15}   {6:<11}  ".format(j, toFixed(x[j],10), toFixed(y_m[j],10),  toFixed(y[j],10),  toFixed(real(x[j]),10),  toFixed(math.fabs(y_m[j]-real(x[j])),10),  toFixed(math.fabs(y[j]-real(x[j])),10))  +'\n') 
with open("output1.txt",'a',encoding = 'utf-8') as f:
    f.write("\n\nGlobal error of m_Euler = {0:<6}  \n\nGlobal error of increased m_Euler = {1:<15} \n\nK = {2:<6}".format(error(x,y_m),error(x,y),error(x,y_m)/error(x,y)))
    
     
f.close()


graph(y,h);                     # график 

