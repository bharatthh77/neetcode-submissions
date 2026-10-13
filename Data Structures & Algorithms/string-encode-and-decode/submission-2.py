class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            l = len(s)
            res += str(l)
            res += '#'
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []

        i = 0
        while i < len(s):
            c = s[i]
            dig = ''
            while c.isdigit():
                dig += str(c)
                i += 1
                c = s[i]
            i += 1
            # print('dig:', dig)
            # print('i: ', i)
            j = i + int(dig) 
            # print('j: ', j)
            res.append(s[i:j])
            # print('res: ', res)
            i = j
        return res


            





