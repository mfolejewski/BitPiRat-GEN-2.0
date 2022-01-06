# coding: utf-8

from time import *
import smbus

#tpa6130a2 i2c address 
i2c_addr = 0x2f
bus = smbus.SMBus(1)

print("EMC2301 PWM fan controller simple test 0-100%")

#EMC2301 read register
def EMC2301_read_reg(addr): 
    bus = smbus.SMBus(1)
    data = bus.read_word_data(i2c_addr, addr)
    data = data & 0xff
    return data

#read EMC2301 chip ID

#read manufacturer ID

if (EMC2301_read_reg(0xfe) == 0x5d):
    print("EMC2301 -> Manufacturer ID = Microchip")
else:
    print("EMC2301 not found on the I2C interface")
    exit()

if (EMC2301_read_reg(0xfd) == 0x37):
    print("EMC2301 -> Product ID = EMC2301 IC")
else:
    print("EMC2301 not found on the I2C interface")
    exit()

print("fan speed = 0%")
bus.write_word_data(i2c_addr, 0x30, 0x00)
sleep(3)

print("fan speed = 25%")
bus.write_word_data(i2c_addr, 0x30, 0x40)
sleep(3)

print("fan speed = 50%")
bus.write_word_data(i2c_addr, 0x30, 0x80)
sleep(3)

print("fan speed = 75%")
bus.write_word_data(i2c_addr, 0x30, 0xc0)
sleep(3)

print("fan speed = 100%")
bus.write_word_data(i2c_addr, 0x30, 0xff)
sleep(3)

print("test done! fan speed = 0%")
bus.write_word_data(i2c_addr, 0x30, 0x00)
