from sys import argv, exit
from Upgrade import Upgrade
import os 

if len(argv) < 3:
    exit(1)

x, rootDir, cMakeFile = argv

for dirpath, dirs, files in os.walk(rootDir):	 
	path = dirpath.split('/')
	print '|', (len(path))*'---', '[',os.path.basename(dirpath),']'
	for f in files:
		print '|', len(path)*'---', f
#fileList = []
#for root, dirs, files in os.walk(root_directory):
#    for dir in dirs:
#        for file in os.listdir(os.path.join(root, dir)):
#            if file.endswith(".cpp") or file.endswith(".h") or file.endswith(".cxx"):
#                fileList.append(os.path.join(dir, file))

#for f in fileList:
#    print(f)
#cppUpg = Upgrade([".cpp", ".cxx"], "SET(_other_SOURCES", rootDir, cMakeFile)
#hUpg = Upgrade([".h"], "SET(_moc_HEADERS", rootDir, cMakeFile)
#dirUpg = Upgrade([], "INCLUDE_DIRECTORIES", rootDir, cMakeFile)

#tupleUpg = (cppUpg, hUpg, dirUpg)
#for obj in tupleUpg:
#    obj.upgradeFile()
        
#dirUpg.upgradeFile()