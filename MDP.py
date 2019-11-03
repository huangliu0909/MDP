import numpy as np
p = [1/4, 1/2, 1/4]
K = 4
# 有四个状态
s = 3
# 库存量不能多于三个单位
T = 3
# 有三个月，第四个约停止销售
S = [0, 1, 2, 3]
# 状态集合
a_0 = [0, 1, 2, 3]
a_1 = [0, 1, 2]
a_2 = [0, 1]
a_3 = [0]
A = [a_0, a_1, a_2, a_3]
# 决策集合


def c(u):
    # 订购一个单位的商品花费为2
    return 2 * u


def f(u):
    # 需求为u个单位时的收入为8
    return 8 * u


def h(u):
    # 每个单位商品每月库存花费为1
    return u


def F(u):
    # 可向客户供应u个单位商品时的期望收益
    if u == 0:
        return 0
    if u == 1:
        return f(0) * p[0] + f(1) * (p[0] + p[1])
    if u == 2:
        return f(0) * p[0] + f(1) * p[1] + f(2) * p[2]
    if u == 3:
        return f(0) * p[0] + f(1) * p[1] + f(2) * p[2]


def q(u):
    if u == 0:
        return p[0]
    if u == 1:
        return p[0] + p[1]
    if u == 2:
        return p[0] + p[1] + p[2]
    if u == 3:
        return p[0] + p[1] + p[2]
    return 0


def P(i, j, a):
    # 当前为i，新订购a
    # 转移概率
    if j > i + a:
        return 0
    if j > 0:
        return p[i + a - j]
    if j == 0:
        return q(i + a)


def r(i, a):
    # 当前为i，新订购a
    # 期望报酬
    return F(i + a) - c(a) - h(i + a)


d = np.zeros((21, 4))
V = np.zeros((21, 4))
R = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        if i + j < 4:
            R[i, j] = r(i, j)

for t in range(20):
    t = 19 - t
    for s in S:
        pi = np.zeros((1, 4))
        for a in range(0, 3):
            right = 0
            for ss in S:
                if a + s < 4:
                    right = right + P(s, ss, a) * (r(s, a) + V[t+1, ss])
            pi[0, a] = right
        V[t, s] = np.max(R[s, :] + pi[0, :], axis=0)
        d[t, s] = np.argmax(R[s, :] + pi[0, :], axis=0)
print(d)