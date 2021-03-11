import matplotlib.pyplot as plt
import numpy as np


#使绘图支持中文
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
#创建两行两列的子图像
fig, [[ax1,ax2],[ax3,ax4],[ax5,ax6]] = plt.subplots(nrows=3, ncols=2,figsize=(8,8))

#绘制柱状图bar
value = (2, 3, 4, 1, 2)
index = np.arange(5) #从0-5有序排列
ax1.bar(index, value,alpha=0.4, color='b')
ax1.set_xlabel('Group')
ax1.set_ylabel('Scores')
ax1.set_title('柱状图')

#绘制直方图histogram
h = 100 + 15 * np.random.randn(437) #randn有正态分布那味了，取值[0,1]
ax2.hist(h, bins=50)
ax2.title.set_text('直方图')

#绘制饼图pie
labels = 'Frogs', 'Cai', 'Yongji', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
ax3.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax3.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax3.title.set_text('饼图')

#绘制棉棒图stem
x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)
ax4.stem(x,y, linefmt="-.", markerfmt="o", basefmt='-')
ax4.set_title("棉棒图")

#绘制气泡图scatter
a = np.random.randn(100)
b = np.random.randn(100)
ax5.scatter(a, b, s=np.power(2*a+4*b,2), c=np.random.rand(100), cmap=plt.cm.RdYlBu, marker="o")

#绘制极线图polar
fig.delaxes(ax6)

ax6 = fig.add_subplot(236, projection='polar')
#ax6 = fig.add_subplot(2,3,6, projection='polar')#2行，3列，第6个图
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
ax6.plot(theta, r)
ax6.set_rmax(2)
ax6.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax6.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax6.grid(True)

#调整子图像的布局
fig.subplots_adjust(wspace=1,hspace=1.2)
fig.suptitle("图形绘制",fontsize=16)

plt.show()