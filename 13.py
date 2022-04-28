class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = 0
        pr = 0
        i  =0
        while i != len(s):
            if i != len(s)-1:
                if roman[s[i]]<roman[s[i+1]] and pr == 0:
                    sum += roman[s[i+1]]-roman[s[i]]
                    pr = 1
                    i+=1
                elif pr == 1:
                    pr =0
                    i += 1
                else:
                    sum += roman[s[i]]
                    pr = 0
                    i += 1
                print (i, s[i], sum )
            else:
                if pr != 1:
                    sum+= roman[s[i]]
                i += 1
        return sum