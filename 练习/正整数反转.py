"""正整数反转
   
  单纯利用数字来运算
  
"""

num = int(input("num = "))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
