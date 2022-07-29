import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Table from Ed Smith answer
clust_data = np.random.random((10,3))
collabel=("col 1", "col 2", "col 3")
ax.table(cellText=clust_data,colLabels=collabel,loc='center')
plt.show()

# http://stackoverflow.com/questions/32137396/matplotlib-table-only