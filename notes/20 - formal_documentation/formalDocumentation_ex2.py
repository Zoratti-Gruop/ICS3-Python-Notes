#-----------------------------------------------------------------------------
# Name:        Formal Documentation i.e. docstrings (formalDocumentation_ex2.py)
# Purpose:     Provides an example of how to create docstrings in Python using
#		formal documentation standards.				
#
# Author:      Mr. Seidel
# Created:     22-Aug-2018
# Updated:     04-Nov-2018 (fixed spacing)
#-----------------------------------------------------------------------------

def hypotenuse(sideA, sideB):
  '''
  Calculates the hypotenuse and returns it to the sender based on
  sideA and sideB given
	计算斜边并将其返回给发送者，其依据是
  给出的边A和边B
  Parameters
  ----------
  sideA : float
    One of the arms of the right angle of the triangle
  sideB : float
    The other arm of the right angle of the triangle
	
  Returns
  -------
  float
    The hypotenuse value
  '''

  cSquare = sideA**2 + sideB**2	# local variable used to hold information用来保存信息的局部变量
  hypotenuseValue = cSquare**0.5 	# takes the square root取其平方根
  return float(hypotenuseValue)

# Program runs starting here.  Above this line, the functions are just defined.程序从这里开始运行。 在这一行上面，只是定义了一些函数。
hyp = hypotenuse(3, 4)
print(str(hyp))
