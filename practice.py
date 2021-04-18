#%%
class MyMath:
    
    def __init__(self):
        self.x = 1234567890
        
    def checkPrime(self,number):
        if number>1:
            for i in range(2,number):
                if number%i==0:
                    return False
            return True
        else:
            return False
    
    def gcd(self,number):
        def recursiveGcd(a,b):
            if b==0:
                return a
            else:
                return recursiveGcd(b,a%b)
        return recursiveGcd(self.x,number)    
    
# Test
m = MyMath()
m.checkPrime(31)    

# %%
