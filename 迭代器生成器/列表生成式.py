"""列表生成式语法
[expr for iter_var in iterable] 
[expr for iter_var in iterable if cond_expr]
"""

print([f"{i}" for i in range(1, 10)])
# 利用生成式列表生成一个乘法口诀表
print(
    "\n".join(
        [" ".join(f"{i}x{j}={i*j}" for i in range(1, j + 1)) for j in range(1, 10)]
    )
)

print(
    "\n".join(
        [
            " ".join("%dx%d=%2d" % (x, y, x * y) for x in range(1, y + 1))
            for y in range(1, 10)
        ]
    )
)
