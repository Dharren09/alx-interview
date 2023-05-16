#!/usr/bin/python3
"""method that determines if a given data set represents a
valid UTF-8 encoding"""


def validUTF8(data):
    """initialize the variable to keep track of the number of bytes"""
    numBytes = 0

    """iterate over each byte in the data list"""
    for byte in data:
        if numBytes == 0:
            if byte >> 7 == 0b0:
                numBytes = 0
            elif byte >> 5 == 0b110:
                numBytes = 1
            elif byte >> 4 == 0b1110:
                numBytes = 2
            elif byte >> 3 == 0b11110:
                numBytes = 3
            else:
                return False
        else:
            """continuation byte check"""
            if byte >> 6 != 0b10:
                return False
            numBytes -= 1

    """check if all characters were completed"""
    return numBytes == 0
