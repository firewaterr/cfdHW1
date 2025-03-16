import numpy as np


def f(j, x, a = 1, b = 2, c = 3, d = 4): 
    if j == 0:
        return np.sin(x)
    elif j == 1:
        return a*x + b
    elif j == 2:
        return a*x**2 + b*x + c
    elif j == 3:
        return a*x**3 + b*x**2 + c*x + d

def df(j, x, a = 1, b = 2, c = 3, d = 4):
    if j == 0:
        return np.cos(x)
    elif j == 1:
        return a
    elif j == 2:
        return 2*a*x + b
    elif j == 3:
        return 3*a*x**2 + 2*b*x + c

def d2f(j, x, a = 1, b = 2, c = 3, d = 4):
    if j == 0:
        return -np.sin(x)
    elif j == 1:
        return 0
    elif j == 2:
        return 2*a
    elif j == 3:
        return 6*a*x + 2*b

grid = np.linspace(0, 2*np.pi, 1004)
f_values = np.zeros(len(grid))
df_values = np.zeros((len(grid), 2))
d2f_values = np.zeros((len(grid), 2))
df_real = np.zeros(len(grid))
d2f_real = np.zeros(len(grid))
df_error = np.zeros(2) 
d2f_error = np.zeros(2)

for j in range (0, 4):
    for i in range (0, len(grid)): 
        f_values[i] = f(j, grid[i])
        df_real[i] = df(j, grid[i])
        d2f_real[i] = d2f(j, grid[i])
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
    print(df_error)
    print(d2f_error)
