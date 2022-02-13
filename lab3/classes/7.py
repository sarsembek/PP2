import math
max = 19    #Set it here
max += 1
primes = range(2, max) 
for i in range(2, int( math.ceil(math.sqrt(max)) )): 
    primes = list(filter(lambda x: x == i or x % i, primes))
print(primes)