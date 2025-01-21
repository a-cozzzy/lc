class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # return s == s[::-1]

        n=x
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        return n==rev


            