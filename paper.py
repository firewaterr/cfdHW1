import numpy as np

def function(x):
    return np.sin(x)
def dfunction(x):
    return np.cos(x)
def d2function(x):
    return -np.sin(x)
def function1(x):
    return 7 * x + 9
def dfunction1(x):
    return 7
def d2function1(x):
    return 0
def function2(x):
    return 5 * x**2 + 7 * x + 9
def dfunction2(x):
    return 10 * x + 7
def d2function2(x):
    return 10
def function3(x):
    return 3 * x**3 + 5 * x**2 + 7 * x + 9
def dfunction3(x):
    return 9 * x**2 + 10 * x + 7
def d2function3(x):
    return 18 * x + 10
def function4(x):
    return 1 * x**4 + 3 * x**3 + 5 * x**2 + 7 * x + 9
def dfunction4(x):
    return 4 * x**3 + 9 * x**2 + 10 * x + 7
def d2function4(x):
    return 12 * x**2 + 18 * x + 10

grid = np.linspace(0, 10 * np.pi, 5004)
grid_2 = np.linspace(0, 10 * np.pi, 10004)

f_values = function(grid)
df_real = dfunction(grid)
d2f_real = d2function(grid)
df_values = np.zeros((len(grid), 2))
d2f_values = np.zeros((len(grid), 2))

#question 2
df_error = np.zeros(2)
d2f_error = np.zeros(2)
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
df_error_2 = np.zeros(2)
d2f_error_2 = np.zeros(2)
f_values_2 = function(grid_2)
df_real_2 = dfunction(grid_2)
d2f_real_2 = d2function(grid_2)
df_values_2 = np.zeros((len(grid_2), 2))
d2f_values_2 = np.zeros((len(grid_2), 2))
for i in range(2, len(grid)-2):#注意长度应和grid相同
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

df_accuracy = np.zeros(2)
d2f_accuracy = np.zeros(2)
p = (grid[1] - grid[0]) / (grid_2[1] - grid_2[0])
df_accuracy[0] = np.log(df_error[0] / df_error_2[0]) / np.log(p)
df_accuracy[1] = np.log(df_error[1] / df_error_2[1]) / np.log(p)
d2f_accuracy[0] = np.log(d2f_error[0] / d2f_error_2[0]) / np.log(p)
d2f_accuracy[1] = np.log(d2f_error[1] / d2f_error_2[1]) / np.log(p)
print('numerical accuracy of the first order derivative:')
print(df_accuracy)
print('numerical accuracy of the second order derivative:')
print(d2f_accuracy)
print(p)
