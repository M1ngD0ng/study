import numpy as np
import matplotlib.pylab as plt


def step_function(x):  # 계단 함수 구현에서 사용한 넘파이의 트릭
    return np.array(x > 0, dtype=np.int)


x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
