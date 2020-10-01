#!/usr/bin/python
# -*- coding: utf-8 -*-
class ElementOperator:
    def add(self, num1, num2):
        # 32bits integer max/min
        MAX = 0x7FFFFFFF
        MASK = 0xFFFFFFFF
        ans = num1
        while num2 != 0:
            #相与，再左移一位
            ans = (num1 ^ num2) & MASK
            num2 = ((num1 & num2) << 1) & MASK
            num1 = ans
           # 递归调用前两步，直到进位为0
        return ans if ans <= MAX else ~(ans ^ MASK)

#正数：补码 = 原码 负数：补码 = 反码 + 1 = ~原码 + 1
    def subtract(self, num1, num2):
        mid = self.add(~num2, 1)
        return self.add(num1, mid)

    def is_negative(self, num1, num2):
        return (num1 ^ num2) < 0
    def abs(self, num):
        if num >= 0:
            return num
        else:
            return self.add(~num, 1)

    def multiply(self, num1, num2):
        #将乘数和被乘数都取绝对值　
        abs1 = self.abs(num1)
        abs2 = self.abs(num2)
        # 计算绝对值的乘积　
        ans = 0
        while abs2 != 0:
            if abs2 & 1:
                ans = self.add(ans, abs1)
            abs2 = abs2 >> 1 #每运算一次，乘数要右移一位
            abs1 = abs1 << 1 #每运算一次，被乘数要左移一位　　
        #计算乘积的符号
        if self.is_negative(num1, num2):
            return self.add(~ans, 1)
        return ans

    def divide(self, num1, num2):
        if num2 == 0:
            raise Exception("Divisor is zero.", num2)
        #先取被除数和除数的绝对值
        abs1 = self.abs(num1)
        abs2 = self.abs(num2)
        ans = 0
        i = 31
        while i >= 0:
            #比较abs1是否大于abs2的(1<<i)次方
            if (abs1 >> i) >= abs2:
                ans = self.add(ans, 1 << i)
                abs1 = self.subtract(abs1, abs2 << i)
            i = self.subtract(i, 1)
        #确定商的符号
        if self.is_negative(num1, num2):
            return self.add(~ans, 1)
        return ans

if __name__ == '__main__':
    s = ElementOperator()
    # 用户输入
    print("选择运算：")
    print("1、相加")
    print("2、相减")
    print("3、相乘")
    print("4、相除")

    choice = input("输入你的选择(1/2/3/4):")

    num1 = int(input("输入第一个数字: "))
    num2 = int(input("输入第二个数字: "))

    if choice == '1':
       print(num1, "+", num2, "=", s.add(num1, num2))

    elif choice == '2':
       print(num1, "-", num2, "=", s.subtract(num1, num2))

    elif choice == '3':
       print(num1, "*", num2, "=", s.multiply(num1, num2))

    elif choice == '4':
       print(num1, "/", num2, "=", s.divide(num1, num2))
    else:
       print("非法输入")