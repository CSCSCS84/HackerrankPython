#Collection of Challenges in Domain Python->Strings of Hackerrank

#https://www.hackerrank.com/challenges/swap-case
def swap_case(s):
    answer="".join(a.lower() if a.isupper() else a.upper() for a in s )
    return answer

#https://www.hackerrank.com/challenges/python-string-split-and-join
def split_and_join(line):
    # writ your code here
    line=line.split(" ")
    #print(line)
    string="-".join(line)
    return string

#https://www.hackerrank.com/challenges/whats-your-name
def print_full_name(a, b):
    print("Hello %s %s! You just delved into python." % (a, b))

#https://www.hackerrank.com/challenges/python-mutations
def mutate_string(string, position, character):
    output=string[:position]+character+string[position+1:]
    return output

#https://www.hackerrank.com/challenges/find-a-string
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string) - len(sub_string) + 1):

        if (string[i:(i + len(sub_string))] == sub_string[0:]):
            count = count + 1
    return count

#https://www.hackerrank.com/challenges/string-validators
if __name__ == '__main__':
    s = input()
    if any([c.isalnum() for c in s]):
        print("True")
    else:
        print("False")

    if any([c.isalpha() for c in s]):
        print("True")
    else:
        print("False")

    if any([c.isdigit() for c in s]):
        print("True")
    else:
        print("False")

    if any([c.islower() for c in s]):
        print("True")
    else:
        print("False")

    if any([c.isupper() for c in s]):
        print("True")
    else:
        print("False")

#https://www.hackerrank.com/challenges/text-alignment
#Replace all ______ with rjust, ljust or center.

thickness = int(raw_input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print (c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1)

#Top Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Middle Belt
for i in range((thickness+1)/2):
    print (c*thickness*5).center(thickness*6)

#Bottom Pillars
for i in range(thickness+1):
    print (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6)

#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6)

#https://www.hackerrank.com/challenges/text-wrap
def wrap(string, max_width):
    return textwrap.fill(string,max_width)

#https://www.hackerrank.com/challenges/designer-door-mat
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print("".join("-" for j in range((M-3*i)//2))+"".join((".|.") for j in range(i))+"".join("-" for j in range((M-3*i)//2)))
print("".join("-" for j in range((M-7)//2))+"WELCOME"+"".join("-" for j in range((M-7)//2)))
for i in range(N-2,-1,-2):
     print("".join("-" for j in range((M-3*i)//2))+"".join((".|.") for j in range(i))+"".join("-" for j in range((M-3*i)//2)))

#https://www.hackerrank.com/challenges/python-string-formatting
def print_formatted(number):
    maxBinaryString = len(str((bin(number)))) - 1

    for i in range(1, number + 1):
        decimal = str(i)
        octal = str(oct(i))[2:]
        hexal = str(hex(i)).upper()[2:]
        binary = str(bin(i))[2:]
        print("{:>{width}}".format(decimal, width=maxBinaryString - 1) + "{:>{width}}".format(octal,
                                                                                              width=maxBinaryString) + "{:>{width}}".format(
            hexal, width=maxBinaryString) + "{:>{width}}".format(binary, width=maxBinaryString))


#https://www.hackerrank.com/challenges/alphabet-rangoli
import string
def print_rangoli(size):
    letters=string.ascii_lowercase

    for i in range(size):
        rangoli1="-"*(size*2-(i+1)*2)
        rangoli2="-".join([letters[size-c-1] for c in range(i+1)])
        rangoli3=rangoli2[::-1]
        print(rangoli1+rangoli2+rangoli3[1:]+rangoli1)
    for i in range(size-2,-1,-1):
        rangoli1="-"*(size*2-(i+1)*2)
        rangoli2="-".join([letters[size-c-1] for c in range(i+1)])
        rangoli3=rangoli2[::-1]
        print(rangoli1+rangoli2+rangoli3[1:]+rangoli1)

#https://www.hackerrank.com/challenges/capitalize
def capitalize(string):
    inputString=string.split(" ")
    outputString=" ".join([e[0].upper() + e[1:] if e.strip()!=""  else e for e in inputString ])
    return outputString

#https://www.hackerrank.com/challenges/the-minion-game
def minion_game(string):
    # your code goes here

    scoreStuart = 0
    scoreKevin = 0
    vowel = ["A", "E", "I", "O", "U"]
    for i in range(len(string) + 1):

        first = string[i:i + 1]

        if first in vowel:
            scoreKevin = scoreKevin + len(string) - i

        else:
            scoreStuart = scoreStuart + len(string) - i
    if scoreStuart < scoreKevin:
        print("Kevin " + str(scoreKevin))
    if scoreStuart > scoreKevin:
        print("Stuart " + str(scoreStuart))
    if scoreStuart == scoreKevin:
        print("Draw")

#https://www.hackerrank.com/challenges/merge-the-tools
from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    for i in range(int(len(string) / k)):
        substring = string[k * i:k * (i + 1)]
        dic = OrderedDict.fromkeys(substring)

        print("".join(dic))
