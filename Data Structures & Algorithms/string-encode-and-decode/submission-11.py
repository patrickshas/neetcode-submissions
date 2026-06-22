class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = str()
        for i in strs:
            encoded_string = encoded_string + "~"
            for j in i:
                encoded_string = encoded_string + j
        if strs == []: encoded_string = ""
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_string = []
        stringy = str()
        for index, i in enumerate(s):
            if (i == "~") & (index != 0):
                decoded_string.append(stringy)
                stringy = str()
            elif i != "~":
                stringy = stringy + i
        decoded_string.append(stringy)

        if s == "": decoded_string = [] 

        return decoded_string