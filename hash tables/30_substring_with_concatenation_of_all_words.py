class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        wordLen = len(words[0]) 
        wordsLen = len(words) 
        winSize = wordLen * wordsLen 

        wordsCntr = Counter(words) 

        winStart = 0 
        matched = 0 
        res = [] 

        # iterate through each element of the array s
        for winEnd in range(len(s)):
            duplicate = False
            tempCntr = wordsCntr.copy() 
            if winEnd >= winSize - 1:
                winArr = s[winStart:winEnd + 1] 
                for i in range(wordLen-1, len(winArr), wordLen): 
                    word = winArr[i-wordLen+1:i+1] 
                    if word in tempCntr: 
                        tempCntr[word] -= 1 
                        if tempCntr[word] == 0: 
                            matched += 1
                        if tempCntr[word] < 0: 
                            duplicate = True
                            break
                if matched == len(tempCntr) and not duplicate: 
                    res.append(winStart)
                matched = 0 
                winStart += 1 
        return res
