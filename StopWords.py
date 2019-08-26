import re

class StopWords():
    def __init__(self, path):
        self.stopWords = []
        with open(path) as f_obj:
            for line in f_obj:
                self.stopWords.append(re.sub('\n', '', line))

    def isStopWord(self, word):
        if word in self.stopWords:
            return True
        return False

    def removeWords(self, string):
        stringArr = string.split(" ")
        outputArr = []
        for word in stringArr:
            if self.isStopWord(word)==False:
                outputArr.append(word)
        return ' '.join(outputArr)
    
    def getStopWords(self):
        return self.stopWords

#sw = StopWords("D:/Information Retrieval/IR/stop words.txt")
#updated = sw.removeWords("i am a painful is by in document had for together have")
#print(sw.getStopWords())
#print(updated)