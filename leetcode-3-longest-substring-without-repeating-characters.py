class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0 

        for i in range(len(s)):
            charSet = set()
            for j in range(i, len(s)):
                if s[j] in charSet:
                    break
                charSet.add(s[j])
                count = max(count, len(charSet))
        return count
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        count = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            count = max(count, r - l + 1)
        return count
    
