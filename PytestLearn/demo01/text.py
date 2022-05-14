# class Solution:
#     def romanToInt(self, s: str):
#         a = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         res = 0
#         for i in range(len(s)):
#             if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
#                 res -= a[s[i]]
#             else:
#                 res += a[s[i]]
#         print(res)
#
#
# if __name__ == '__main__':
#     Solution().romanToInt("IX")

# class Solution:
#     def isPalindrome(self, x: int):
#         a = str(x)
#         b = a[::-1]
#         if a == b:
#             print(True)
#         else:
#             print(False)
#
#
# if __name__ == '__main__':
#     Solution().isPalindrome(x=1211)
import pytest



