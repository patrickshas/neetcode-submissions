class Solution:
    def isPalindrome(self, s: str) -> bool:
        print (s[0])
        s_reversed = reversed(s)
        s_clean = ''.join(filter(str.isalnum, s))
        s_reversed_clean = ''.join(filter(str.isalnum, s_reversed))
        print (s_clean)
        print (s_reversed_clean)

        for i in range (len(s_clean)):
            if s_clean[i].lower() == s_reversed_clean[i].lower():
                continue
            else:
                return False
        return True
