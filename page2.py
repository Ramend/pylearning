from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]

# 设置图形大小
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴刻度
_xticks_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, _xticks_labels, fontproperties=my_font)

# 添加描述信息
plt.xlabel("年龄", fontproperties=my_font)
plt.ylabel("个数", fontproperties=my_font)
plt.title("11岁到30岁谈对象的个数", fontproperties=my_font)

# 展示
plt.show()
