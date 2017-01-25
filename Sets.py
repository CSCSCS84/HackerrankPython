#Collection of Challenges in Domain Python->Sets of Hackerrank
#https://www.hackerrank.com/challenges/py-introduction-to-sets
if __name__ == '__main__':
    n = int(input())
    heights=map(int,input().split(" "))
    setOfHeights=set(heights)
    sum=0
    for e in setOfHeights:
        sum=sum+e
    #print(sum)
    print(sum/len(setOfHeights))

#https://www.hackerrank.com/challenges/symmetric-difference
a=input()
firstSet=set(map(int,input().split(" ")))
b=input()
secondSet=set(map(int,input().split(" ")))

s=sorted(firstSet^secondSet)


for e in s:
    print(e)

#https://www.hackerrank.com/challenges/no-idea
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

hapiness = 0
for n in numbers:
    if n in A:
        hapiness += 1
    if n in B:
        hapiness -= 1

print(hapiness)

#https://www.hackerrank.com/challenges/py-set-add
n=int(input())
distinctStamps=set()
for x in range(0,n):
    stamp=input()
    distinctStamps.add(stamp)
print(len(distinctStamps))

#https://www.hackerrank.com/challenges/py-set-discard-remove-pop
n = int(input())
s = set(map(int, input().split()))
numberOfCommands = int(input())
for x in range(0, numberOfCommands):
    line = input().split(" ")
    arguments = line[1:]

    eval("s." + line[0] + "(" + ",".join(arguments) + ")")

print(sum(s))

#https://www.hackerrank.com/challenges/py-set-union
n1= int(input())
a = set(map(int, input().split()))
n2 = int(input())
b= set(map(int, input().split()))
c=a|b
print(len(c))

#https://www.hackerrank.com/challenges/py-set-intersection-operation
n1= int(input())
a = set(map(int, input().split()))
n2 = int(input())
b= set(map(int, input().split()))
c=a&b
print(len(c))

#https://www.hackerrank.com/challenges/py-set-difference-operation
n1= int(input())
a = set(map(int, input().split()))
n2 = int(input())
b= set(map(int, input().split()))
c=a-b
print(len(c))

#https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation
n1= int(input())
a = set(map(int, input().split()))
n2 = int(input())
b= set(map(int, input().split()))
c=a^b
print(len(c))

#https://www.hackerrank.com/challenges/py-set-mutations
input()
A=set(map(int,input().split(" ")))
for _ in range((int)(input())):
    func,x=input().split(" ")
    B=set(map(int,input().split(" ")))
    eval("A."+str(func)+"(B)")
print(sum(A))

#https://www.hackerrank.com/challenges/py-the-captains-room
from collections import Counter
input()
count=Counter(map(int,input().split()))
for e in count:
    if count[e]==1:
        print(e)

#https://www.hackerrank.com/challenges/py-check-subset
for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print(A.issubset(B))

#https://www.hackerrank.com/challenges/py-check-strict-superset

A = set(input().split())
a = True
for _ in range(int(input())):
    B = set(input().split())
    if len(A) == len(B) or not (B.issubset(A)):
        a = False
if a:
    print("True")
else:
    print("False")
