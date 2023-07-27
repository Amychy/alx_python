#!/usr/bin/python3

if __name__ == "__main__":
    """Print number and list of arguments"""
    import sys

    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(i, sys.argv[i]))
