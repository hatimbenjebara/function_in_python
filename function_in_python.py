import numpy as np
#function
def name(first_name, last_name): #parameters
    print(first_name + " " + last_name)
name("hatim","benjebara") # arguments
def familly_age(*age):
    print("the youngest one have is :" + str(np.min(age)))
familly_age(35, 29, 37, 39)
def tri_recusion(k):
    if (k>0):
        result = k +tri_recusion(k-1)
        print(result)
    else:
        result = 0
    return result
print("recursion example results: \n")
tri_recusion(10)
def factorization(n):
    a=n
    factor = []
    divisor = 2
    while n>1:
        while n % divisor == 0: 
            factor.append(divisor)
            n //= divisor
        divisor +=1
    print(f"factorization of {a} is :", factor)
factorization(144)
x = lambda a: a+10
print(x(10))
x = lambda a,b : a*b
print(x(5,6))