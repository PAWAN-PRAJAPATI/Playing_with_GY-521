"""
ldr.py
Display analog data from Arduino using Python (matplotlib)
Author: Mahesh Venkitachalam
Website: electronut.in
"""

import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque

import matplotlib.pyplot as plt
import matplotlib.animation as animation


# plot class
class AnalogPlot:
    # constr
    def __init__(self, strPort, maxLen):
        # open serial port
        self.ser = serial.Serial(strPort, 9600)

        self.ax = deque([0.0] * maxLen)
        self.ay = deque([0.0] * maxLen)
        self.maxLen = maxLen

    # add to buffer
    def addToBuf(self, buf, val):
        if len(buf) < self.maxLen:
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)

    # add data
    def add(self, data):
        assert (len(data) == 2)
        self.addToBuf(self.ax, data[1])
        self.addToBuf(self.ay, data[2])

    # update plot
    def update(self, frameNum, a0, a1):
        try:
            line = self.ser.readline()
            data = list(line.split(b','))
            print(data)
            # print data
            for i in range(len(data)):
                data[i]=float(data[i])
            if (len(data) == 2):
                self.add(data)
                a0.set_data(range(self.maxLen), self.ax)
                a1.set_data(range(self.maxLen), self.ay)
        except:
            pass
        print(a0)
        return a0,

        # clean up

    def close(self):
        # close serial
        self.ser.flush()
        self.ser.close()

        # main() function


def main():
    # create parser


    # strPort = '/dev/tty.usbserial-A7006Yqh'
    strPort = "/dev/ttyACM0"

    print('reading from serial port %s...' % strPort)

    # plot parameters
    analogPlot = AnalogPlot(strPort, 100)

    print('plotting data...')

    # set up animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, analogPlot.update,
                                   fargs=(a0, a1),
                                   interval=50)

    # show plot
    plt.show()

    # clean up
    analogPlot.close()

    print('exiting.')


# call main
if __name__ == '__main__':
    main()