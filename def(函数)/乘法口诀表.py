def pithy():
    for i in range(1, 10):
        for j in range(1, i + 1):
            """非常多种字符串占位替换方式

            在我这写的这四种占位方式中 推荐指数从上到下 最上面的最推荐
            """
            # print(f"{i}x{j} = {i*j}\t",end = "") # python 3.6后可用
            # print("{}x{}={}\t".format(i, j, i * j), end="") # python 2.6后可用
            # print("%d x %d = %d\t" % (i, j, i * j), end="") # 最早期即可用
            # print(str(i) + "x" + str(j) + "=" + str(i * j) + "\t", end="") # 不推荐使用 纯属扩展

            print("{}x{}={}\t".format(i, j, i * j), end="")
        print("")


pithy()


def create_name(*value):
    for item in value:
        text = f"tell me your name,your name is {item}?"
        print(text)


create_name("chiko", "angle", "xiatian")


# 生成 99 -0
def create_number():
    a = 99
    while a >= 0:
        print(a)
        a -= 1


create_number()
