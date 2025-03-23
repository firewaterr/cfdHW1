# cfdHW2
First version of CFD homework 2.

First,  I installed git to my computer. I learned how to use git with Visual Studio Code. I tried to upload my first code to my github account. It's all right.

Then, I created a frame of my code. The calculating method may be wrong, but it gives out good outputs.

2025.3.23 Most questions finished. I still need to finish README.md.
# 代码运行指南
本次作业涉及的代码包括'homework.py'和'homework-question4.py'两个文件，使用的语言是python，运行时需要使用numpy软件包。运行'homework.py'文件可以得到作业第二问、第三问的结果；运行'homework-question4.py'文件可得到作业第四问的结果。

请注意，代码输出结果中的method1~method4对应报告中的公式（1）~（4）

数值验证格式精度时，我将格点数减少了一倍，也就是取q=2（近似），用事后验证的公式即可得到数值精度。具体见'homework.py'文件中question2部分，可以看出，一阶微分的第一种格式，数值精度为四阶，一阶微分的第二种格式和二阶微分的两种格式，数值精度均为二阶；

研究舍入误差和截断误差时，我采用了一次、二次、三次、四次方程四种来研究。具体见'homework.py'文件中question3部分。对于一次、二次方程，四种格式均无截断误差，舍入误差较小，但可以发现，二阶微分的舍入误差比一阶微分的舍入误差大两个数量级，这是因为作二阶微分时，除数和被除数都更小，所以误差增长较大。到了三次、四次方程，可以看出一阶微分的两种格式精度相差很大，此时截断误差起主要效果。

numpy默认使用双精度浮点值，为了分析单精度和双精度的影响，'homework-question4.py'文件中用'np.float32'语句将所有双精度浮点运算改为单精度浮点运算。对比两份代码中误差的不同，可以看出，单精度浮点运算比双精度误差大很多。