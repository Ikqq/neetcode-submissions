class Solution:
    def encode(self, strs: List[str]) -> str:
        s = []
        if strs == []:
            return ""
        else:
            for ents in strs:
                ent = ents
                if ent == "":
                    s.append("ว")
                else:
                    half = len(ent) // 2
                    for i in range(1):
                        odd = ent[:half]
                        even = ent[half:]
                        ent = ""
                        for j in range(half):
                            ent += (even[j]+odd[j])
                        if len(ent) != len(ents):
                            ent += even[len(even)-1]
                        s.append(ent)
            return "ย".join(s)
                
    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        else:
            s = s.split("ย")
            result = []
            for i in s:  
                if i == "ว" :
                    result.append("")
                else:
                    letter = ""
                    even = i[0::2]
                    odd = i[1::2]
                    letter = odd + even
                    result.append(letter)
            return result
        
            
                       

