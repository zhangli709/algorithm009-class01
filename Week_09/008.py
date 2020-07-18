
# 字符串转换为整数

"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        num = ''

        if not str:
            return 0
        list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        empty_flag = True
        for i in str:
            if i
        if new_str[0] in ['+', '-']:
            num = new_str[0]
        elif new_str[0] in list1:
            num = new_str[0]
        else:
            return 0
        for i in new_str[1:]:
            if i in list1:
                num += i
            else:
                break
        if num == '+' or num == '-':
            return 0
        if int(num) > pow(2, 31) - 1:
            return 2147483647
        elif int(num) < -pow(2, 31):
            return -2147483648
        return int(num)