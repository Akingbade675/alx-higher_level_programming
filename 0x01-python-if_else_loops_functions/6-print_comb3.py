#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if i < j:
            if (i * 10 + j) == 89:
                print("{:02d}".format(i * 10 + j))
            else:
                print("{:02d}".format(i * 10 + j), end=", ")
