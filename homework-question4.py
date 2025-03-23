import numpy as np

# Define all the functions I need
def function(x):  # sin(x)
    return np.sin(x)

def dfunction(x):  # first order derivative of sin(x)
    return np.cos(x)

def d2function(x):  # second order derivative of sin(x)
    return -np.sin(x)

# Question 4: Investigate the difference between float32 and float64
# Grid initialization
grid_float32 = np.linspace(0, 10 * np.pi, 5004, dtype=np.float32)
grid_float64 = np.linspace(0, 10 * np.pi, 5004, dtype=np.float64)

# Values in grid
# Calculate the real value of the function, first order derivative, and second order derivative
f_values_float32 = function(grid_float32)
df_real_float32 = dfunction(grid_float32)
d2f_real_float32 = d2function(grid_float32)

f_values_float64 = function(grid_float64)
df_real_float64 = dfunction(grid_float64)
d2f_real_float64 = d2function(grid_float64)

# Define arrays to store numerical values and errors
df_values_float32 = np.zeros((len(grid_float32), 2), dtype=np.float32)
d2f_values_float32 = np.zeros((len(grid_float32), 2), dtype=np.float32)
df_error_float32 = np.zeros(2, dtype=np.float32)
d2f_error_float32 = np.zeros(2, dtype=np.float32)

df_values_float64 = np.zeros((len(grid_float64), 2), dtype=np.float64)
d2f_values_float64 = np.zeros((len(grid_float64), 2), dtype=np.float64)
df_error_float64 = np.zeros(2, dtype=np.float64)
d2f_error_float64 = np.zeros(2, dtype=np.float64)

# Calculate the numerical value of the first and second order derivative
# Calculate the error of the first and second order derivative
for i in range(2, len(grid_float32) - 2):
    # float32 calculations
    df_values_float32[i][0] = ((f_values_float32[i - 2] / 12) - (2 * f_values_float32[i - 1] / 3) + (2 * f_values_float32[i + 1] / 3) - (f_values_float32[i + 2] / 12)) / (grid_float32[i + 1] - grid_float32[i])
    df_values_float32[i][1] = ((f_values_float32[i + 1] / 2) - (f_values_float32[i - 1] / 2)) / (grid_float32[i + 1] - grid_float32[i])
    d2f_values_float32[i][0] = ((f_values_float32[i - 2] / 3) - (f_values_float32[i - 1] / 3) - (f_values_float32[i + 1] / 3) + (f_values_float32[i + 2] / 3)) / ((grid_float32[i + 1] - grid_float32[i]) ** 2)
    d2f_values_float32[i][1] = (f_values_float32[i + 1] - (2 * f_values_float32[i]) + f_values_float32[i - 1]) / ((grid_float32[i + 1] - grid_float32[i]) ** 2)
    df_error_float32[0] += (df_values_float32[i][0] - df_real_float32[i]) ** 2
    df_error_float32[1] += (df_values_float32[i][1] - df_real_float32[i]) ** 2
    d2f_error_float32[0] += (d2f_values_float32[i][0] - d2f_real_float32[i]) ** 2
    d2f_error_float32[1] += (d2f_values_float32[i][1] - d2f_real_float32[i]) ** 2

    # float64 calculations
    df_values_float64[i][0] = ((f_values_float64[i - 2] / 12) - (2 * f_values_float64[i - 1] / 3) + (2 * f_values_float64[i + 1] / 3) - (f_values_float64[i + 2] / 12)) / (grid_float64[i + 1] - grid_float64[i])
    df_values_float64[i][1] = ((f_values_float64[i + 1] / 2) - (f_values_float64[i - 1] / 2)) / (grid_float64[i + 1] - grid_float64[i])
    d2f_values_float64[i][0] = ((f_values_float64[i - 2] / 3) - (f_values_float64[i - 1] / 3) - (f_values_float64[i + 1] / 3) + (f_values_float64[i + 2] / 3)) / ((grid_float64[i + 1] - grid_float64[i]) ** 2)
    d2f_values_float64[i][1] = (f_values_float64[i + 1] - (2 * f_values_float64[i]) + f_values_float64[i - 1]) / ((grid_float64[i + 1] - grid_float64[i]) ** 2)
    df_error_float64[0] += (df_values_float64[i][0] - df_real_float64[i]) ** 2
    df_error_float64[1] += (df_values_float64[i][1] - df_real_float64[i]) ** 2
    d2f_error_float64[0] += (d2f_values_float64[i][0] - d2f_real_float64[i]) ** 2
    d2f_error_float64[1] += (d2f_values_float64[i][1] - d2f_real_float64[i]) ** 2

# Calculate the final errors
for i in range(2):
    df_error_float32[i] = np.sqrt(df_error_float32[i])
    d2f_error_float32[i] = np.sqrt(d2f_error_float32[i])
    df_error_float64[i] = np.sqrt(df_error_float64[i])
    d2f_error_float64[i] = np.sqrt(d2f_error_float64[i])

# Output the results
print('numerical error of the first order derivative (float32):')
print('method 1:', df_error_float32[0])
print('method 2:', df_error_float32[1])

print('numerical error of the second order derivative (float32):')
print('method 3:', d2f_error_float32[0])
print('method 4:', d2f_error_float32[1])

print('numerical error of the first order derivative (float64):')
print('method 1:', df_error_float64[0])
print('method 2:', df_error_float64[1])

print('numerical error of the second order derivative (float64):')
print('method 3:', d2f_error_float64[0])
print('method 4:', d2f_error_float64[1])