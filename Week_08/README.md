学习笔记


# 位运算符
    * 按位或   |    0011 | 1011   -->   1011
    * 按位与   &   0011 & 1011    -->  0011
    * 按位取反  ~   0011    -->  1100
    * 按位异或  ^   0011 ^ 1011   -->1000

# 算数移位与逻辑移位
    * 左移  <<    0011 => 0110
    * 右移  >>    0110 => 0011

# 位运算的应用
    1. 将X最右边的n位清零： X & (~0<<n)
    2. 获取X的第n位值(0或者1):   (x>>n) & 1
    3. 获取X的第n位的幂值：      x &(1<<n)
    4. 仅将第n位置为1：    x | (1<<n)
    5. 仅将第n位置为0：    x&(~(1<<n))
    6. 将X最高位至第n位（含）清零：  x&((1<<n)-1)
    
    * 判断基偶
        x%2 == 1   -->(X&1)==1  
        x%2 == 0   -->(X&1)==0
        
    * x>>1    -->x/2
        即x = x/2;  --> x=x>>1
        mid=(left+right)/2; -->mid=(left+right) >>1
    * x = x&(x-1) 清零最低位的1
    * x & -x =>得到最低位的1
    * x & ~x => 0

# 布隆过滤器
    * 一个很长的二进制向量和一系列随机映射函数。
    * 布隆过滤器可以用于检索一个元素是否存在一个集合中
    * 优点： 空间效率和查询时间都远远超过一般的算法
    * 缺点： 有一定的误识别率和删除困难
## 应用
    1. 比特币网络
    2. 分布式系统
    3. Redis缓存
    4. 垃圾邮件， 评论等的过滤

#  排序算法
    1. 比较类排序
        * 通过比较来决定元素间的相对次序， 由于其时间复杂度不能突破O(nlongn), 因此也称为非线性时间比较类排序
        
    2. 非比较类排序
        * 不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下限，以线性时间运行，因此也称为线性时间非比较类排序
        
# 重点需要掌握
    1. 堆排序
    2. 快速排序
    3. 归并排序
        
        
        
## 排序方法
    1. 冒泡排序  嵌套循环， 每次查看相邻的元素如果逆序，则交换
    2. 插入排序  从前到后逐步构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
    3. 选择排序： 每次找到最小值，然后放到待排序数组的起始位置
    
    4. 快速排序： 数组取标杆， 将小元素放pivot左边， 大元素放右侧，然后依次对右边和右边的子数组继续快排，以达到整个序列有序。
    5. 归并排序--分治：
        1. 把长度为N的输入序列分成两个长度为N/2的子序列
        2. 对这两个子序列分别采用归并排序
        3. 将两个排序好的子序列合并成一个最终的排序序列。
    
    6. 堆排序  -- 堆插入O（logN)， 取最大值O（1）
        1. 数组元素一次建立小顶堆
        2. 一次取堆顶元素，并删除。