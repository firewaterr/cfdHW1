# cfdHW2
First version of CFD homework 2.
First,  I installed git to my computer. I learned how to use git with Visual Studio Code. I tried to upload my first code to my github account. It's all right.
Then, I created a frame of my code. The calculating method may be wrong, but it gives out good outputs.
# 代码运行指南
本次作业涉及的代码包括'homework.py'和'homework-question4.py'两个文件，使用的语言是python，运行时需要使用numpy软件包。

数值验证格式精度时，我将格点数减少了一倍，也就是取q=2，用事后验证的公式即可得到数值精度。具体见'homework..py'文件

numpy默认使用双精度浮点值，为了分析单精度和双精度的影响，'homework-question4.py'文件中用'np.float32'语句将所有双精度浮点运算改为单精度浮点运算。对比两份代码中截断误差的不同，就可以看出单精度和双精度的影响。