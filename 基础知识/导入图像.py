import os
import urllib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#加州房价数据(大家不用在意域名)
housing = pd.read_csv("http://blog.caiyongji.com/assets/housing.csv")
#加州地图
url = "http://blog.caiyongji.com/assets/california.png"
urllib.request.urlretrieve("http://blog.caiyongji.com/assets/california.png", os.path.join("./", "california.png"))
california_img=mpimg.imread(os.path.join("./", "california.png"))

#根据经纬度绘制房价散点图
ax = housing.plot(kind="scatter", x="longitude", y="latitude", figsize=(10,7),
                       s=housing['population']/100, label="Population",
                       c="median_house_value", cmap=plt.get_cmap("jet"),
                       colorbar=False, alpha=0.4,
                      )
plt.imshow(california_img, extent=[-124.55, -113.80, 32.45, 42.05], alpha=0.5,
           cmap=plt.get_cmap("jet"))
plt.ylabel("Latitude", fontsize=14)
plt.xlabel("Longitude", fontsize=14)

prices = housing["median_house_value"]
tick_values = np.linspace(prices.min(), prices.max(), 11)

#颜色栏，热度地图
cbar = plt.colorbar(ticks=tick_values/prices.max())
cbar.ax.set_yticklabels(["$%dk"%(round(v/1000)) for v in tick_values], fontsize=14)
cbar.set_label('Median House Value', fontsize=16)
plt.legend(fontsize=16)
plt.show()