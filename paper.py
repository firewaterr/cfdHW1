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
print('rounding error of the first order derivative:')
print('method 1:',dfunction3_error[0])
print('method 2:',dfunction3_error[1])
print('rounding error of the second order derivative:')
print('method 3:',d2function3_error[0])
print('method 4:',d2function3_error[1])

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
print('rounding error of the first order derivative:')
print('method 1:',dfunction4_error[0])
print('method 2:',dfunction4_error[1])
print('rounding error of the second order derivative:')
print('method 3:',d2function4_error[0])
print('method 4:',d2function4_error[1])