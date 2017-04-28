from machine import Pin
from time import sleep

relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(0, Pin.IN)


#Setting initial relay states
relay_1.value(1)
relay_2.value(1)
last_direction = 'up'

# function to drive a motor in one direction (used for testing my circuit)
def up_on():
    try:
        while True:
            last_direction = 'up'
            relay_1.value(0)
            print("Going up")
            read_states()
            sleep(0.5)
    except KeyboardInterrupt:
        relay_1.value(1)

# function to drive motor in the opposite direction (used for testing my circuit)
def down_on():
    try:
        while True:
            last_direction = 'down'
            relay_2.value(0)
            print("Going Down")
            read_states()
            sleep(0.5)
    except KeyboardInterrupt:
        relay_2.value(1)	
        
def up():
    last_direction = 'up'
    relay_1(0)

def down():
    last_direction = 'down'
    relay_2(0)
    
def read_states():
    print("R1 = ", relay_1.value(), " R2 =", relay_2.value())

def all_off():
    relay_1.value(1)
    relay_2.value(1)

# print initial states               
print(read_states())

def run(last_direction):
    # run in the oposite direction
    if last_direction == 'up':
        down()
    else:
        up()
        
def main():
    while True:
        #if button is pressed
        if not button.value():
            #if stopped
            if relay_1.value() == 1 and relay_2.value() == 1:
                run(last_direction)
            else:
                all_off()
        
