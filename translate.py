import os
import sys
 
prePath = sys.argv[1]
finPath = sys.argv[2]
# read file
def read_file(path):
    lines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            lines.append(line.strip())
    return lines
# write file
def write_file(path, lines):
    with open(path, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '')

lines = read_file(prePath)
write_file(finPath, lines)