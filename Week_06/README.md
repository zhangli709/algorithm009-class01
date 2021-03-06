学习笔记

# 动态规划的实现及关键点
* 动态递归， 将一个复杂的问题，分解为简单的子问题。  分治+最优子结构

* 关键点：
    1. 动态规划和递归或者分治， 没有根本上的区别，关键看有无最优的子结构
    2. 共性：找到重复子问题
    3. 差异性：最优子结构，中途可以淘汰次优解。

## 动态规划
    1. 动态规划方程
    2. 状态转移方程
    3. dp方程

## 动态规划关键点
    1. 最优子结构 opt[n] = best_of(opt[n-1],opt[n-2],...)
    2. 存储中间状态： opt[i]
    3. 递推公式（美其名曰：状态转移方程或者DP方程）
        Fib:opt[i] = opt[n-1] + opt[n-2]
        二维路劲： opt[i,j] = opt[i+1][j] + opt[i][j+1] 且判断a[i,j]是否空地