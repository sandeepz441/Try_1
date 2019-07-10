import os

curDir = os.getcwd()
print(curDir)

os.mkdir('newDir')

os.rename('newDir','newDir2')

os.rmdir('newDir2')
