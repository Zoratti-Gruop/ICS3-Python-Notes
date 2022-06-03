#-----------------------------------------------------------------------------
# Name:        Using microbit class (using microbit class.py)
# Purpose:     This program is an example to demonstrate how to use the Microbit class to interface
#              with a microbit that is running serial output.
#
# Author:      Mr. Brooks-Prenger
# Created:     10-March-2021
# Updated:     3-June-2022
#-----------------------------------------------------------------------------
#--------------------------EXAMPLE CODE TO RUN ON MICROBIT -------------------
# from microbit import *
# import utime
# 
# while True:
#     
#     display.show(Image.HEART)
#     print('heart ', utime.ticks_ms())
#     utime.sleep_ms(15)
# 
#-----------------------------------------------------------------------------
# 
from Microbit import *


def openSingleMicrobit():
    '''Load a single microbit connection'''
    #Create microbit instance
    mb = Microbit()
    
    #Check to make sure it's working
    if not mb.isReady():
        print('Error, Problem Loading Microbit.  Exiting Program')
        return
         
    return mb


    
mb = openSingleMicrobit()

while True:
    
    line = mb.nonBlockingReadLine()
    if line != None:
        print(line)
        
    
    #time.sleep(1)
mb.closeConnection()
