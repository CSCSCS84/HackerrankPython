#Collection of Challenges in Domain Python->Errors and Exceptions of Hackerrank

#https://www.hackerrank.com/challenges/exceptions
t = int(input())
for i in range(0, t):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code: " + str(e))


#https://www.hackerrank.com/challenges/incorrect-regex
import re
for _ in range(int(input())):
    reg=input()
    try:
        re.compile(reg)
        isValid=True
    except re.error:
        isValid=False
    print(isValid)