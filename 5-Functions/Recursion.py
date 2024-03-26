#Simple recursive algorithmn
#return returns a value to the caller
#the caller is the function or method in this case (factorial)


def factorial(n):
    print(n)
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(4))

# n * factorial(n-1) calls the function within the function
# eventually returning 0 which returns 1
# then 1*1*2*3*4
