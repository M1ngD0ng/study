import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        print(0)
        return 0
    elif tmp > 0:
        print(1)
        return 1


def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        print(0)
        return 0
    elif tmp > 0:
        print(1)
        return 1


def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(w*x)+b
  if tmp <= 0:
      print(0)
      return 0
  elif tmp > 0:
      print(1)
      return 1





def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    print('XOR: ',y)


XOR(0, 0)
XOR(0, 1)
XOR(1, 0)
XOR(1, 1)
