#!/usr/bin/python3
for i in range(0, 10):
    for j in range(((i * 10) + (i + 1)), (i * 10) + 10):
        if (j == 89):
	    continue
        print("{:02d}, ".format(j), end="")
print("{:d}".format(j))
