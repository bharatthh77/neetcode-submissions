class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # l = 0
        row = 0
        curWidth = 0
        res = []
        curRes = []
        finRes = []

        while row < len(words):
            # print(res)
            # print(words[row])
            if curWidth != 0:
                curWidth += 1
            curWidth += len(words[row])

            if curWidth <= maxWidth:
                curRes.append(words[row])
                row += 1
            else: 
                res.append(curRes)
                curRes = []
                curWidth = 0

        res.append(curRes)
        print(res)

        # curTot = 0
        lenRes = len(res)
        for i, row  in enumerate(res):
            curTot = 0
            if i != lenRes - 1 and len(row) > 1:
                for w in row:
                    curTot += len(w)
                totRemSpace = maxWidth - curTot
                spaceCount = len(row) - 1
                eqSplit = totRemSpace // spaceCount
                rem = totRemSpace % spaceCount
                print('row: ', row)
                print('eqSplit: ', eqSplit)
                print('rem: ', rem)
                for j, wd in enumerate(row):
                    if j == 0:
                        continue
                    elif j >= 1:
                        row[j] = (" " * eqSplit) + wd
                for j, wd in enumerate(row):
                    print('word from in: ', wd)
                    print('rem from in: ', rem)
                    if j > 0 and rem > 0:
                        row[j] = " " + wd
                        rem -= 1
                    
            else:
                for j, wd in enumerate(row): 
                    if j == 0:
                        curTot += len(wd)
                        
                    elif j > 0:
                        row[j] = " " + wd
                        curTot += 1 + len(wd)
                    
                spaceToBeFilled = maxWidth - curTot
                row[-1] = row[-1] + " " * spaceToBeFilled

        print(res)
                
        return [''.join(w) for w in res]
            



            

                
