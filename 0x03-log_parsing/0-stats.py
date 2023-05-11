#!/usr/bin/python3

"""
reads stdin line by line and computes the metrics.
status code should printed in ascending order
"""

import re
import sys


def compute_metrics():
    """defines a dictionary of keys for the possible HTTP status codes"""
    status_dict = {"200": 0, "301": 0, "400": 0,
                   "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    total_file_size = 0
    count = 0
    try:
        """uses a while loop to red stdin indefinately"""
        while True:
            line = sys.stdin.readline()
            if not line:
                break

            st = r'\[(.*?)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
            pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' + st
            
            """each line is matched to a regular expression pattern"""
            match = re.match(pattern, line)
            """if line doesnt match pattern, script skips to next line"""
            if not match:
                continue

            status_code = match.group(3)

            """if status code extracted is not an int. scripts skips to next"""
            if not int(status_code):
                continue

            if status_code in status_dict:
                count += 1
                status_dict[status_code] += 1
                total_file_size += int(match.group(4))
            
            """if count reaches 10, it prints total file size and count
            in ascending order"""
            if count == 10:
                print("Total file size: {}".format(total_file_size))
                sorted_dict = sorted(status_dict.items(),
                                     key=lambda x: x)
                for key, value in sorted_dict:
                    if value != 0:
                        print("{}: {}".format(key, value))
                count = 0
    except KeyboardInterrupt as e:
        sorted_dict = sorted(status_dict.items(),
                             key=lambda x: x)
        for key, value in sorted_dict:
            if value != 0:
                print("{}: {}".format(key, value))
        print(e)


if __name__ == "__main__":
    compute_metrics()
