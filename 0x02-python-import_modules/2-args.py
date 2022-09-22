#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()


commandArg = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    commandArg += 's.'
elif argc == 1:
    commandArg += ':'
else:
    commandArg += 's:'
print(commandArg.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, argument))
    i += 1
