#!/usr/bin/python3
"""
`Module 0-stats`
A script that reads from stdin line by line and computes matrics
"""
import sys
import re

if __name__ == "__main__":
    entry_counter = 0
    cumulative_file = 0
    status_code_counts = {}
    entry_pattern = (
        r"^(\d{1,3}\.){3}\d{1,3}"
        r" - "
        r"\[\d{4}-\d{2}-\d{2}"
        r" \d{2}:\d{2}:\d{2}\.\d+\]"
        r' "GET /projects/260 HTTP/1\.1"'
        r" \d{3}"
        r" \d+$"
    )

    def display_matrics():
        """file size, status code frequence"""
        print("File size: {}".format(cumulative_file))
        for i, j in sorted(status_code_counts.items()):
            print("{}: {}".format(i, j))

    try:
        while True:
            log_entry = sys.stdin.readline()
            if not log_entry:
                break

            if re.match(entry_pattern, log_entry):
                entry_counter += 1
                file_size_match = re.search(r"\d+$", log_entry)
                status_code_match = re.search(r"(\d+)\s+\d+$", log_entry)

                if file_size_match:
                    file_size = file_size_match.group()
                    cumulative_file += int(file_size)

                if status_code_match:
                    status_code = status_code_match.group(1)
                    if status_code in status_code_counts:
                        status_code_counts[status_code] += 1
                    else:
                        status_code_counts[status_code] = 1
                if entry_counter % 10 == 0:
                    display_matrics()
            else:
                continue
    except Exception as err:
        print("Error occurred:", err)
    finally:
        display_matrics()
