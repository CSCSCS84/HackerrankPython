#Collection of Challenges in Domain Python->Math of Hackerrank

#https://www.hackerrank.com/challenges/polar-coordinates
import cmath
print(*cmath.polar(complex(input())),sep='\n')

#https://www.hackerrank.com/challenges/find-angle
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math
AB=int(raw_input())
BC=int(raw_input())
AC=AB*AB+BC*BC
AC=math.sqrt(AC)

alpha=math.acos(BC/AC)

CM=0.5*AC
x=BC*BC+CM*CM-2*BC*CM*math.cos(alpha)
x=math.sqrt(x)
omega=math.acos((x*x+BC*BC-CM*CM)/(2*x*BC))
omega=180/math.pi * omega
#omega=math.sqrt(omega)

print str(int(round(omega)))+"°"

#https://www.hackerrank.com/challenges/triangle-quest-2
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print (((10**i-1)//9)**2)

#https://www.hackerrank.com/challenges/python-mod-divmod
a=int(input())
b=int(input())
print(a//b)
print(a%b)
print(divmod(a,b))

#https://www.hackerrank.com/challenges/python-power-mod-power
a=int(input())
b=int(input())
m=int(input())
print(pow(a,b))
print(pow(a,b,m))

#https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes
a=int(input())
b=int(input())
c=int(input())
d=int(input())
print(a**b+c**d)

#https://www.hackerrank.com/challenges/python-quest-1
for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print ((10**i-1)//9 *i)




