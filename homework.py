import numpy as np

#define all the functions i need
def function(x):#sin(x)
    return np.sin(x)
def dfunction(x):#first order derivative of sin(x)
    return np.cos(x)
def d2function(x):#second order derivative of sin(x)
    return -np.sin(x)
def function1(x):#7x+9
    return 7 * x + 9
def dfunction1(x):#first order derivative of 7x+9
    return 7
def d2function1(x):#second order derivative of 7x+9
    return 0
def function2(x):#5x^2+7x+9
    return 5 * x**2 + 7 * x + 9
def dfunction2(x):#first order derivative of 5x^2+7x+9
    return 10 * x + 7
def d2function2(x):#second order derivative of 5x^2+7x+9
    return 10
def function3(x):#3x^3+5x^2+7x+9
    return 3 * x**3 + 5 * x**2 + 7 * x + 9
def dfunction3(x):#first order derivative of 3x^3+5x^2+7x+9
    return 9 * x**2 + 10 * x + 7
def d2function3(x):#second order derivative of 3x^3+5x^2+7x+9
    return 18 * x + 10
def function4(x):#x^4+3x^3+5x^2+7x+9
    return 1 * x**4 + 3 * x**3 + 5 * x**2 + 7 * x + 9
def dfunction4(x):#first order derivative of x^4+3x^3+5x^2+7x+9
    return 4 * x**3 + 9 * x**2 + 10 * x + 7
def d2function4(x):#second order derivative of x^4+3x^3+5x^2+7x+9
    return 12 * x**2 + 18 * x + 10


#question 2 calculate the numerical accuracy of the first and second order derivative
print('question 2')

#grid initialization
grid = np.linspace(0, 10 * np.pi, 5004)
grid_2 = np.linspace(0, 10 * np.pi, 10004)

#values in grid
#calculate the real value of the function, first order derivative and second order derivative
f_values = function(grid)
df_real = dfunction(grid)
d2f_real = d2function(grid)
df_values = np.zeros((len(grid), 2))
d2f_values = np.zeros((len(grid), 2))

#defining the error of the first and second order derivative
df_error = np.zeros(2)
d2f_error = np.zeros(2)

#calculate the numerical value of the first and second order derivative
#calculate the error of the first and second order derivative
for i in range(2, len(grid)-2):
    df_values[i][0] = ((f_values[i-2] / 12) - (2 * f_values[i-1] / 3) + (2 * f_values[i+1] / 3) - (f_values[i+2] / 12))/(grid[i+1] - grid[i])
    df_values[i][1] = ((f_values[i+1] / 2) - (f_values[i-1] / 2))/(grid[i+1] - grid[i])
    d2f_values[i][0] = ((f_values[i-2] / 3) - (f_values[i-1] / 3) - (f_values[i+1] / 3) + (f_values[i+2] / 3))/((grid[i+1] - grid[i])**2)
    d2f_values[i][1] = (f_values[i+1] - (2 * f_values[i]) + f_values[i-1])/((grid[i+1] - grid[i])**2)
    df_error[0] = df_error[0] + (df_values[i][0] - df_real[i])**2
    df_error[1] = df_error[1] + (df_values[i][1] - df_real[i])**2
    d2f_error[0] = d2f_error[0] + (d2f_values[i][0] - d2f_real[i])**2
    d2f_error[1] = d2f_error[1] + (d2f_values[i][1] - d2f_real[i])**2
for i in range (0, 2):
    df_error[i] = np.sqrt(df_error[i])
    d2f_error[i] = np.sqrt(d2f_error[i])

#values in grid_2
#calculate the real value of the function, first order derivative and second order derivative
df_error_2 = np.zeros(2)
d2f_error_2 = np.zeros(2)
f_values_2 = function(grid_2)
df_real_2 = dfunction(grid_2)
d2f_real_2 = d2function(grid_2)
df_values_2 = np.zeros((len(grid_2), 2))
d2f_values_2 = np.zeros((len(grid_2), 2))

#calculate the numerical value of the first and second order derivative
#calculate the error of the first and second order derivative
for i in range(2, len(grid)-2):#same length as grid
    df_values_2[i][0] = ((f_values_2[i-2] / 12) - (2 * f_values_2[i-1] / 3) + (2 * f_values_2[i+1] / 3) - (f_values_2[i+2] / 12))/(grid_2[i+1] - grid_2[i])
    df_values_2[i][1] = ((f_values_2[i+1] / 2) - (f_values_2[i-1] / 2))/(grid_2[i+1] - grid_2[i])
    d2f_values_2[i][0] = ((f_values_2[i-2] / 3) - (f_values_2[i-1] / 3) - (f_values_2[i+1] / 3) + (f_values_2[i+2] / 3))/((grid_2[i+1] - grid_2[i])**2)
    d2f_values_2[i][1] = (f_values_2[i+1] - (2 * f_values_2[i]) + f_values_2[i-1])/((grid_2[i+1] - grid_2[i])**2)
    df_error_2[0] = df_error_2[0] + (df_values_2[i][0] - df_real_2[i])**2
    df_error_2[1] = df_error_2[1] + (df_values_2[i][1] - df_real_2[i])**2
    d2f_error_2[0] = d2f_error_2[0] + (d2f_values_2[i][0] - d2f_real_2[i])**2
    d2f_error_2[1] = d2f_error_2[1] + (d2f_values_2[i][1] - d2f_real_2[i])**2
for i in range (0, 2):
    df_error_2[i] = np.sqrt(df_error_2[i])
    d2f_error_2[i] = np.sqrt(d2f_error_2[i])

#calculate the numerical accuracy of the first and second order derivative
#calculate the p value
df_accuracy = np.zeros(2)
d2f_accuracy = np.zeros(2)
p = (grid[1] - grid[0]) / (grid_2[1] - grid_2[0])
df_accuracy[0] = np.log(df_error[0] / df_error_2[0]) / np.log(p)
df_accuracy[1] = np.log(df_error[1] / df_error_2[1]) / np.log(p)
d2f_accuracy[0] = np.log(d2f_error[0] / d2f_error_2[0]) / np.log(p)
d2f_accuracy[1] = np.log(d2f_error[1] / d2f_error_2[1]) / np.log(p)

#output the result
print('numerical accuracy of the first order derivative:')
print('method 1:',df_accuracy[0])
print('method 2:',df_accuracy[1])
print('numerical accuracy of the second order derivative:')
print('method 3:',d2f_accuracy[0])
print('method 4:',d2f_accuracy[1])

#question 3.1 investigate the properties of the rounding error

print('question 3.1')

#linear function
function1_values = function1(grid)
dfunction1_real = np.zeros(len(grid))
d2function1_real = np.zeros(len(grid))
dfunction1_values = np.zeros((len(grid), 2))
d2function1_values = np.zeros((len(grid), 2))
dfunction1_error = np.zeros(2)
d2function1_error = np.zeros(2)
for i in range(2, len(grid)-2):
    dfunction1_real[i] = dfunction1(grid[i])
    d2function1_real[i] = d2function1(grid[i])
    dfunction1_values[i][0] = ((function1_values[i-2] / 12) - (2 * function1_values[i-1] / 3) + (2 * function1_values[i+1] / 3) - (function1_values[i+2] / 12))/(grid[i+1] - grid[i])
    dfunction1_values[i][1] = ((function1_values[i+1] / 2) - (function1_values[i-1] / 2))/(grid[i+1] - grid[i])
    d2function1_values[i][0] = ((function1_values[i-2] / 3) - (function1_values[i-1] / 3) - (function1_values[i+1] / 3) + (function1_values[i+2] / 3))/((grid[i+1] - grid[i])**2)
    d2function1_values[i][1] = (function1_values[i+1] - (2 * function1_values[i]) + function1_values[i-1])/((grid[i+1] - grid[i])**2)
    dfunction1_error[0] = dfunction1_error[0] + (dfunction1_values[i][0] - dfunction1_real[i])**2
    dfunction1_error[1] = dfunction1_error[1] + (dfunction1_values[i][1] - dfunction1_real[i])**2
    d2function1_error[0] = d2function1_error[0] + (d2function1_values[i][0] - d2function1_real[i])**2
    d2function1_error[1] = d2function1_error[1] + (d2function1_values[i][1] - d2function1_real[i])**2
for i in range (0, 2):
    dfunction1_error[i] = np.sqrt(dfunction1_error[i])
    d2function1_error[i] = np.sqrt(d2function1_error[i])
print('rounding error of the first order derivative: linear function')
print('method 1:',dfunction1_error[0])
print('method 2:',dfunction1_error[1])
print('rounding error of the second order derivative: linear function')
print('method 3:',d2function1_error[0])
print('method 4:',d2function1_error[1])

#quadratic function
function2_values = function2(grid)
dfunction2_real = np.zeros(len(grid))
d2function2_real = np.zeros(len(grid))
dfunction2_values = np.zeros((len(grid), 2))
d2function2_values = np.zeros((len(grid), 2))
dfunction2_error = np.zeros(2)
d2function2_error = np.zeros(2)
for i in range(2, len(grid)-2):
    dfunction2_real[i] = dfunction2(grid[i])
    d2function2_real[i] = d2function2(grid[i])
    dfunction2_values[i][0] = ((function2_values[i-2] / 12) - (2 * function2_values[i-1] / 3) + (2 * function2_values[i+1] / 3) - (function2_values[i+2] / 12))/(grid[i+1] - grid[i])
    dfunction2_values[i][1] = ((function2_values[i+1] / 2) - (function2_values[i-1] / 2))/(grid[i+1] - grid[i])
    d2function2_values[i][0] = ((function2_values[i-2] / 3) - (function2_values[i-1] / 3) - (function2_values[i+1] / 3) + (function2_values[i+2] / 3))/((grid[i+1] - grid[i])**2)
    d2function2_values[i][1] = (function2_values[i+1] - (2 * function2_values[i]) + function2_values[i-1])/((grid[i+1] - grid[i])**2)
    dfunction2_error[0] = dfunction2_error[0] + (dfunction2_values[i][0] - dfunction2_real[i])**2
    dfunction2_error[1] = dfunction2_error[1] + (dfunction2_values[i][1] - dfunction2_real[i])**2
    d2function2_error[0] = d2function2_error[0] + (d2function2_values[i][0] - d2function2_real[i])**2
    d2function2_error[1] = d2function2_error[1] + (d2function2_values[i][1] - d2function2_real[i])**2
for i in range (0, 2):
    dfunction2_error[i] = np.sqrt(dfunction2_error[i])
    d2function2_error[i] = np.sqrt(d2function2_error[i])
print('rounding error of the first order derivative: quadratic function')
print('method 1:',dfunction2_error[0])
print('method 2:',dfunction2_error[1])
print('rounding error of the second order derivative: quadratic function')
print('method 3:',d2function2_error[0])
print('method 4:',d2function2_error[1])

#cubic function
function3_values = function3(grid)
dfunction3_real = np.zeros(len(grid))
d2function3_real = np.zeros(len(grid))
dfunction3_values = np.zeros((len(grid), 2))
d2function3_values = np.zeros((len(grid), 2))
dfunction3_error = np.zeros(2)
d2function3_error = np.zeros(2)
for i in range(2, len(grid)-2):
    dfunction3_real[i] = dfunction3(grid[i])
    d2function3_real[i] = d2function3(grid[i])
    dfunction3_values[i][0] = ((function3_values[i-2] / 12) - (2 * function3_values[i-1] / 3) + (2 * function3_values[i+1] / 3) - (function3_values[i+2] / 12))/(grid[i+1] - grid[i])
    dfunction3_values[i][1] = ((function3_values[i+1] / 2) - (function3_values[i-1] / 2))/(grid[i+1] - grid[i])
    d2function3_values[i][0] = ((function3_values[i-2] / 3) - (function3_values[i-1] / 3) - (function3_values[i+1] / 3) + (function3_values[i+2] / 3))/((grid[i+1] - grid[i])**2)
    d2function3_values[i][1] = (function3_values[i+1] - (2 * function3_values[i]) + function3_values[i-1])/((grid[i+1] - grid[i])**2)
    dfunction3_error[0] = dfunction3_error[0] + (dfunction3_values[i][0] - dfunction3_real[i])**2
    dfunction3_error[1] = dfunction3_error[1] + (dfunction3_values[i][1] - dfunction3_real[i])**2
    d2function3_error[0] = d2function3_error[0] + (d2function3_values[i][0] - d2function3_real[i])**2
    d2function3_error[1] = d2function3_error[1] + (d2function3_values[i][1] - d2function3_real[i])**2
for i in range (0, 2):
    dfunction3_error[i] = np.sqrt(dfunction3_error[i])
    d2function3_error[i] = np.sqrt(d2function3_error[i])
print('error of the first order derivative: cubic function')
print('method 1:',dfunction3_error[0])
print('method 2:',dfunction3_error[1])
print('error of the second order derivative: cubic function')
print('method 3:',d2function3_error[0])
print('method 4:',d2function3_error[1])

#quartic function
function4_values = function4(grid)
dfunction4_real = np.zeros(len(grid))
d2function4_real = np.zeros(len(grid))
dfunction4_values = np.zeros((len(grid), 2))
d2function4_values = np.zeros((len(grid), 2))
dfunction4_error = np.zeros(2)
d2function4_error = np.zeros(2)
for i in range(2, len(grid)-2):
    dfunction4_real[i] = dfunction4(grid[i])
    d2function4_real[i] = d2function4(grid[i])
    dfunction4_values[i][0] = ((function4_values[i-2] / 12) - (2 * function4_values[i-1] / 3) + (2 * function4_values[i+1] / 3) - (function4_values[i+2] / 12))/(grid[i+1] - grid[i])
    dfunction4_values[i][1] = ((function4_values[i+1] / 2) - (function4_values[i-1] / 2))/(grid[i+1] - grid[i])
    d2function4_values[i][0] = ((function4_values[i-2] / 3) - (function4_values[i-1] / 3) - (function4_values[i+1] / 3) + (function4_values[i+2] / 3))/((grid[i+1] - grid[i])**2)
    d2function4_values[i][1] = (function4_values[i+1] - (2 * function4_values[i]) + function4_values[i-1])/((grid[i+1] - grid[i])**2)
    dfunction4_error[0] = dfunction4_error[0] + (dfunction4_values[i][0] - dfunction4_real[i])**2
    dfunction4_error[1] = dfunction4_error[1] + (dfunction4_values[i][1] - dfunction4_real[i])**2
    d2function4_error[0] = d2function4_error[0] + (d2function4_values[i][0] - d2function4_real[i])**2
    d2function4_error[1] = d2function4_error[1] + (d2function4_values[i][1] - d2function4_real[i])**2
for i in range (0, 2):
    dfunction4_error[i] = np.sqrt(dfunction4_error[i])
    d2function4_error[i] = np.sqrt(d2function4_error[i])
print('error of the first order derivative: quartic function')
print('method 1:',dfunction4_error[0])
print('method 2:',dfunction4_error[1])
print('error of the second order derivative: quartic function')
print('method 3:',d2function4_error[0])
print('method 4:',d2function4_error[1])
                                   

#question 3.2 investigate the properties of the truncation error

print('question 3.2')

#using the result of question 2
print('numerical error of the first order derivative: trigonometric function')
print('method 1:',df_error[0])
print('method 2:',df_error[1])
print('numerical error of the second order derivative: trigonometric function')
print('method 3:',d2f_error[0])
print('method 4:',d2f_error[1])