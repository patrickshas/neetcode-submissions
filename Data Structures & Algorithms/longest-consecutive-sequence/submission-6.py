class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = sorted(set(nums))
        # print (nums_set)
        counter=0

        for i, n in enumerate(nums_set):

            if n-1 not in nums_set:
                # print("Bingo")
                #TODO start counting
                counter_temp = 1
                if counter < 1:
                    counter = 1
                # print ("here")
                for j in range(i, len(nums_set) -1):
                    # print (list(nums_set)[j]) 
                    # print (list(nums_set)[j+1]) 
                    # print (j)
                    # print ("here")
                    if list(nums_set)[j] + 1 == list(nums_set)[j+1]:
                        counter_temp += 1
                        # print (counter_temp)
                        # print (list(nums_set)[j], list(nums_set)[j+1])
                        if counter_temp > counter:
                            counter = counter_temp
                        continue
                    else:
                        counter_temp = 0
                        # print (list(nums_set)[j], list(nums_set)[j+1])
                        break
                    
                    
        return counter
