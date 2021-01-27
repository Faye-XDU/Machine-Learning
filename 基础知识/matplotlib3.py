import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 400)
y = np.sin(x**2)
z = 1 / (1 + np.exp(-x))
a = np.random.randint(0,100,400)
b = np.maximum(x,0.1*x)

#创建两行两列的子图像
fig, ax_list = plt.subplots(nrows=2, ncols=2)

# 'r-'其中r表示color=red，-表示linestyle='-'
ax_list[0][0].plot(x, y, 'r-')
ax_list[0][0].title.set_text('sin')

ax_list[0][1].scatter(x, a, s=1) #散点图
ax_list[0][1].title.set_text('scatter')

ax_list[1][0].plot(x, b, 'b-.')
ax_list[1][0].title.set_text('leaky relu')

ax_list[1][1].plot(x, z, 'g')
ax_list[1][1].title.set_text('sigmoid')

fig.subplots_adjust(wspace=0.9, hspace=0.5)
fig.suptitle("Figure graphs", fontsize=16)

plt.show()