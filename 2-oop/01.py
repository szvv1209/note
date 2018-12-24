'''
定义一个学生类，用来描述学生
'''
#定义一个空的类
class Student():
    #一个空的类，pass代表直接跳过
    #此处pass必须有
    pass

#定义一个对象
mingyue = Student()

#再定义一个类，用来描述学习python的学生
class PythonStudent():
    #用None给不确定的值赋值
    name=None
    age=18
    course="python"
    #需要注意
    #1.def dohomework的缩进层级
    #2.系统默认有一个self参数
    def dohomework(self):
        print("在做作业")
        #推荐在函数末尾使用return语句
        return None
#实例化一个叫Lily的学生，是一个具体的人
lily=PythonStudent()
print(lily.name)
print(lily.age)
#注意成员函数的调用没有传递进入参数
lily.dohomework()