

# 2的幂

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        i = 0
        while True:
            if pow(2, i) < n:
                i += 1
            elif pow(2, i) == n:
                return True
            else:
                return False 