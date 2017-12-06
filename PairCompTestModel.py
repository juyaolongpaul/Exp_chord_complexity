# Embedded file name: E:\Python27\PyInstaller-2.1\PairCompTestController\build\PairCompTestController\out00-PYZ.pyz\PairCompTestModel
from random import shuffle
from itertools import permutations
import time
import random
import os
import string

class ExpModel:

    def validateSystems(self):
        pass

    def getExpSeq(self, Random = True):
        self.expSeq = []
        for i in range(5):#len(self.indexListN) * 2):
            stims = [ self.PathSystemFolder + k + os.path.sep + self.pathStims[k][i % 50] for k in self.pathStims.keys() ]
            pairs = list(permutations(stims, 2))
            pairs = [ list(item) for item in pairs ]
            for j in range(len(pairs)):
                pairs[j].append(self.pathRefs[i % 50])

            self.expSeq.append(random.choice(pairs))

        shuffle(self.expSeq)
        return self.expSeq

    def setScore(self, scoreStruct):
        """ The structure of scoreStruct is as following:
        [ ( < whole path of 1st stim>, < whole path of 2nd stim> ), <points of score> ]
        this function will replace 1 with true score
        according to score type """
        tokensA = scoreStruct[0][0].split(os.path.sep)
        tokensB = scoreStruct[0][1].split(os.path.sep)
        nameSysA = tokensA[-1]
        nameSysB = tokensB[-1]
        self.Result.append([nameSysA, nameSysB, scoreStruct[-1]])

    def writeResult(self):
        date = time.strftime('%Y%m%d-%X', time.localtime()).replace(':', '_')
        with open(self.PathResultFolder + self.testerName + '_' + date + '.txt', 'w') as f:
            f.write('# Testday: %s, Name: %s\n' % (date, self.testerName))
            for score in self.Result:
                f.write('%s:%d\n' % (score[1], score[2]))

    def configPath(self, path):
        if not path.endswith(os.path.sep):
            path = path + os.path.sep
        self.PathSystemFolder = path + 'Systems' + os.path.sep
        if not os.path.exists(self.PathSystemFolder):
            pass
        self.PathResultFolder = path + 'Results' + os.path.sep
        if not os.path.exists(self.PathResultFolder):
            pass
        self.pathStims = {}
        with open(path + 'list.txt') as flist:
            self.indexList = [ a.strip() for a in flist.readlines() if a.strip() is not [] ]
            self.indexListN = [ int(n) for n in self.indexList ]
            for p in os.listdir(self.PathSystemFolder):
                self.pathStims[p] = [ 'Chord' + ' ' + a + '.wav' for a in self.indexList ]

        self.PathSystems = [ self.PathSystemFolder + p + os.path.sep for p in os.listdir(self.PathSystemFolder) ]
        self.nameRefSystem = os.listdir(path + 'Ref')[0]
        self.PathRefFolder = os.path.join(path + 'Ref', self.nameRefSystem)
        self.pathRefs = [ os.path.join(self.PathRefFolder, 'Chord' + ' ' + a + '.wav') for a in self.indexList ]
        print 'Path Config Done'

    def __init__(self, ExpPath):
        self.configPath(ExpPath)
        self.testerName = 'ABC'
        self.Result = []


if __name__ == '__main__':
    m = ExpModel(os.path.join(os.path.curdir, 'ExpEnv'))
    expseq = m.getExpSeq()
    print 'Done'