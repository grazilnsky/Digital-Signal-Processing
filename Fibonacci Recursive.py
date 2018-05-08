# -*- coding: utf-8 -*-


# Write Fibonacci Recursive

def fibo(n): #return the n-th member of the fibonacci series
    if n<=2 :
        return 1
    else:
        return (fibo(n-1)+fibo(n-2))
        

print(fibo(8))