# Challenge #6: Sum Square Difference
#
# The sum of the squares of the first ten natural numbers is,
#
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math
import time

time.clock()

number = 100

factorial = math.factorial(number)

nSum = number*(number+1) / 2

sum = 0
for x in range (1, number+1):
    sum += x*x

print ("the sum is " + str(sum))
print ("the sum of all numbers under the number "+ str(number)+" is "+ str(nSum))

print ("The sum square difference is "+ str(nSum*nSum-(sum)))

print ("the run time is "+str(time.clock()))
