#-----------------------------------------------------------------------------
# Name:        Functions (functions_ex2.py)
# Purpose:     To provide examples of how for functions work in Python
#              This example uses required parameters.
#              Required in the sense that the caller **must** provide all
#              parameters for the function to work.
#
#为了提供关于for函数在Python中如何工作的例子
#             这个例子使用了必要参数。
#             所谓需要，是指调用者必须提供所有的
#             参数才能使函数工作。

# Author:      Mr. Seidel
# Created:     22-Aug-2018
# Updated:     11-Nov-2018
#-----------------------------------------------------------------------------

# A function with two required parameters一个有两个必要参数的函数
def hypotenuse(sideA, sideB):
	'''
	Calculates the hypotenuse and returns it to the sender based on
	sideA and sideB given
	根据给定的边A和边B，计算斜边并将其返回给发送者
	'''

	cSquare = sideA**2 + sideB**2	# local variable used to hold information用来保存信息的局部变量
	hypotenuseValue = cSquare**0.5 	# takes the square root取平方根
	return hypotenuseValue

# Program runs starting here.  Above this line, the functions are just defined.
hyp = hypotenuse(3, 4)
print(str(hyp))


