#!/usr/bin/python3
from add_0 import add
def main():
    a = 1
    b = 2
    from add_0 import add

    result = add(a, b)
    print("{} + {} = {}".format(a,b,result)

if __name__ == "__main__":
    main()
