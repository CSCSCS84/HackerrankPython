#Collection of Challenges in Domain Python->Collections of Hackerrank

#https://www.hackerrank.com/challenges/collections-counter
from collections import Counter

X = int(input())
sizes =input().split()
counter=Counter(sizes)
n = int(input())
moneyEarned=0

for i in range(1,n+1):
    size,price=input().split()
    #print(size + " "+price)
    if int(counter[size]) > 0 :
         moneyEarned=moneyEarned+int(price)
    #print(moneyEarned)
    counter[size]=counter[size]-1
print(moneyEarned)

#https://www.hackerrank.com/challenges/defaultdict-tutorial
from collections import defaultdict
from collections import Counter

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(0, n):
    d['A'].append(input())
counter = Counter(d['A'])
string = ""
for i in range(0, m):
    b = input()
    if not (b in d['A']):
        string = string + "-1"
    else:
        for j in range(0, n):
            if (d['A'][j] == b):
                string = string + "" + str(j + 1) + " "
    string = string + "\n"
print(string)

#https://www.hackerrank.com/challenges/py-collections-namedtuple
from collections import namedtuple

n = int(input())

fields = ",".join(input().split(' '))
Student = namedtuple('student', fields)
sumMarks = 0
for i in range(0, n):
    studentInput = list(input().split())
    stud = Student(*studentInput)
    sumMarks += int(stud.MARKS)
print(sumMarks / n)

#https://www.hackerrank.com/challenges/py-collections-ordereddict
from collections import OrderedDict

n=int(input())
boughtItems= OrderedDict()
for i in range(0,n):
    item=input().split()
    price=int(item[len(item)-1])
    itemName=" ".join(i for i in item[0:len(item)-1])
    if itemName in boughtItems:
        boughtItems[itemName]+=price
    else:
        boughtItems[itemName]=price

for itemName, sumPrice in boughtItems.items():
    print(itemName,sumPrice)

#https://www.hackerrank.com/challenges/word-order
from collections import OrderedDict

words = OrderedDict()
n = int(input())
for _ in range(n):
    word = input()
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1

print(len(words))
print(" ".join([str(value) for key, value in words.items()]))

#https://www.hackerrank.com/challenges/py-collections-deque
from collections import deque
d=deque()
for _ in range(int(input())):
    fun=input().split()
    if(len(fun)==2):
        element=fun[1]
        eval("d."+str(fun[0])+"("+element+")")
    if(len(fun)==1):
        eval("d."+str(fun[0])+"()")
print(" ".join(str(e) for e in d ))

#https://www.hackerrank.com/challenges/piling-up
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    leftIndex = 0
    rightIndex = n - 1
    currentCube = 0
    if (cubes[leftIndex] < cubes[rightIndex]):
        currentCube = cubes[rightIndex]
        rightIndex = rightIndex - 1
    else:
        currentCube = cubes[leftIndex]
        leftIndex = leftIndex + 1
    while leftIndex <= rightIndex:
        if (cubes[leftIndex] < cubes[rightIndex]):
            if cubes[rightIndex] <= currentCube:
                currentCube = cubes[rightIndex]
                rightIndex = rightIndex - 1
            else:
                print("No")
                rightIndex = leftIndex - 2
        else:
            if cubes[leftIndex] <= currentCube:
                currentCube = cubes[leftIndex]
                leftIndex = leftIndex + 1
            else:
                print("No")
                rightIndex = leftIndex - 2
    if rightIndex != leftIndex - 2:
        print("Yes")

#https://www.hackerrank.com/challenges/most-commons
from collections import Counter
inp=input()

#sol= collections.Counter(inp).most_common(3)
counter = Counter(inp)
most_common = sorted(counter.items(), key=lambda pair: (-pair[1], pair[0]))
print(*most_common[0])
print(*most_common[1])
print(*most_common[2])