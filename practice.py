#%%
class MyMath:
    """
    Define MyMath with Class Property x as defined in question
    """
    def __init__(self):
        self.x = 1234567890
    
    # Function to find whether a number passed in 
    # argument is prime or not    
    def checkPrime(self,number):
        # If number is greater than 1 
        if number>1:
            # Loop from 2 to number and check if 
            # the given number is divisible by any 
            # number within this range. If divisible 
            # it is not prime else it is prime.  
            for i in range(2,number):
                # check divisibility by taking remainder 
                # using modulo function 
                if number%i==0:
                    return False
            # Return True if it is not divisible by any  number 
            # in above range
            return True
        else:
            # if number is less than 1 or 1 
            return False
    
    # Function to find Gcd of function using recursion
    def gcd(self,number):
        # define recursive function that finds gcd of two 
        # numbers a and b 
        def recursiveGcd(a,b):
            # if b==0, then return a 
            if b==0:
                return a
            # return b and remainder of a and b
            else:
                return recursiveGcd(b,a%b)
        # Find the gcd of x and argument passed  
        return recursiveGcd(self.x,number)    
    
# Test
m = MyMath()
# Test Prime 
print("check 17 is prime")
print(m.checkPrime(17))
print("check 6 is prime")
print(m.checkPrime(6))

print("\n")

# Test gcd
print("Gcd of x and number 31 = ",m.gcd(31))
print("Gcd of x and number 10 = ",m.gcd(10))
print("Gcd of x and number 6 = ",m.gcd(6))
# %%
import random

"""
Define the class numbers
"""
class Numbers:
    
    def __init__(self):
        pass
    
    # Define iter by initializing the counter object
    def __iter__(self):
        self.counter=0
        return self
    
    # Define next function 
    def __next__(self):
        # Generate a random integer
        randomInt = random.randint(0,100)
        # check counter <= 20 and generated  integer < 90
        # and return the generated Integer
        if self.counter<=20 and randomInt<90:
            self.counter+=1
            return  randomInt
        # If condition fails stop iteration 
        else:
            raise StopIteration

# Test Cases with next function 
number = Numbers()
print("Generating numbers with next function")
i = iter(number)
print(next(i))
print(next(i))
print(next(i))

print("\n")

print("Generating numbers with For loop")
# Test Case with for loop
loop_object = Numbers()
for i in loop_object:
    print(i)        
        
#%%

# %%
