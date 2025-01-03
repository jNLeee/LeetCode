class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the delimiter
            j = i
            while s[j] != "#":
                j += 1
            
            # Get the length of next string
            length = int(s[i:j])
            
            # Get the actual string
            string = s[j + 1 : j + 1 + length]
            res.append(string)
            
            # Move pointer to start of next length
            i = j + 1 + length
            
        return res