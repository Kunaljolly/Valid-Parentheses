class Solution:
    def isValid(self, s: str) -> bool:
        t = []
        for x in s:
            f = 0
            if len(t) != 0 and t[-1] == "(" and x == ")":
                f = 1
                t.pop()

            if len(t) != 0 and  t[-1] == "[" and x == "]":
                f = 1
                t.pop()

            if len(t) != 0 and  t[-1] == "{" and x == "}":
                f = 1
                t.pop()
            if f == 0:
                t.append(x)
        if len(t) == 0:
            return True
        return False
