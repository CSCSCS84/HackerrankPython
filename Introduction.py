#Collection of Challenges in Domain Python->Introduction of Hackerrank

#https://www.hackerrank.com/challenges/py-hello-world
if __name__ == '__main__':
    print("Hello, World!")

#https://www.hackerrank.com/challenges/python-raw-input
def read():
    s = input()
    return s

#https://www.hackerrank.com/challenges/py-if-else
if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        print("Weird")
    else:
        if n >= 2 and n <= 5:
            print("Not Weird")
        elif n >= 6 and n <= 20:
            print("Weird")
        else:
            print("Not Weird")

#https://www.hackerrank.com/challenges/python-arithmetic-operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print (a+b)
    print (a-b)
    print (a*b)

#https://www.hackerrank.com/challenges/python-division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#https://www.hackerrank.com/challenges/python-loops
if __name__ == '__main__':
    n = int(input())
    for x in range(0,n):
        print(x**2)

#https://www.hackerrank.com/challenges/write-a-function
def is_leap(year):
    leap = False

    if year % 4 == 0:
        if (year % 100 == 0):
            if (year % 400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True

    else:
        leap = False

    return leap

#https://www.hackerrank.com/challenges/python-print
from __future__ import print_function

if __name__ == '__main__':
   print(*range(1, int(input())+1), sep='')