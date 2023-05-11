#!/usr/bin/python3

"""
reads stdin line by line and computes the metrics.
status code should printed in ascending order
"""

import re
import sys


def compute_metrics():
    """possible status codes inserted in a dictionary"""
    status_dict = {"200": 0, "301": 0, "400": 0,
                   "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
    total_file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            match = re.match(
                r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
                r'"GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$',
                line)
            if not match:
                continue

            status_code = match.group(3)

            if status_code in status_dict:
                count += 1
                status_dict[status_code] += 1
                total_file_size += int(match.group(4))

            if count == 10:
                print(f"Total file size: {total_file_size}")
                for key, value in sorted(status_dict.items(),
                                         key=lambda x: x[0]):
                    if value != 0:
                        print(f"{key}: {value}")
            count = 0
    except KeyboardInterrupt:
        print(f"Total file size: {total_file_size}")
        for key, value in sorted(status_dict.items(),
                                 key=lambda x: x[0]):
            if value != 0:
                print(f"{key}: {value}")


if __name__ == "__main__":
    compute_metrics()
