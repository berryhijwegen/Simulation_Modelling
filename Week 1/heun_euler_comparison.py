import math
import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    return y

def heun(x0,y0,n,end):
    def asol(x):
        return math.exp(x)

    yasol = np.vectorize(asol)

    h = end / n
    x = np.arange(0.0, end+h, h)
    y = np.zeros(x.size)
    y[0] = y0

    for i in range(1, x.size):
        y_intermediate = y[i-1] + h*func(x[i-1],y[i-1])

        y[i] = y[i-1] + (h/2.0)*(func(x[i-1],y[i-1]) + func(x[i],y_intermediate))
    plt.plot(x,y,'r-', label='Heun')
    plt.plot(x,yasol(x),'b-', label='Actual')
    
    print("Actual solution at x = ", x[-1], " is ", "%.6f"% yasol(x)[-1])  
    print("Heun's Method solution at x = ", x[-1], " is ", "%.6f"% y[-1])  

# Function for euler formula 
def euler(x0,y,n,end):   
    h = end / n
    all_x = [x0]
    all_y = [y]
    while x0 < end: 
        y = y + h * func(x0, y) 
        x0 = x0 + h 
        
        all_x.append(x0)
        all_y.append(y)
    plt.plot(all_x,all_y,'y-', label='Euler')
    print("Euler's Method solution at x = ", end, " is ", "%.6f"% y) 
      
x0 = 0
y0 = 1

list_n = [5,10,20,100] 
end = 1.0

comparison_functions = [heun, euler]
for n in list_n: 
    print(f"n = {n}")
    [function(x0,y0,n,end) for function in comparison_functions]
    plt.legend()
    plt.savefig(f'plot_heun_vs_euler_steps-{n}.png')
    plt.show()
    input(f"Press enter to continue.\n------\n")