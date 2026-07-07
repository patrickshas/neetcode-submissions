class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area_holder = 0
        length = 0
        area = 0
        for i, n in enumerate(heights):
            for j, m in enumerate(heights):
                if n > m:
                    length = m
                else:
                    length = n

                area_holder = (abs(j-i)) * length 

                if area < area_holder:
                    area = area_holder

        return area    
        