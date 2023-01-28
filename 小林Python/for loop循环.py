"""
for 变量 in 字串 或者 列表:
    要重复执行的代码
    
#假设为列表，它会将列表里的值一一地放入变量里，并重复执行内代码
#假设为字串，它会将字串切成一个个的字源，并一一地放入变量里，重复执行内代码

"""

#例：先将“小”放入name, 然后执行内代码一次。接着同样对“白，你，好”做同样的事情
for name in "小白你好":
    print(name)
    
#例：先将“0”放入num, 然后执行内代码一次。接着同样对“1，2，3, 4”做同样的事情
for num in [0,1,2,3,4]:
    print(num)
    
#__range__
#range是常见的和for loop一起使用的代码
#括号内单值： for i in range(循环次数)
#括号内三值： for i in range(起始循环数，终点循环数(循环将在此值前停下)，每次循环增加/减少值)
#例：
# for i in range(5, 0, -2): 从5到0进行循环，每次循环减少2

#例题：用for loop做和pow(2,6)相同的事情

def power(bace_num, pow_num):  #创建了一个名叫power的函数，需要两个参数。两个参数被命名为bace_num(基数) 和 pow_num（几次方）
    result = base_num    #result是最后要回传的结果，这里同时设定了初始数2，所以我们一开始就有一个2.
    for index in range(pow_num - 1): #设定要循环的次数，如果用户给出6次方，我们就减1. 目的是让它循环5次，因为已经有2，所以只需再乘5次。
        rusult = result * base_num
    return result

print(power(2,6))








