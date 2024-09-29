from enum import Enum

# member.value 是自动赋给成员的 int 类型的常量，默认是从 1 开始的
# Enum 的成员均为单例（Singleton），并且不可实例化，不可更改
Month = Enum(
    "Month",
    (
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
)

# # 遍历枚举类型
# for name, member in Month.__members__.items():
#     print(name, member)

# # 直接引用一个常量
# print("\n", Month.Jan)


# 有些时候我们需要控制枚举的类型，我们可以 Enum 派生出自定义类来满足这种需要
@unique  # @unique 装饰器可以帮助我们检查保证没有重复值
class Month2(Enum):
    Jan = "January"
    Feb = "February"
    Mar = "March"
    Apr = "April"
    May = "May"
    Jun = "June"
    Jul = "July"
    Aug = "August"
    Sep = "September "
    Oct = "October"
    Nov = "November"
    Dec = "December"


# 直接引用一个常量
print("\n", Month2.Dec, Month2.Dec.name, Month2.Dec.value)  # Month2.Dec Dec December


# 正常枚举不能使用比较运算符，但是enum.IntEnum可以
class Month3(Enum.IntEnum):
    pass
