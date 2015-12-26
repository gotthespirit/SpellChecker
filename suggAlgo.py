# What this module basically does is it takes in a word which is not in the dictionary and finds suitable suggestions for it.
# Made by - Pratik Shastri.

class wrongWord: # Class of wrong word.
    def __init__(self, wWord, fname):# Initializes the various variables used in the class.
        self.wWord = wWord
        self.fname = fname
        self.dictionary = []
        self.lenLst1 = []
        self.lenLst2 = []
        self.wLen = len(wWord)
    def readDict(self): # Reads the text file and stores the words in a list.
        file = open(self.fname, "r+")
        strr = file.read()
        file.close()
        self.dictionary = strr.split()
    def sortLen(self): # Sorts the words in the dictionary into words of length len(wWord), len(wWord) - 1 and len(wWord) + 1
        self.lenLst1 = [token for token in self.dictionary if abs(len(token) - len(self.wWord)) == 1]
        self.lenLst2 = [token for token in self.dictionary if abs(len(token) - len(self.wWord)) == 2]
        self.dictionary = [token for token in self.dictionary if len(token) == len(self.wWord)]
    def suggWords(self): # Generates a list of suggestions sugg based on the wrong word input wWord.
        sugg = [] # List of suggestions.
        wCounter = 0 # Counter for number of suggestions.
        for token in self.dictionary: # Checks for words with same length as wWord, first letter common and which have a common substring of length = len(wWord) - 2.
            if wCounter >= 20: break
            if(token[0] == self.wWord[0]):
                for i in range(2):
                    for j in range(i + 1):
                        if token[j:j+self.wLen-i] in self.wWord:
                            sugg.append(token)
                            wCounter += 1 
                            break
                    else: continue
                    break
        for token in self.dictionary: # Checks for words with same length as wWord and which have a common substring of length = len(wWord) - 2.
            if wCounter >= 20: break
            for i in range(2):
                for j in range(i + 1):
                    if token[j:j+self.wLen-i] in self.wWord and token not in sugg:
                        wCounter += 1
                        sugg.append(token)
                        break
                else: continue
                break
        for token in self.lenLst1: # Checks for words with length differing by 1 from the input.
            if wCounter >= 20: break
            if token in self.wWord or self.wWord in token:
                sugg.append(token)
                wCounter += 1
        for token in self.lenLst2: # Checks for words with length differing by 1 from the input.
            if token in self.wWord or self.wWord in token:
                sugg.append(token)
                wCounter += 1
            if wCounter >= 20: break
        for k in range(5): # Loop contains 4 checks, which are implemented 5 times each with the value of k ranging from 0 to 4. Implements these checks on words of same length as the input.
            for token in self.dictionary: # Checks if the first letter matches and less than k corrosponding letters don't match.
                if wCounter >= 20: break
                if(token[0] == self.wWord[0]):
                    counter = 0
                    for i in range(len(self.wWord)):
                        if(self.wWord[i] == token[i]): counter += 1
                    if self.wLen - counter <= k and token not in sugg:
                        sugg.append(token)
                        wCounter += 1
            for token in self.dictionary: # Checks if less than k corrosponding letters don't match.
                if wCounter >= 20: break
                counter = 0
                for i in range(len(self.wWord)):
                    if(self.wWord[i] == token[i]): counter += 1
                if self.wLen - counter <= k and token not in sugg:
                    sugg.append(token)
                    wCounter += 1
        return sugg
if __name__ == "__main__": # Module specific code for test cases.
    inpt = raw_input() # Reads a word.    
    wW = wrongWord(inpt, "big.txt") # wW object is created of the wrongWord class.
    wW.readDict() # Dictionary file is read.
    wW.sortLen() # Dictionary file is sorted accorting to length of words.
    suggestions = wW.suggWords() # Suggestions list is made.
    print suggestions 
