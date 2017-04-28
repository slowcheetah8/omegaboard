from machine import Pin
from time import sleep

relay_1 = Pin(12, Pin.OUT)
relay_2 = Pin(13, Pin.OUT)
button = Pin(0, Pin.IN)

#Setting initial relay states
relay_1.value(0)
relay_2.value(0)

# function to drive a motor in one direction (used for testing my circuit)
def up_on():
	try:
		while True:
			relay_1.value(1)
			print("Going up")
			read_states()
			sleep(0.5)
	except KeyboardInterrupt:
		relay_1.value(0)
		
# function to drive motor in the opposite direction (used for testing my circuit)
def down_on():
	try:
		while True:
			relay_2.value(1)
			print("Going Down")
			read_states()
			sleep(0.5)
	except KeyboardInterrupt:
		relay_2.value(0)	
		
def read_states():
	print("R1 = ", R1.value(), " R2 =", R2.value())

def all_off():
    relay_1.value(0)
    relay_2.value(0)

# print initial states               
print(read_states())





	
