"""
函数的定义：
函数分为两个部分，函数的定义与函数的呼叫。
"""

def hello(): #定义函数
    print("hello")
    
hello()  #呼叫函数

def hello(name, age): #传入参数
    print("hello" + name + "你今年" + age + "岁")
    
hello("小白","87")  #呼叫函数 (注意，数字无法与字串相加，所以这里87我们设为字串)

"""
函数的回传
主要用于对呼叫函数的更多运算，也导致大部分情况将要用到return
"""
#1
def add(num1, num2):
    #print(num1+num2)
    return 10  #当函数中存在return, 它将直接替换掉呼叫函数的值，所以这里会将"add(2,3)"变成”10“

add(2,3)

#2

def add(num1, num2): #呼叫函数将代入定义函数
    #print(num1+num2)
    return num1 + num2  # return的值将直接替换掉呼叫函数的值，这里将得到5

add(2,3)

#3
def add(num1, num2): #1.程式由上往下执行，经过了我们定义的add函数  #3. 程序找到函数
    print(num1+num2)                                            #4. 程序开始执行代码，将打印num1+num2的结果
    return 10                                                   #5. 发现我们return 10， 它将会把呼叫函数替换为10
    #注意，当函数碰到return, 它将不会再运行return下面的所有代码。所以要将return放在最后.

value = add(2,3) #2.发现我们呼叫了add3,4. 程序往上找。          #6. 替换呼叫函数为return的值， 此值被放入变量
print(value)                                                 #7. 打印结果。     *最终将得到7和10的打印结果
#----------------------------------------------------------------------------------------------------------

#类别CLass， 物件Object
#class只是模板，
class phone:#phone 是我们资料形态的名字)#
    #__init__为python的识别初始函数的必要名字#
    #self是这个物件的本身#
    def __init__#name of function#(self, os, number, is _waterproof)#(本身，必要的咨询1，必要的咨询2，必要的咨询3)
    #self以后的东西为手机的资讯（需要提供self后面的三个资讯，！才能！创建我们的手机）
        self.os = os  #这个物件有个属性叫os，它的值=我们传入的os的值
        self.number = number
        self.is_waterproof = us_waterproof
        
phone = phone("ios", 123, True)# 传入值
#类似我打电话给手机工厂老板，我向他提出了我的做手机的需求（系统，号码，防水）。
#老板在__init__这个函数处接到我的订单，老板将我们的三个需求放入实体的手机（self）

print(phone.os)#这个code可以将他的数据单独提取出来。可以用与多个函数
"""
----------------------------------------------------------------------------------
继承函数
继承用于创建两个函数，但是两个函数有大部分重复代码，使用继承可以减少代码的使用
在object后面写（），括号内写入要继承的函数。例如class Student(Person):, 相当于将class Person的内容
复制了一份到class student（）里面的最上面，注意继承者的__init__函数不可删除
#类似父子，儿子拥有父亲的DNA（相同的函数）#

如果在不同文件，做引入from 档案名 import 函数名 或 from 档案名 import *(所有） 


--------------------------------------------------------

"""