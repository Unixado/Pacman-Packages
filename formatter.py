#!/usr/bin/python
import sys
import os

filename = sys.argv[1]
with open (filename) as file_in:
    lines = file_in.readlines()

filename += "Formatted"
if not os.path.exists(filename):
    with open(filename, "w") as file_out:
        for line in lines:
            line = line.rsplit(' ', 1)[0]
            file_out.write(line + " ")
else:
    print("Formatted file already exists")
