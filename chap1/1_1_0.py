#coding:utf-8

import numpy as np
import matplotlib.pyplot as plt

# 訓練データの数
N = 10

# N個の訓練データを生成
xlist = np.linspace(0, 1, N)     # 0から1の間から均等にN点を抽出

print xlist

print np.random.normal(0, 0.2, xlist.size)


tlist = np.sin(2 * np.pi * xlist) + np.random.normal(0, 0.2, xlist.size)  # sinにN(0, 0.2)の乱数を加える

# オリジナルのsin用データ
xs = np.linspace(0, 1, 1000)    # sinは連続関数なのでxを細かくとる
ideal = np.sin(2 * np.pi * xs)  # xsに対応するsinを求める

# 訓練データとオリジナルのsinデータをプロット
plt.plot(xlist, tlist, 'bo')        # 訓練データを青い（b）の点（o）で描画
plt.plot(xs, ideal, 'g-')           # sin曲線を緑（g）の線（-）で描画
plt.xlim(0.0, 1.0)                  # X軸の範囲
plt.ylim(-1.5, 1.5)                 # Y軸の範囲
plt.show()                          # グラフを表示