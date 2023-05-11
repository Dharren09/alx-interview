#!/usr/bin/python3
""" script that reads a stdin line by line
and computes the metrics"""


import sys


def compute_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]))

    """Initialize the variables to store the metrics"""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0,
                    401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0


try:
    """iterate through the input lines"""
    for line in sys.stdin:
        """split the line into two parts"""
        parts = line.split()
        if len(parts) == 7:
            status_code = int(parts[5])
            file_size = int(parts[6])
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
            """ print the metrics processed 10 times"""
            if line_count % 10 == 0:
                compute_metrics(total_size, status_codes)
            """ Handle the keyboard Interrupt """
            if KeyboardInterrupt:
                compute_metrics(total_size, status_codes)
                sys.exit(0)


except KeyboardInterrupt:
    compute_metrics(total_size, status_codes)
    sys.exit(0)
