class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        trig = False
        while trig == False:
            if (numbers [i] + numbers [j]) > target:
                j -= 1
            elif (numbers [i] + numbers [j]) < target:
                i += 1
            elif (numbers [i] + numbers [j]) == target:
                trig = True
                print (numbers [i], numbers [j])
                print (i, j)
                return [i+1, j+1]
