#!usr/bin/env python3
import os

os.chdir("D:\MyObject\python_base\读写文件")  # 改变工作目录


# 读取文件
def read_file():
    try:
        # 加个with会自动释放 相当于读取完自动执行了 f.close()
        with open("我的周末.txt", "r", encoding="utf-8") as f:
            print(f.read())
            pass
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("指定了为止的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")


def read_binary():
    try:
        # 读取图片会读出一长串经过加密或编码的二进制数据
        with open("1.jpg", "rb") as fs1:
            data = fs1.read()
            print(type(data))
        with open("chiko.jpg", "wb") as fs2:
            fs2.write(data)  # 将二进制数据重新写入到名为chiko的图片中
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except IOError:
        print("读写文件时出现错误")


if __name__ == "__main__":
    # read_file()
    read_binary()
