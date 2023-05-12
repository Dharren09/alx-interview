#!/usr/bin/python3

"""
reads stdin line by line and computes the metrics.
status code should printed in ascending order
"""

import re
import sys

# a regular xpression to match the input format
regex = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
)

# Initialize variables
total_size = 0
status_codes = {}

# read lines in the stdin
for line in sys.stdin:
    # match the input format
    match = regex.match(line)
    if match:
        # Get the ip addresses, date, status codes and file size
        ip_address = match.group(1)
        date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        # Update the total size with increment
        total_size += file_size

        # Update the status codes dict
        if status_code not in status_codes:
            status_codes[status_code] = 0
        status_codes[status_code] += 1

        # Print the statistics every 10 line
        if status_code % 10 == 0:
            print('File size: {}'.format(total_size))
            for status_code in sorted(status_codes):
                print('{}: {}'. format(status_code, status_codes[status_code]))


# Handle the keyboard interrupts
if sys.stdin.isatty() and input('Press ENTER to continue...') == '':
    sys.exit(0)
