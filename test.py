#%%
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_digits(number):
            x=number
            digits =[]
            while(x>0):
                if x>=10:
                    val=x%10
                    digits.append(val)
                    x=x//10
                else:
                    digits.append(x)
                    x=0
            return digits
        def happy_list(digits):
            return sum(map(lambda x:x**2,digits))
        temp = n
        while True:
            digits = get_digits(temp)
            value = happy_list(digits)
            if value <= 1:
                return True
            elif 1<value<10 and len:
                return False
            else:
                temp = value
s = Solution()
s.isHappy(1111111)