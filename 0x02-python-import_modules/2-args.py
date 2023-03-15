#!/usr/bin/python3
import sys

n = len(sys.argv)
if n == 1:
    print("{} arguments.".format(n - 1))
else:
    if n == 2:
        print("{} argument:".format(n - 1))
    else:
        print("{} arguments:".format(n - 1))
for i in range(n):
     if i == 0:
         continue
     print("{}: {}".format(i, sys.argv[i]))
