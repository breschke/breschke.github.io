
import sys
import re

doc = open(sys.argv[1]).read()

def mdfix(doc):
    docmod = re.sub(r'href="#ref',r'href="post/'+sys.argv[2]+r'#ref',doc)
    #sys.stdout.write(docmod)
    return docmod

out = open(sys.argv[1], "w")
out.write(mdfix(doc))
