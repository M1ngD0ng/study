import numpy as np
import matplotlib.pylab as plt

def sigmoid(x): # 시그모이드=S자 모양 이라는 뜻임 !!!
    return 1/(1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
