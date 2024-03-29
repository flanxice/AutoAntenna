# -*- coding: utf-8 -*-
# @Time : 21/3/2024 上午 11:28
# @Author : SBP
# @File : Antenna.py
# @Software : PyCharm

import serial

BYTES_0_1 = 0x0014
FCODES = {
    "CHIP_RESET": 0x33,
    "FRONT_INIT": 0x42,
    "FRONT_SELF_CHECK": 0x21,
    "FRONT_POWER_UP_DOWN": 0x36,
    "BEAM_CONTROL": 0x37,
    "LOAD_MODE": 0x37,
    "LODE_FRAME": 0x35,
    "FC_SWITCH_TX_RX": 0xa5,
    "FC_LOCAL_OSCILLATOR": 0xa4,
}

# DEFINE & RESPONSE
ANTENNA_RESET = "0x 00 14 11 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 93 0c "  # 0x11
ANTENNA_INIT = "0x 00 14 42 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 d4 63 "  # 0x42
ANTENNA_SELFTEST = "0x 00 14 21 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 f6 12 "  # 0x21
ANTENNA_RESPONSE_INIT = "0x "


class antenna:
    def __init__(self, com, baud=115200, bytesize=8, stopbits=1, parity="N"):
        self.ser = serial.Serial(port=com, baud=baud, bytesize=bytesize, stopbits=stopbits, parity=parity, timeout=5)
        self.open_ser()  # open ser

    def __make_bytes20__(self, fcode, data1=0x0, data2=0x0, data3=0x0, data4=0x0):
        bytes20 = 0

    def open_ser(self):
        while not self.ser.open():
            self.ser.open()
        print("serial open successfully!")

    def antenna_init(self):
        if self.ser.isOpen():
            self.ser.write(ANTENNA_RESET.encode("utf8"))
            self.ser.write(ANTENNA_INIT.encode("utf8"))
            self.ser.write(ANTENNA_SELFTEST.encode("utf8"))
            while True:
                response = self.ser.readline()
                if response == ANTENNA_RESPONSE_INIT:
                    print("antenna init successfully!")
                    break

    def antenna_change_tx_rx(self):
        pass
