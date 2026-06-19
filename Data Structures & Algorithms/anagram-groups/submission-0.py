class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str = []
        anogram = []
        dont_itterate = []
        for i in strs:
            sorted_str.append(sorted(i))
        
        for indexi, i in enumerate(sorted_str):
            sub_anogram = []
            sub_anogram.append(strs[indexi])
            if indexi in dont_itterate:
                continue
            for indexj, j in enumerate(sorted_str):
                if i == j:
                    if indexi != indexj:
                        print ("bingo")
                        sub_anogram.append(strs[indexj])
                        dont_itterate.append(indexj) 
            
            anogram.append(sub_anogram)
                    
        return(anogram)
            
                
            
        