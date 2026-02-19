class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return int(''.join(f'{k:b}' for k in range(n+1)),2)%(10**9+7)
        