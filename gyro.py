import smbus
import math
 
# Register
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c
 
def read_byte(reg):
    return bus.read_byte_data(address, reg)
 
def read_word(reg):
    h = bus.read_byte_data(address, reg)
    l = bus.read_byte_data(address, reg+1)
    value = (h << 8) + l
    return value
 
def read_word_2c(reg):
    val = read_word(reg)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
 
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
 
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
 
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
 
bus = smbus.SMBus(1) # bus = smbus.SMBus(0) fuer Revision 1
address = 0x68       # via i2cdetect
 
# Aktivieren, um das Modul ansprechen zu koennen
bus.write_byte_data(address, power_mgmt_1, 0)
f = open("testdata.txt", "w")
while (True): 
	beschleunigung_xout = read_word_2c(0x3b)
	beschleunigung_yout = read_word_2c(0x3d)
	beschleunigung_zout = read_word_2c(0x3f)
 
	beschleunigung_xout_skaliert = beschleunigung_xout / 16384.0
	beschleunigung_yout_skaliert = beschleunigung_yout / 16384.0
	beschleunigung_zout_skaliert = beschleunigung_zout / 16384.0
 
	f.write(str(beschleunigung_xout_skaliert) + " " + str(beschleunigung_yout_skaliert) + " " + str(beschleunigung_zout_skaliert) + "\n")
