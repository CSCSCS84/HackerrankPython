#Collection of Challenges in Domain Python->Itertools of Hackerrank

#https://www.hackerrank.com/challenges/itertools-product
import itertools
A=map(int,input().split())
B=map(int,input().split())
AB=list(itertools.product(A,B))
print (" ".join(map(str,AB)))

#https://www.hackerrank.com/challenges/itertools-permutations
from itertools import permutations
S,k=input().split()
print(*[''.join(i) for i in permutations(sorted(S),int(k))],sep='\n')

#https://www.hackerrank.com/challenges/itertools-combinations
from itertools import combinations
S,k=input().split()
S=sorted(S)
for i in range(1,int(k)+1):
    com=combinations(S,int(i))
    print(*[''.join(c) for c in com],sep='\n')

#https://www.hackerrank.com/challenges/itertools-combinations-with-replacement
from itertools import combinations_with_replacement
S,k=input().split()
S=sorted(S)
l=list(combinations_with_replacement(S,int(k)))
print("\n".join([str("".join([b for b in e])) for e in l]))

#https://www.hackerrank.com/challenges/compress-the-string
from itertools import groupby
S=input()

d=groupby(S)

print( " ".join(("("+str(len(list(key)))+", "+str(a)+")") for  a,key in groupby(S)))

#https://www.hackerrank.com/challenges/iterables-and-iterators
import itertools
n=int(input())
numbers=list(map(str,input().split(" ")))
length=int(input())
count=0
countA=0
subsets=list(itertools.combinations(numbers, length))
for s in subsets:
    if "a" in s:
        countA=countA+1
    count=count+1
print(countA/count)

#https://www.hackerrank.com/challenges/maximize-it
K,M=map(int,input().split(" "))
arr=[]
for _ in range(K):
    arr.append(map(lambda x:int(x)**2,input().split(" ")[1:]))
#arr=[(map(int,input().split(" ")[1:]) for _ in xrange(K))]

from itertools import product
print(max([sum(x)%M for x in product(*arr)]))