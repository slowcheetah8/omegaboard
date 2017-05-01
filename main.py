from machine import Pin
import time



relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(0, Pin.IN)

#Setting initial relay states to all_off
# the pins are inverted, so: 1 = off and 0 = on
relay_1.value(1)
relay_2.value(1)
last_direction = 'up'

def up():
    global last_direction
    last_direction = 'up'
    #switches relay_1 on
    relay_1(0)
    print("Going up")
    
def down():
    global last_direction
    last_direction = 'down'
    #switches relay_1 on
    relay_2(0)
    print("Going down")
    
def stay():
    relay_1.value(1)
    relay_2.value(1)
    print("Stopped")
    
def read_states():
    print("R1 = ", relay_1.value(), " R2 =", relay_2.value())

# print initial states               
print(read_states())

funcs = (up, stay, down, stay)
index = 0

def main():
    global funcs
    global index
    while True:
        if button.value() ==0:
            if index == 4:
                index = 0
            funcs[index]()
            index += 1
            time.sleep(1)
    

            
                
                
