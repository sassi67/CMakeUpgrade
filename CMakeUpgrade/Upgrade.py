import os
from UpgradeInterface import UpgradeInterface

class Upgrade(UpgradeInterface):
    """Upgrade of .cpp and .cxx files"""
    def __init__(self, extensions, entryPoint, rootDir, fileName):
        return super(Upgrade, self).__init__(extensions, entryPoint, rootDir, fileName)

    def upgradeFile(self):
        result = False

        for dirpath, dirs, files in os.walk(self._rootDir):	 
            for f in files:
                for ext in self._extensions:
                    if f.endswith(ext):
                        s = os.path.join(dirpath, f)
                        s = s[len(self._rootDir) + 1:]
                        self._listFiles.append(s)
        
        result = True
        return result #super(UpgradeCPP, self).upgradeFile()