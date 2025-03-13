import numpy as np


def f(x, a = 1, b = 0, c = 0):
    return np.sin(x)

grid = np.linspace(0, 2*np.pi, 104)

f_values = f(grid)

df_values = np.zeros((len(grid), 2))
d2f_values = np.zeros((len(grid), 2))

df_real = np.cos(grid)
d2f_real = -np.sin(grid)

df_error = np.zeros((len(grid), 2))
d2f_error = np.zeros((len(grid), 2))


for i in range(2, len(grid)-2):
    df_values[i][0] = (f_values[i+1] - f_values[i-1])/(grid[i+1] - grid[i-1])
    d2f_values[i][0] = (f_values[i+1] - 2*f_values[i] + f_values[i-1])/((grid[i+1] - grid[i])**2)
    df_values[i][1] = (f_values[i+2] - f_values[i-2])/(grid[i+2] - grid[i-2])
    d2f_values[i][1] = (f_values[i+2] - 2*f_values[i] + f_values[i-2])/((grid[i+2] - grid[i])**2)
    df_error[i][0] = (df_values[i][0] - df_real[i])**2
    d2f_error[i][0] = (d2f_values[i][0] - d2f_real[i])**2
    df_error[i][1] = (df_values[i][1] - df_real[i])**2
    d2f_error[i][1] = (d2f_values[i][1] - d2f_real[i])**2

print(df_error)
print(d2f_error)
