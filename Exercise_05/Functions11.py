from xmlrpc.client import boolean


def divisible(numerator: int, denominator: int)->boolean: 
    return numerator % denominator == 0 

print(divisible(30,7)) 
