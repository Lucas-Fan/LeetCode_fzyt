class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            y = int(str(x)[::-1])
            return (x==y)
