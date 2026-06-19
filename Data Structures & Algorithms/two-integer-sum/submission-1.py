class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # print (nums)
        # print (target)

        for indexi,i in enumerate(nums):
            for indexj, j in enumerate(nums):
                if (i+j == target):
                    if indexi!= indexj:
                        return [indexi,indexj]
        