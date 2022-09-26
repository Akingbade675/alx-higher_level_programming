#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv) - 1
    print("{} {}".format(n, "arguments" if not n == 1 else "argument"), end="")
    print("{}".format(":" if n else "."))
    if n:
        for i in range(1, n + 1):
            print("{}: {}".format(i, argv[i]))
