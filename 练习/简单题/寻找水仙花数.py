"""找出所有水仙花数"""

for i in range(100, 1000):
    low = i % 10
    mid = i // 10 % 10
    high = i // 100
    num = low**3 + mid**3 + high**3
    if i == num:
        print(i)
