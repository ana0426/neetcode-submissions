class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        hashmp = {')':'(', '}':'{',']':'['}

        for c in s :
            if c not in hashmp:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    if stk.pop() != hashmp[c]:
                        return False
        return not stk
        