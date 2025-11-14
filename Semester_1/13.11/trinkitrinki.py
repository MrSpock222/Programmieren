from time import *

def sieb(n):
    start = perf_counter()
    prime= []
    number = list(range(2,n))
    
    k = 2
    while k**2 < n:
        for i in range(k,n,k):
            if i in number:
                number.remove(i)
        prime.append(k)
        k =number[0]
    stop = perf_counter()
    zeit = stop - start
    return prime + number, zeit
    

def brute(n):
    start = perf_counter()
    prime = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(i)
    stop = perf_counter()
    zeit = stop-start
    return prime, zeit

def siebneu(n):
    
    start = perf_counter()
    primes = [ ]
    sieb = [True]*(n+1)
    sieb[0] = sieb[1] = False

    p = 2
    while p ** 2 <= n:
        if sieb[p]:
            i = p
            while p * i <= n:
                sieb[p*i] = False
                i+=1

        p+=1
    k = 2
    while k <= n:
        if sieb[k]:
            primes.append (k)
        k+=1
    end = perf_counter()
    time = end-start
    return primes, time

