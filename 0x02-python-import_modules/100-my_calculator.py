#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    n = len(argv) - 1
    if n == 3:
        a = int(argv[1])
        b = int(argv[3])
        operator = argv[2]
        if operator not in ["+", "-", "*", "/"]:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        elif operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
