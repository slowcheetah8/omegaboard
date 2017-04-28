from machine import Pin
from time import sleep

relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(0, Pin.IN)


#Setting initial relay states
relay_1.value(1)
relay_2.value(1)
last_direction = 'up'

def up():
    global last_direction
    last_direction = 'up'
    relay_1(0)

def down():
    global last_direction
    last_direction = 'down'
    relay_2(0)

def read_states():
    print("R1 = ", relay_1.value(), " R2 =", relay_2.value())

def all_off():
    relay_1.value(1)
    relay_2.value(1)

# print initial states               
print(read_states())

def run():
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
            if relay_1.value() == 0 and relay_2.value() == 0:
                run()
            else:
                all_off()
