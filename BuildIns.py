#Collection of Challenges in Domain Python->Built-Ins of Hackerrank

#https://www.hackerrank.com/challenges/zipped

N,X=map(int,input().split())
marks=[]
for i in range(0,X):
    marksOfStudent=(list(map(float,input().split())))
    marks.append(marksOfStudent)
print(*[sum(student)/len(student) for student in zip(*marks)],sep="\n")

#https://www.hackerrank.com/challenges/input
# Enter your code here. Read input from STDIN. Print output to STDOUT
xk = raw_input().split()
x = xk[0]
k = int(xk[1])
line = raw_input()
line = line.replace("x", x)
result = int(eval(line))
if result == k:
    print
    "True"
else:
    print
    "False"

#https://www.hackerrank.com/challenges/python-eval
eval(input())

#https://www.hackerrank.com/challenges/python-sort-sort
from operator import itemgetter

N,M=map(int, input().split(" "))
data=[]
for _ in range(N):
    data.append(list(map(int,input().split())))
K=int(input())
data=sorted(data,key=itemgetter(K))
for i in data:
    print(*i)

#https://www.hackerrank.com/challenges/any-or-all
N=int(input())
numbers=list(map(str,input().split()))
a=all([int(i) >0 for i in numbers])
b=any(([num==num[::-1] for num in numbers]) )
print(all([a,b]))

#https://www.hackerrank.com/challenges/ginorts