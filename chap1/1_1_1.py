#coding:utf-8


import sys

import numpy as np
import matplotlib.pyplot as plt


# M次多項式近似
M =6
def y(x, wlist):
    ret = wlist[0]
    for i in range(1, M+1):
        ret += wlist[i] * (x ** i)
    return ret


# 訓練データからパラメータを推定
def estimate(xlist, tlist):
    #(1.123)のAij式
    A = np.zeros((M+1, M+1))
    for i in range(M + 1):
        for j in range(M + 1):
            A[i,j]=(xlist**(i+j)).sum()
    print A

    # (1.123)のTi式
    T = np.array([((xlist**i) * tlist).sum() for i in xrange(M + 1)])

    # パラメータwは線形連立方程式の解
    wlist = np.linalg.solve(A, T)
    return wlist

def example1():
    # 訓練データ
    # sin(2*pi*x)の関数値にガウス分布に従う小さなランダムノイズを加える
    xlist = np.linspace(0, 2.5, 20)
    tlist = np.sin(2*np.pi*xlist) + np.random.normal(0, 0.2, xlist.size)
    # 訓練データからパラメータを推定
    wlist = estimate(xlist, tlist)
    print (wlist)
    # 連続関数のプロット用X値
    xs = np.linspace(0, 2.5, 500)
    ideal = np.sin(2*np.pi*xs)         # 理想曲線
    model = [y(x, wlist) for x in xs]  # 推定モデル
    plt.plot(xlist, tlist, 'bo')  # 訓練データ
    plt.plot(xs, ideal, 'g-')     # 理想曲線
    plt.plot(xs, model, 'r-')     # 推定モデル
    plt.xlim(0.0, 1.0)
    plt.ylim(-1.5, 1.5)
    plt.show()

if __name__ == "__main__":
    example1()