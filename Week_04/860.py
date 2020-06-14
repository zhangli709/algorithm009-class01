
# 柠檬水找零

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        i5 = 0
        i10 = 0
        for i in bills:
            if i == 5:
                i5 += 1
            elif i == 10:
                i5 -= 1
                i10 += 1
            else:
                if i10 == 0:
                    i5 -= 3
                else:
                    i5 -= 1
                    i10 -= 1
            if i5 <0 or i10 <0:
                return False
        return True