class Solution:
    def addBinary(self, a: str, b: str) -> str:
        maxL = max(len(a), len(b))
        C = 0
        res = []

        def sum_bit(A, B, C):
            return (A ^ B) ^ C

        def carry_bit(A, B, C):
            return (A & B) | ((A ^ B) & C)

        for i in range(maxL):
            A = a[-1 - i] & 1 if i < len(a) else 0
            B = b[-1 - i] & 1 if i < len(b) else 0

            res.append(str(sum_bit(A, B, C)))
            C = carry_bit(A, B, C)

        if C: res.append(str(C))

        return "".join(reversed(res))
