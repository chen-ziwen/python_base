#!usr/bin/env python3
def main():
    try:
        # 加个with会自动释放
        with open("我的周末.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件！")
    except LookupError:
        print("指定了为止的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")


if __name__ == "__main__":
    main()
