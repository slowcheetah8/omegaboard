from machine import Pin
from time import sleep

relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(0, Pin.IN)


#Setting initial relay states
relay_1.value(0)
relay_2.value(0)
last_direction = 'up'

def up():
    global last_direction
    last_direction = 'up'
    relay_1(1)

def down():
    global last_direction
    last_direction = 'down'
    relay_2(1)

def read_states():
    print("R1 = ", relay_1.value(), " R2 =", relay_2.value())

def all_off():
    relay_1.value(0)
    relay_2.value(0)

# print initial states               
print(read_states())

def run():
    # run in the oposite direction
    if last_direction == 'up':
        all_off()
        sleep(1)
        down()
    else:
        all_off()
        sleep(1)
        up()

def main():
    while True:
        #if button is pressed
        if button.value() == 0:
            #if stopped
            if relay_1.value() == 0 and relay_2.value() == 0:
                run()
            elif relay_1.value() == 1 or relay_2.value() == 1:
                all_off()
                
