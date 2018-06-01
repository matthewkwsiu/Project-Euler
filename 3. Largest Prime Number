# challenge #3: Largest Prime Factor

import math

# public variables

greatestPrime = 0
total = 600851475143
loop= 1

# this function checks if the number is a prime number
def primeCheck(number):
    i = 2
    # set prime to 1 to set it as true
    prime = 1
    while i < number:
        if (number/i) % 1 == 0:
            prime = 0
        i += 1
    return prime


while loop < total:
    #print(loop)
    if (total / loop) % 1 == 0:
        print ("this  is a factor"+str(loop))
        if primeCheck(loop) == 1:
            print("this  is a PRIME factor" + str(loop))
            greatestPrime == loop

    loop += 1

print (greatestPrime)


