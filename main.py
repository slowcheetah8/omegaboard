from machine import Pin, ADC, Timer
import time



relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(2, Pin.IN)
adc = ADC(0)
tim = Timer(-1)

#Setting initial relay states to all_off
# the pins are inverted, so: 1 = off and 0 = on
relay_1.value(1)
relay_2.value(1)
last_direction = 'up'

def up():
    global tim
    global index
    #switches relay_1 on
    relay_1(0)
    print("Going up", index)
        
def down():
    global tim
    global index
    #switches relay_1 on
    relay_2(0)
    print("Going down", index)
    
     
    
def stay():
    relay_1.value(1)
    relay_2.value(1)
    print("Stopped", index)
    
   
    
def read_states():
    print("R1 = ", relay_1.value(), " R2 =", relay_2.value(), "ADC = ", adc.read())

# print initial states               
print(read_states())

funcs = (up, stay, down, stay)
index = 0

def timeout():
    global index
    index = 1
    
def main():
    global funcs
    global index
    while True:
        if button.value() == 0:
            if index == 4:
                index = 0
                    
            funcs[index]()
            tim.init(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:timeout())
            index += 1
            
            time.sleep(1)
            

            
                
                
