class Solution:
    def reverse(self, x: int) -> int:
        max_v = 2147483647
        mix_v = -2147483648
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -x
            x = -int(str(x)[::-1])
        if mix_v<x<max_v:
            return x
        else:
            return 0
