'''Example Microbit Program
Save this program onto your microbit as 'main.py' and it will run automatically
Ctrl-D to restart the program on the microbit
Ctrl-C to end the program on the microbit
Microbit Micropython API is here: https://microbit-micropython.readthedocs.io/en/v1.0.1/microbit_micropython_api.html

'''

from microbit import *
import audio

print("Hello!")
print("Mirobit program is starting now.")

counter = 1 # initialise the counter

while True:
    if button_a.was_pressed(): # get the next multiple of the thirteen
        counter += 1 # Increase the counter
        #print(f"Button a has been pressed {counter} times") # f strings won't work on the microbit :(
        print('Button a has been pressed ' + str(counter) +' times') # print the counter using string concatenation instead
        display.scroll(str(counter), wait=False, loop=False)
        
    
    if button_b.was_pressed(): # Say Hello
        display.show(Image.HAPPY)
        audio.play(Sound.HAPPY)
        display.clear()
        
    sleep(10) # a 10 millisecond delay
