%pylab inline
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x=linspece(0,5, 20)
fig, ax=plt.subplots(facecolor='w',edgecolor='k')
ax.plot(x, sin(x), marker="o", color="r", linestyle='None')
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.grid(True)
ax.legend(["y=x**2"])
plt.title('puntos')
plt.show()
fig.savefig("grafica.png")
