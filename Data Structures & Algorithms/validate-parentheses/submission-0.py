class Solution:
    def isValid(self, s: str) -> bool:
        # some sort of search using stack.
        # start reading from the beginning and look for the matching item down the list.
        # if it exists then good and delete both and start again
        # if not false
        # if all the above is good then true
        
        # define the couples (dict??)
        
        stack = []
        closeOpen = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in closeOpen:
                if stack and stack [-1] == closeOpen [i]:
                    stack.pop()
                else:
                    return False
            else:
                    stack.append(i)

        return True if not stack else False

            # for k,l in enumerate(s, start=2):
                # if   