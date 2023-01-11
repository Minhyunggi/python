import re

p = re.compile("ca.e")

def print_match(m):
    if m:
        print(m.group())

print_match("care")