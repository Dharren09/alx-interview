#!/usr/bin/python3
"""scripts that reads stdin line by line and computes the metrics"""

import sys


def compute_metrics(file_size, status):
    """Prints stats"""
    print("File size: {}".format(file_size))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    """Main function"""
    status = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    counter = 0
    file_size = 0
    try:
        for line in sys.stdin:
            if counter == 10:
                compute_metrics(file_size, status)
                counter = 1
            else:
                counter += 1
            line = line.split()
            try:
                file_size += int(line[-1])
            except Exception as e:
                pass
            try:
                for key, value in status.items():
                    if line[-2] == key:
                        status[key] += 1
            except Exception as e:
                pass
        compute_metrics(file_size, status)
    except KeyboardInterrupt as e:
        compute_metrics(file_size, status)
