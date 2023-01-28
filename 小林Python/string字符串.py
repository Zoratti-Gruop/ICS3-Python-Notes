
# 在字符串中使用双引号“:
print("Hello\" Mr.allpe") #如果想要在字符串中增加双引号，在此双引号前加上斜线\，以告诉Python此双引号是我们字符串的一部分


#两字符串连接:
print("Hello" + "Mr.apple") #使用+号对两个字符串做连接

#--------------------------------------
#字符串指令：
phrase1 = "Hello Mr.apple"
print(phrase1.lower()) #将字符串全部变成小写

phrase2 = "Hello Mr.apple"
print(phrase2.upper()) #将字符串全部变大写

phrase3 = "Hello Mr.apple"
print(phrase3.isupper()) #检查字符串中是否全为大写, 如果全为大写，将回传True，反之回传False

phrase4 = "Hello Mr.apple"
print(phrase4.islower()) #检查字符串中是否全为小写, 如果全为小写，将回传True，反之回传False

#--------------------------------------------------
#字符串的叠加:
phrase5 = "Hello Mr.apple"
print(phrase5.lower().islower())
#字符串的指令的效果可叠加，将以此按照从左往右运行代码
#这里先将字符串全部变成小写，然后检查字符串是否全为小写，这串代码我们将得到True



#中括号的用法
phrase6 = "Hello Mr.apple"
        #  0123456789     #0为第一位字符，倒数第一位为-1
print(phrase6[1]) #[]内数字代表字符串内字符的位置。这里将打印e

#下面为带冒号的用法，与list中的道理相同，详细请见list文件
print(phrase6[0:5]) #从第一位取到第六位前(0-5),这里取得Hello


# 使用index指数
phrase7 = "Hello Mr.apple"
        #  0123456789
print(phrase7.index("M")) #M为被寻找值。
#用于寻找M所在本字符串的位置，这里是6
#如果字符串中存在多个相同的被寻找值, 将会回传（使用）最前面的一个。


# 使用replace替换
phrase7 = "Hello Mr.apple"
        #  0123456789
print(phrase7.replace("l", "L")) #"l"为被替换值，“L”为替换值。(在字符串中找到小写l后，它将被替换为大写L)。
#replace将会替换字符串中所用的 被指定的 被替换值 ，如果

# 将字串转换为列表：

string1="Python is great"

print("String converted to list :",string1.split())

string2 = "Ask.aQustion"
print(list(string2))

print(list(map(list,string1.split())))

string3 = "abc,efg,hij"
print(string3.split(','))
"""
以上代码的输出结果
String converted to list : ['Python', 'is', 'great']
['A', 's', 'k', '.', 'a', 'Q', 'u', 's', 't', 'i', 'o', 'n']
[['P', 'y', 't', 'h', 'o', 'n'], ['i', 's'], ['g', 'r', 'e', 'a', 't']]
['abc', 'efg', 'hij']
"""



