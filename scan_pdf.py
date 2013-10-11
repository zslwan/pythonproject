import os,os.path
import re

def print_pdf(arg,dirs,files):
    for file in files:
        path = os.path.join(dirs,file)
        path = os.path.normcase(path)
        if not re.search(r".*\.pdf",path):continue
        if re.search(r".\dist",path):continue
        
        print(path)

for root,dirs,files in os.walk('.'):
    print_pdf(root,dirs,files)
