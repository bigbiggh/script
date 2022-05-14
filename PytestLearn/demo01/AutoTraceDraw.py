#coding=utf-8

import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600,0,0)
t.pencolor("red")
t.pensize(5)

# eval将字符串引号去掉
# map：将第一个参数对应的方法作用与第二个参数的每一个参数
datals = []
f = open("data")
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()

for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
