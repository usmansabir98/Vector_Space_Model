import re
import math
from StopWords import StopWords

class Frequency():
    def __init__(self):
        self.collection = [
            ['w1','w2','w4','w6'],
            ['w1','w2','w7','w3'],
            ['w8', 'w5', 'w4', 'w5', 'w6']
        ]
        self.dictionary = {}
        self.stopWords = StopWords("D:/Information Retrieval/Assignment 2/stop words.txt")
        

    def loadDocuments(self):
        self.collection = []
        for i in range(1, 51):
            filename = "D:/Information Retrieval/Assignment 2/ShortStories/"+str(i)+".txt"
            s = ""
            with open(filename) as f_obj:
                for line in f_obj:
                    if(line != '\n'):
                        l = re.sub('[^a-zA-Z0-9\s]|[\n]', '', line)
                        l = self.stopWords.removeWords(l.lower())
                        s = s + l.lower() + " "
#                        print(l.lower())
            lines = s.split(" ")
            self.collection.append(lines)

    def buildDictionary(self):
        for i in range(0 ,len(self.collection)):
            array = self.collection[i]

            for j in range(0,len(array)):
                if(array[j] not in self.dictionary):
                    docId = i+1
                    d = {docId:1}
                    self.dictionary[array[j]] = d
                else:
                    d = self.dictionary[array[j]]

                    if (i+1) in d:
                        l = d[i+1]
                        l = l +1
                        d[i+1] = l
                        
                    else:
                        docId = i+1
                        d[docId] = 1
                    
                    self.dictionary[array[j]] = d

    def getTermFrequency(self, key):
        if key not in self.dictionary:
            return []
        return self.dictionary.get(key)
    
    def getDocumentFrequency(self, key):
        if key not in self.dictionary:
            return []
        return list(self.dictionary.get(key).keys())
    
    def getWords(self):
        return list(self.dictionary.keys())
    
    def getIdf(self, N):
        words = self.getWords()
        idf = [math.log10(N/len(self.getDocumentFrequency(x))) for x in words]
        return idf
    
    

#pi = Frequency()
##pi.loadDocuments()
#pi.buildDictionary()
#print(pi.getWords())
#print(pi.getIdf())
#print(pi.getTermFrequency('w1'))
