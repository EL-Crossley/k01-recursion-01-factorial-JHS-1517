# Put your function here
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n>0:
        return n * factorial(n-1)
    else:
        return print("invalidnumber")
        
   
    
# testing
num = int(input())
print(factorial(num))
