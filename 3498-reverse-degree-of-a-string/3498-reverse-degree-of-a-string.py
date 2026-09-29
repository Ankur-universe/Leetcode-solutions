class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for i, ch in enumerate(s):
            reverse_pos = ord('z') - ord(ch) + 1
            total += reverse_pos * (i + 1)

        return total