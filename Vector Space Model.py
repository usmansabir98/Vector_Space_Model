from Frequency import Frequency
import numpy as np
import pandas as pd

class VectorSpaceModel():

    def __init__(self, N):
        self.frequency = Frequency()
        self.noOfDocs = N

    def userInterface(self):
        op = '1'
        while(op!='0'):
            print("vector Space Model")
            print("-----------------------------")
            print("1. Execute Query")
            print("0. Exit")

            op = input("Enter input: ")

            self.inputQuery(op)

    def inputQuery(self, op):
        
        if op == '1':
            query = input("Enter query: ")
            queryArr = query.split(" ")
            self.data = self.createTable()
            
            qVector = self.getVector(queryArr)
            docVectors = self.getDocumentVectors()
            
#            print('q= ', qVector)
#            print('docs = ', docVectors)
            
            rankings = self.generateRankings(docVectors, qVector)
            print(self.formatRankings(rankings))
            
        else:
            return
    
    def formatRankings(self, rankings):
        rankings = rankings.loc[rankings['sim']>0.005]
        return rankings.sort_values(by=['sim'], ascending=False)
        
    
    def generateRankings(self, docs, q):
        rankings = pd.DataFrame({
                'docs': [str(x)+'.txt' for x in range(1,self.noOfDocs+1)],
                'sim': [self.sim(docs[i], q) for i in range(1,self.noOfDocs+1)]
                })
        return rankings
        
        
    def sim(self, d, q):
        x = np.array(d)
        y = np.array(q)
        
        modX = sum(x*x)**0.5
        modY = sum(y*y)**0.5
        
        return sum(x*y)/(modX*modY)
            
    def createTable(self):
        self.frequency.loadDocuments()
        self.frequency.buildDictionary()
#        data = pd.DataFrame({
#                'words': self.frequency.getWords(),
#                'idf': self.frequency.getIdf()
#                })
    
        keys = self.frequency.getWords()
        values = self.frequency.getIdf(self.noOfDocs)
    
        data = dict(zip(keys, values))
#        print('data: ', data)
        return data
    
    def getVector(self, array, docId=0):
        vector = []
        
        for word,idf in self.data.items():
            
            if word in array:
                if(docId==0):
                    # docId=0 means getting vector for query
                    tf = self.getQueryFrequency(array)[word]
                else:
                    tf = self.frequency.getTermFrequency(word)[docId]
                    
                vector.append(self.tf_idf(tf, idf))
            else:
                vector.append(0)
        return vector
        
    def getDocumentVectors(self):
        docVectors = {}
        docId = 1
        for i in range(self.noOfDocs):
            doc = self.frequency.collection[i]
            docVectors[docId] = self.getVector(doc, docId)
            docId += 1
        return docVectors
    
    def getQueryFrequency(self, queryArr):
        tf = {}
        for q in queryArr:
            if q not in tf:
                tf[q] = 1
            else:
                tf[q] = tf[q]+1
        return tf
    
    def tf_idf(self, tf, idf):
        return tf*idf

vsm = VectorSpaceModel(50)
vsm.userInterface()
#data = vsm.createTable()
#data = vsm.getDocumentVectors()
#print(vsm.tf_idf('w5', 3))

#data = pd.DataFrame({
#        'words': ['a', 'b', 'c'],
#        'count': [1,2,3]
#        })
#    
#
#print(int(data.loc[data['words']=='b']['count']))