#Collection of Challenges in Domain Python->Basic Data Types of Hackerrank

#https://www.hackerrank.com/challenges/python-lists
if __name__ == '__main__':
    list = []

    N = int(input())
    # print(N)
    for i in range(1, N + 1):
        # eval(s[i])
        # print(i)
        s = input().split()
        command = s[0]
        arguments = s[1:]
        if command != "print":
            argumentsAsString = ",".join(arguments)
            eval("list." + command + "(" + argumentsAsString + ")")
            # list.insert(0,3)
            # print(argumentsAsString)
        else:
            eval("print(list)")


#https://www.hackerrank.com/challenges/python-tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    inputTuple=tuple(integer_list)
    hashValue=hash(inputTuple)
    print(hashValue)

#https://www.hackerrank.com/challenges/list-comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    output=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c !=n]
    print(output)

#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
if __name__ == '__main__':
    n = int(input())

    arr = map(int, input().split())
    numbers = tuple(arr)
    largestNumber = numbers[0]
    secondLargest = -100
    for number in numbers:
        if (number > largestNumber):
            secondLargest = largestNumber
            largestNumber = number
        if (secondLargest < number < largestNumber):
            secondLargest = number

    print(secondLargest)

#https://www.hackerrank.com/challenges/nested-list
import operator;

if __name__ == '__main__':
    nestedList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nestedList.append([name, score])

    sortedList = sorted(nestedList, key=operator.itemgetter(1))
    # print(sortedList)
    lowest = sortedList[0][1]

    while lowest == sortedList[0][1]:
        sortedList.pop(0)
    # print(sortedList)
    secondLowest = sortedList[0][1]
    # print(secondLowest)
    listSecondLowest = []
    for e in sortedList:
        if (e[1] == secondLowest):
            listSecondLowest.append(e[0])

    # print(sorted(listSecondLowest))

    print("\n".join(a for a in sorted(listSecondLowest)))

#https://www.hackerrank.com/challenges/finding-the-percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    score = student_marks[query_name]
    scoreAverage = (sum(score)) / 3
    print("%.2f" % scoreAverage)