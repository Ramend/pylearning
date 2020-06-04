from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

#windows和linux设置字体的方式
# font = {'family': 'Microsoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
#
# matplotlib.rc("font", **font)

#另外一种设置字体的方式
my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴刻度
_xticks_labels = ["10点{}分".format(i) for i in range(60)]
_xticks_labels += ["11点{}分".format(i) for i in range(60)]

# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xticks_labels[::3], rotation=45, fontproperties = my_font)  # rotation旋转的度数

#添加描述信息

plt.show()
