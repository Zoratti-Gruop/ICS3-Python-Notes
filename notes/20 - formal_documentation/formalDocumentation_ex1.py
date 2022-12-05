#-----------------------------------------------------------------------------
# Name:        Formal Documentation i.e. docstrings (formalDocumentation_ex1.py)
# Purpose:     Provides an example of how to create docstrings in Python using提供了一个例子，说明如何在Python中使用以下方法创建文档字符串
#		formal documentation standards.		正式的文件标准。			
#
# Author:      Mr. Seidel
# Created:     22-Aug-2018
# Updated:     04-Nov-2018 (fixed spacing)
#-----------------------------------------------------------------------------

def menu():
  '''
  A menu of options
	
  This function will print out a list of food options
  available for the user and then return to the caller该函数将打印出一份用户可选择的食物清单，然后返回给调用者。
  并返回给调用者。

  Parameters
  ----------
  None
	
  Returns
  -------
  None
  '''

  print('Menu')
  print('Vegetables')
  print('Fruit')
  return

# Program runs starting here.  Above this line, the functions are just defined.
menu()
