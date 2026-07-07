from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n =len(temperatures)
        res = []

        for i in range(n):
            count = 1
            j = i + 1
            while j < n and temperatures[j] <= temperatures[i]:
                count +=1
                j += 1
            if j == n:
                count = 0
            res.append(count)
        return res
            
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, temperature = stack.pop()
                res[index] = i-index
            stack.append((i, temp))
        return res