import os
from sys import exit

class Upgrade(object):
    """ constructor """
    def __init__(self, extensions, entryPoint, rootDir, fileName):
        self._extensions = extensions # a list
        self._entryPoint = entryPoint
        self._rootDir = rootDir
        self._fileName = fileName
        self._listFiles = []

    def upgradeFile(self):
        result = False
        # check the type of the arguments
        if not isinstance(self._extensions, list):
            print "extensions is NOT a dictionary"
            return result
        if not isinstance(self._entryPoint, basestring):
            print "entry point is NOT a string"
            return result
        if not isinstance(self._rootDir, basestring):
            print "root dir is NOT a string"
            return result
        if not isinstance(self._fileName, basestring):
            print "filename is NOT a string"
            return result
        
        # look for the files identified by the list 'extensions'
        self.__getFilesList__(self._rootDir)
                
        
        with open("results.tx" , 'a') as res:
            fileListRel = []
            for f in self._listFiles:
                s = f.replace(self._rootDir + "\\", "")
                fileListRel.append(s)
                res.write(s + '\n')
                
            #print(s)

        #with open(self._fileName, 'r') as f:

        return result

    def __getFilesList__(self, thisDir):
        for root, dirs, files in os.walk(thisDir):
            for file in files:
                if self._extensions:
                    for ext in self._extensions:
                        if file.endswith(ext):
                            tmp = os.path.join(root, file)
                            if not tmp in self._listFiles:
                                self._listFiles.append(os.path.join(root, file))
                else:
                    if file.endswith(".cpp") or file.endswith(".cxx") or file.endswith(".h"):
                        if not root in self._listFiles:
                            self._listFiles.append(root) 
            for dir in dirs:
                print "Enter directory:", os.path.join(root, dir)
                self.__getFilesList__(os.path.join(root, dir))  # recursion!!


