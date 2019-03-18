import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,50)
y1 = 2 * x + 1
y2 = x ** 2


plt.figure()
#plt.figure(figsize=(8, 6), dpi=80) # 创建一个8x6大小的figure，并设置每英寸80个像素点


# plt.subplot(111) # 创建在1x1的位置创建一个subplot
#  #subplot是用来布局plots的，需要指定（行、列、序号）

# ======================================================================画图

plt.plot(x, y1, color='red', linewidth=1.0, linestyle='-', label = "2x+1")  #plot()为画线函数
plt.plot(x, y2, color='blue', linewidth=1.0, linestyle='--', label = "x**2")

# ==========================================绘制折线图

# x = [1, 2, 3, 4, 5]# Make an array of x values
# y = [1, 4, 9, 16, 25]# Make an array of y values for each x value
#
# plt.plot(x, y)# use pylab to plot x and y
# plt.show()# show the plot on the screen

# ==========================================绘制散点图

# s表示点的大小，c就是color，marker点的形状(o,x),alpha透明度，label标签
# plt.scatter(x[],y[],s=30,c='red',marker='o',alpha=0.5,label='x1')
#
# # 把pl.plot(x, y)改成pl.plot(x, y, 'o')
# 红色：把pl.plot(x, y, 'o')改成pl.plot(x, y, ’or’)
# 虚线:plot(x,y, '--')
# 蓝色星型markers：plot(x,y, ’b*’)

# ======================================================================折线角标

plt.legend(loc = 'best', frameon=False) # 角标  'upper left', frameon=True的话，右上角的声明会在一个框内


'''

使用Line2D对象的setter方法。plot函数返回Line2D对象列表
lines = plt.plot(x1, y1, x2, y2)
可以用setp()命令来进行设置，该命令可以对一个列表或者单个对象进行设置，并且提供了matlab式的使用方法
# use keyword args
plt.setp(lines, color='r', linewidth=2.0)
# or MATLAB style string value pairs
plt.setp(lines, 'color', 'r', 'linewidth', 2.0)

'''
# ======================================================================坐标轴范围

# axis()函数给出了形如[xmin,xmax,ymin,ymax]的列表，指定了坐标轴的范围
plt.xlim(-1,2) #x轴范围
plt.ylim(-2,3) #y轴范围

# ======================================================================给坐标轴加注释

plt.xlabel('this is x')  #给x加注释
plt.ylabel('this is y')  #给y加注释

# ======================================================================设置坐标轴标记

new_ticks = np.linspace(-1,2,5)
# print(new_ticks)
plt.xticks(new_ticks) # 设置坐标轴角标
plt.yticks([-2,-1.8,-1,1.37,3],
            [r'$bad$',r'$not\ very\ bad$',r'$noraml$',r'$good$',r'$very\ good$'])
#  r''是为了转义里面的转义字符\

# ======================================================================移动坐标轴
# gca ===> get current axis
ax = plt.gca()

#spines包括图片上下左右4条边界和它们的下标，就是正方形的4条边。
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# set_position中的参数元组的第二个值可取-1，0，1分别代表相对‘data’的不同的位置
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

# ======================================================================标记特征点

x_1 = -0.8
x_2 = -0.8
y_1 = 2 * x_1 + 1
y_2 = x_2 ** 2

plt.plot([x_1,x_1],[0,y_1], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([x_1,],[y_1,], 50, color ='red')
plt.plot([x_2,x_2],[0,y_2], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([x_2,],[y_2,], 50, color ='blue')
# 第一个参数s为要标记上去的文本
# 第二个参数xy为标记的位置，必须是可迭代对象（如tuple，list）
# 第三个对象xycoords表示xy的参考系
# 第四个对象xytext为标记文本相对标记位置的位置，必须是可迭代对象iterabl
# 第五个对象textcoords表示xytext的参考系
# 第六个对象fontsize为字体大小
# 第七个对象arrowprops为箭头样式
plt.annotate(r'$2*x+1=-0.6$', xy=(x_1, y_1), xycoords='data',
                xytext=(-50, -50), textcoords='offset points', fontsize=6,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate(r'$x**2=0.64$', xy=(x_2, y_2), xycoords='data',
                xytext=(+10, +30), textcoords='offset points', fontsize=6,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))




# ======================================================================显示

plt.show() # 在屏幕上显示

# ======================================================================直方图


"""
绘制直方图
data:绘图数据
bins:直方图的长条形数目，默认为10
normed:是否将得到的直方图向量归一化，默认为0代表不归一化，显示频数。normed=1表示归一化，显示频率。
facecolor:长条形的颜色
edgecolor:长条形边框的颜色
alpha:透明度
"""
# plt.hist(data, bins, normed, facecolor, edgecolor, alpha)

"""
绘制条形图
left:长条形中点横坐标
height:长条形高度
width:长条形宽度，默认值0.8
alpha:透明度
color:颜色
label:标志
"""
# plt.bar(left, height, width, alpha, color, label)


"""
绘制水平条形图 barh
参数一：y轴
参数二：x轴
"""
# plt.barh(y, x, height, color, alpha)



#   http://www.labri.fr/perso/nrougier/teaching/matplotlib/


#   https://blog.csdn.net/hustqb/article/details/76237005
