# count = 10
# nums = []
# for i in range(count):
#     nums.insert(0, i)
# print(nums)
#     nums.append(i)
# nums.reverse()
# print(nums)

# from collections import Counter
#
# num1 = []
# num2 = []
# word1 = "debit card"
# word2 = "bad creditasdsad"
# for i1 in word1:
#     num1 += i1
# print(num1)
# for i2 in word2:
#     num2 += i2
# print(num2)
# c = Counter(num1)
# print(c)
# d = Counter(num2)
# print(d)
# if c == d:
#     print(True)
# else:
#     print(False)
import matplotlib.pyplot
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


# 线性回归算法
# """创建数据"""
# x = np.linspace(3, 6, 40)
# y = 3 * x + 2
# x = x + np.random.rand(40)
#
# #由于fit 需要传入二维矩阵数据，因此需要处理x，y的数据格式,将每个样本信息单独作为矩阵的一行
# x = [[i] for i in x]
# y = [[i] for i in y]
# # 构建线性回归模型
# model = linear_model.LinearRegression()
#
# # 训练模型，"喂入"数据
# model.fit(x, y)
#
# # 准备测试数据 x_，这里准备了三组，如下
# x_ = [[4], [5], [6]]
#
# # 打印预测结果
# y_ = model.predict(x_)
# print(y_)
# print("w的值为：", model.coef_)
# print("b截距的值为：", model.intercept_)
#
# #数据集绘制,散点图，图像满足函假设函数图像
# plt.scatter(x, y)
#
# #绘制最佳拟合直线
#
# plt.plot(x_, y_, color="red", linewidth=3.0, linestyle="-")
# plt.legend(["func", "Data"], loc=0)
# plt.show()

# 神经网络分类算法
def main():
    iris = datasets.load_iris()  # 加载鸢尾花数据集
    # 用pandas处理数据集
    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    print(iris.feature_names)
    #数据集标记值 iris.target
    data['class'] = iris.target
    # 此处只取两类 0/1 两个类别的鸢尾花，设置类别不等于 2
    data = data[data['class'] != 2]
    # 对数据集进行归一化和标准化处理
    scaler = StandardScaler()
    # 选择两个特征值（属性）
    X = data[['sepal length (cm)', 'petal length (cm)']]
    #计算均值和标准差
    scaler.fit(X)
    # 标准化数据集（数据转化）
    X = scaler.transform(X)
    # 'class'为列标签，读取100个样本的的列表
    Y = data[['class']]
    # 划分数据集
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
    # 创建神经网络分类器
    mpl = MLPClassifier(solver='lbfgs', activation='logistic')
    # 训练神经网络模型
    mpl.fit(X_train, Y_train)
    # 打印模型预测评分
    print('Score:\n', mpl.score(X_test, Y_test))
    # 划分网格区域
    h = 0.02
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))
    Z = mpl.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    #画三维等高线图，并对轮廓线进行填充
    plt.contourf(xx, yy, Z,cmap='summer')
    # 绘制散点图
    class1_x = X[Y['class'] == 0, 0]
    class1_y = X[Y['class'] == 0, 1]
    l1 = plt.scatter(class1_x, class1_y, color='b', label=iris.target_names[0])
    class2_x = X[Y['class'] == 1, 0]
    class2_y = X[Y['class'] == 1, 1]
    l2 = plt.scatter(class2_x, class2_y, color='r', label=iris.target_names[1])
    plt.legend(handles=[l1, l2], loc='best')
    plt.grid(True)
    plt.show()
# main()

# N = neuralNetwork()
# from PIL import Image
# image = Image.open("D:/Work aids/9.png")
# arr = []
# for i in range(28):
#     for j in range(28):
#         pixel = 255.0 - float(image.getpixel(j,i))
#         pixel2 = (pixel/255.0*0.99)+0.01
#         arr.append(pixel2)
# image_array = numpy.asfarray(arr).reshape((28,28))
# matplotlib.pyplot.imshow(image_array,cmap='Greys',interpolation='None')
# label2 = numpy.argmax(N.query(arr))


