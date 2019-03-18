import numpy as np
# =======================================================
# #numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
# #order C（按行）、F（按列）或A（任意，默认）  ndmin 指定返回数组的最小维数。
# #int8，int16，int32，int64 可替换为等价的字符串 'i1'，'i2'，'i4'，以及其他。
a = np.array([[1,2,3],[4,5,6]], dtype = np.int16)

b = np.zeros((3,4)) #三行四列 默认float类型

c = np.ones((3,4),dtype=np.int16)

d = np.empty((3,4)) # 创建全空数组 但其实接近于0

e = np.arange(10,20,2) #10 12 14 16 18 最后一个为步长

f = np.arange(12).reshape((3,4))

g = np.linspace(1,10,20) # 20段1到10的list

# print (a,b,c,d,e,f,g)

r = [1 ,2, 3]
r1 = (1, 2, 3)
s = np.asarray(r) # 将现有的参数转换为数组
s1 = np.asarray(r1)
# print(s, s1)

t = np.logspace(1.0, 2.0, num = 10, base = 10) # 在对数刻度上均匀分布的数字 刻度的开始和结束端点是某个底数的幂，通常为 10。
# print (t) # [10 - 100] 10 10^1.1 10^1.2。。。。。。10^2

u = np.arange(10)
v = slice(2,7,2)
# print (u[v]) # ==> u[2:7:2] 切片操作 u[3:] 从第3位到最后
# #多维数组 f 3*4       第二行 f[1, ...] 第一列 f[..., 0]    第二列其他元素f[...,1:]
# #切片 f[1:2,[2,3]] f[0:1,2:3]
w = np.array([[1+2j,2],[3,4+5j]])
# print (w[np.iscomplex(w)]) # 取复数
# print (w[~np.iscomplex(w)]) # 取非复数
x = np.array([12, 3.4, np.nan, 5,6])
# print (x[~np.isnan(x)]) # 过滤not a numeber

# ==================================================运算符
a1 = np.array([10,20,30,40])
a2 = np.arange(4)

a3 = a1-a2
a4 = a1+a2
a5 = a1*a2
a6 = a1**2
a7 = 10*np.sin(a1)
a8 = 10*np.cos(a1)

# print (a2<3) # 返回对应项的布尔值
# print (a2[a2<3]) #返回小于3的值
# print (a3)

a9 = a1 + f # a1 1*4 f 3*4
# print(a9) # 会将a1补齐 然后对应项相加 a1第2，3行补第1行内容

# print(f.T) # f的转置
# print(np.transpose(f)) # == f.T


# for y in np.nditer(f.T, order = 'F'): # 按列读取 在数组上进行迭代
# # for y in np.nditer(f, op_flags = ['readwrite']):# 修改数组元素
# #     y[...] = 2*y #
#     print(y)
#
#
# for y1,y2 in np.nditer([a1,f]):  #两个数组
#     print(y1,y2)


b1 = np.array([[1,2],[3,4]])
b2 = np.arange(4).reshape((2,2))
# #加减乘除 add(), subtract(), multiply(), divide()

b3 = b1*b2 #对应相乘
b4 = np.dot(a,b) #矩阵的乘法
b4_1 = a.dot(b) # b4 = b4_1

# numpy.dot()返回两个数组的点积。 对于二维向量，其等效于矩阵乘法。 对于一维数组，它是向量的内积。
# 对于 N 维数组，它是a的最后一个轴上的和与b的倒数第二个轴的乘积。
#
# numpy.vdot()函数返回两个向量的点积。
# 如果第一个参数是复数，那么它的共轭复数会用于计算。 如果参数id是多维数组，它会被展开。
#
# numpy.inner()此函数返回一维数组的向量内积。
# 对于更高的维度，它返回最后一个轴上的和的乘积。
#
# numpy.matmul()函数返回两个数组的矩阵乘积。
# 虽然它返回二维数组的正常乘积，但如果任一参数的维数大于2，则将其视为存在于最后两个索引的矩阵的栈，并进行相应广播。


b5 = np.pi
print(b4)
c1 = np.random.random((2,4))
# print(np.sum(c1)) # axis = 1 行中寻找    axis = 0 列中寻找
np.min(c1)
np.max(c1)
# #numpy.amin() 和 numpy.amax()从给定数组中的元素沿指定轴返回最小值和最大值。



# #numpy.around(a,decimals)decimals 要舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
# # numpy.floor()此函数返回不大于输入参数的最大整数
# # numpy.ceil()此函数返回不小于于输入参数的最小整数
# # #numpy.mod() 返回输入数组中相应元素的除法余数
# # numpy.real() 返回复数类型参数的实部。
# # numpy.imag() 返回复数类型参数的虚部。
# # numpy.conj() 返回通过改变虚部的符号而获得的共轭复数。
# # numpy.angle() 返回复数参数的角度。 函数的参数是degree。 如果为true，返回的角度以角度制来表示，否则为以弧度制来表示。
# # numpy.power()此函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。

# # numpy.ptp()函数返回沿轴的值的范围（最大值 - 最小值）。
# #============================二进制

# # np.binary_repr(int, width = 8)  将int 二进制表示
# # np.bitwise_and()函数对输入数组中的整数的二进制表示的相应位执行位与运算。
# # np.bitwise_or()函数对输入数组中的整数的二进制表示的相应位执行位或运算。
# # np.invert() 计算输入数组中整数的位非结果。 对于有符号整数，返回补码。
# # numpy.left shift()函数将数组元素的二进制表示中的位向左移动到指定位置，右侧附加相等数量的 0。
# # numpy.right_shift()函数将数组元素的二进制表示中的位向右移动到指定位置，左侧附加相等数量的 0。
#=====================================================字符串操作

# np.char.add(['hello'],['xyz'])函数执行按元素的字符串连接。
# numpy.char.multiply('Hello ',3)这个函数执行多重连接。
# numpy.char.center('hello', 20,fillchar = '*')此函数返回所需宽度的数组，以便输入字符串位于中心，并使用fillchar在左侧和右侧进行填充。
# numpy.char.capitalize('hello world')函数返回字符串的副本，其中第一个字母大写
# np.char.title('hello how are you?')返回输入字符串的按元素标题转换版本，其中每个单词的首字母都大写。
# np.char.lower(['HELLO','WORLD']) 函数返回一个数组，其元素转换为小写。它对每个元素调用str.lower。
# np.char.upper(['hello','world'])函数返回一个数组，其元素转换为大写。它对每个元素调用str.upper。
# np.char.split ('hello how are you?') 返回输入字符串中的单词列表。 默认情况下，空格用作分隔符。 否则，指定的分隔符字符用于分割字符串。
# np.char.splitlines('hello\nhow are you?') 函数返回数组中元素的单词列表，以换行符分割。
# np.char.strip(['arora','admin','java'],'a') 函数返回数组的副本，其中元素移除了开头或结尾处的特定字符。['ror' 'dmin' 'jav']
# np.char.join([':','-'],['dmy','ymd'])这个函数返回一个字符串，其中单个字符由特定的分隔符连接。
# np.char.replace ('He is a good boy', 'is', 'was')这个函数返回字符串副本，其中所有字符序列的出现位置都被另一个给定的字符序列取代。
# np.char.encode('hello', 'cp500') 对数组中的每个元素调用str.encode函数。 默认编码是utf_8，可以使用标准 Python 库中的编解码器。
# np.char.decode('hello', 'cp500') 在给定的字符串中使用特定编码调用str.decode()。

#=====================================================
d1 = np.arange(2,14).reshape((3,4)) # d1.shape(3,4) 也会修改
# print(d1.shape) #
# print(d1.ndim) #返回最小的维度 行列两个维度
# print(d1.itemsize) #返回数组中每个元素的字节单位长度  int8为一个字节 默认int64

# # 数组扁平化
# # numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响原始矩阵，而numpy.ravel()返回的是视图，影响原始矩阵。
# print(d1.flatten())
# print(d1.ravel()) #
# d1.ravel()[1] = 1000 #形象原始矩阵


np.argmin(d1)  #最小值索引
np.argmax(d1)
np.mean(d1)  #平均值    = d1.mean()
np.average(d1) #同样求平均值
np.median(d1) # 中位数
std = sqrt(mean((d1 - d1.mean())**2)) # 标准差
# print(np.cumsum(d1)) # 逐位想加
# print(np.diff(d1)) # 累差
np.nonzero(d1) #非零的 两个list 第一个是行，第二个是列
np.sort(d1) # 排序 order 如果数组包含字段，则是要排序的字段
np.transpose(d1) #转置  = d1.T
np.clip(d1,3,9) #小于3变3 ，大于9变9
# # np.where()函数返回输入数组中满足给定条件的元素的索引。
# # np.extract(condition, x)extract()函数返回满足任何条件的元素。

#===========================================================数组 增删改查

h = np.arange(3,15)
# print(h[3])
j = np.arange(3,15).reshape((3,4))

# print (j[2])
# print (j[1][1])
# print (j[1,1])
# print (j[2,:])
# print (j[2,1:3])

# print(j1)

# for row in j:
#     print(row)
#
# for column in j.T:
#     print (column)
#
# print (j.flatten())   # 矩阵转list
# for item in j.flat:  # 迭代器
#     print (item)

j1 = np.resize(j,(6,2))
j2 = np.append(j1, [[2, 2]], axis = 0) # 行加
j3 = np.append(j1, [[1],[1],[1],[1],[1],[1]], axis = 1) #列加
# #numpy.insert(arr, obj, values, axis)arr：输入数组 obj：在其之前插入值的索引 values：要插入的值 axis：沿着它插入的轴，如果未提供，则输入数组会被展开
j4 = np.insert(j1, 3, [9, 9], axis = 0) #插入
print(j1)
print(j2)
print(j3)
print(j4)
# #numpy.delete(arr, obj, axis)
# #numpy.unique(arr, return_index, return_inverse, return_counts)
# #该函数能够返回一个元组，包含去重数组和相关索引的数组。
num1,indices1 = np.unique(j2.flatten(), return_index = True) #[ 2  3  4  5  6  7  8  9 10 11 12 13 14]
print(num1, '\n', indices1) # [12  0  1  2  3  4  5  6  7  8  9 10 11] 重复值望前方 返回遇到的第一个重的位置
num2,indices2 = np.unique(j2.flatten(), return_inverse = True) #[ 2  3  4  5  6  7  8  9 10 11 12 13 14]
print(num2, '\n', indices2) # [ 1  2  3  4  5  6  7  8  9 10 11 12  0  0] 返回重的位置 若此位置数重了 返回0

#==========================================================合并
k1 = np.array([1,1,1])
k2 = np.array([2,2,2])

# # numpy.stack(arrays, axis)
# print (np.vstack((k1,k2)))   # 上下合并  vertical stack 行合并
# print (np.hstack((k1,k2)))   # 左右合并  horizintal stack 列合并
k3 = np.vstack((k1,k2))
# print (k3.shape)

# k1.T #不能改变序列

k4 = k1[:,np.newaxis]  # 改变纬度 横向变纵向，list ==> 矩阵

k5 = np.concatenate((k1,k2,k2,k1),axis=0) #行合并 axis = 1 列合并

# ===============================================================分割

l = np.arange(12).reshape((3,4))
l1 = np.arange(9)
# print(np.split(l,2,axis=1)) # 行分割 分割成等量2份
# print(np.split(l,3,axis=0)) # 列分割 分割成等量3份 左右
print(np.split(l1,[4,7])) # 一维素组中 第4 第7位置分割 [array([0, 1, 2, 3]), array([4, 5, 6]), array([7, 8])]
# print(np.array_split(l,3,axis=1))  # 不等量分割
# print(np.vsplit(l,3)) #竖直分割 行分割
# print(np.hsplit(l,2)) #水平分割

# ================================================================copy
m = np.arange(4)
m1 = m
m2 = m.copy() ###deep copy

# 简单的赋值不会创建数组对象的副本。 相反，它使用原始数组的相同id()来访问它。 id()返回 Python 对象的通用标识符，类似于 C 中的指针。
# NumPy 拥有ndarray.view()方法，它是一个新的数组对象，并可查看原始数组的相同数据。 与前一种情况不同，新数组的维数更改不会更改原始数据的维数。

# ================================================================io
# load()和save()函数处理 numPy 二进制文件（带npy扩展名）
# loadtxt()和savetxt()函数处理正常的文本文件
