import os 
import time 
import shutil 

src="sample.txt"
dest="classNotes.txt"
rename=os.rename(src,dest)
print('the file is being renamed',rename)