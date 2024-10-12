"""100以内素数

素数指的是只能被1和自身整除的正整数（不包括1）。

"""


# i一定是要大于j的 因为是判断i这个数能否被整除
def prime_number(n):
    for i in range(2, n):
        p = True  # 未被整除
        for j in range(2, i):  # 当j大于等于i时没必要判断
            if i % j == 0:
                p = False  # 如果当前i能被除了1和自身的其他数整除 说明不是水仙花数
                break
        if p:
            print(i)


prime_number(100)
