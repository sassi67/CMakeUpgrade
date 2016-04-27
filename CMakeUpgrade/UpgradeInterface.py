import abc
import os

from sys import exit

class UpgradeInterface(object):
    """Base class for common operation of upgrade"""
    __metaclass__ = abc.ABCMeta

    def __init__(self, extensions, entryPoint, rootDir, fileName):
        self._extensions = extensions # a list
        self._entryPoint = entryPoint
        self._rootDir = rootDir
        self._fileName = fileName
        self._listFiles = []
        # check the type of the arguments
        if not isinstance(self._extensions, list):
            print "extensions is NOT a dictionary"
            exit(1)
        if not isinstance(self._entryPoint, basestring):
            print "entry point is NOT a string"
            exit(1)
        if not isinstance(self._rootDir, basestring):
            print "root dir is NOT a string"
            exit(1)
        if not isinstance(self._fileName, basestring):
            print "filename is NOT a string"
            exit(1)
    
    @abc.abstractmethod
    def upgradeFile(self):
         pass

    def showList(self):
        for f in self._listFiles:
            print f
        print "Number of objects:", len(self._listFiles)
