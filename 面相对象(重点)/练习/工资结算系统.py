from abc import ABCMeta, abstractmethod

"""工资结算系统

某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""


# 封装员工基类
# getter是不能和属性重名的
class Employee(metaclass=ABCMeta):

    def __init__(self, id, name, nickname):
        self._id = id
        self._name = name
        self._nickname = nickname

    @property  # 通过getter的形式去暴露属性 这就是封装
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter  # nickname可以修改 名字和id不暴露修改方法
    def nickname(self, value):
        self._nickname = value

    @abstractmethod
    def get_salary(self):
        """获得的月薪

        :return: 月薪
        """
        pass


# 部门经理
class Manager(Employee):
    def get_salary(self):
        return 15000.0


# 程序员
class Programmer(Employee):

    def __init__(self, id, name, nickname, working_hour=0):
        super().__init__(id, name, nickname)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, value):
        self._working_hour = value

    def get_salary(self):
        return self._working_hour * 150.0


# 销售员
class Salesman(Employee):

    def __init__(self, id, name, nickname, sales=0):
        super().__init__(id, name, nickname)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, value):
        """三元表达式

        value_if_true if condition else value_if_false

        - condition：这是一个布尔表达式，用于判断条件是否为真。
        - value_if_true：如果条件为真，则返回这个值。
        - value_if_true：如果条件为假，则返回这个值。

        """
        self._sales = value if value > 0 else 0  # 三元表达式

    def get_salary(self):
        return 1200.0 + self._sales * 0.05


# 实例化三种员工

# manger = Manager(1, "陈庆生", "生哥")  # 经理
# print(manger.get_salary())

# programmer = Programmer(2, "尤雨溪", "鱿鱼须", 230)  # 程序员
# print(programmer.get_salary())

# salesman = Salesman(3, "k总", "kk", 500000)  # 销售员
# print(salesman.get_salary())


def main():
    emps = [
        Manager(1, "陈庆生", "生哥"),
        Programmer(2, "尤雨溪", "鱿鱼须"),
        Salesman(3, "k总", "kk"),
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            # 通过setter去设置属性
            emp.working_hour = int(input(f"请输入{emp.name}本月工作时间"))
        elif isinstance(emp, Salesman):
            # 通过setter去设置属性
            emp.sales = float(input(f"请输入{emp.name}本月销售额"))

        print(f"{emp}本月工资为: ￥{emp.get_salary()}元")


if __name__ == "__main__":
    main()
