import sys
import re

doc = open(sys.argv[1]).read()
out = open(sys.argv[1],'w')

# repl = '<span id=\"_ENREF_1\".*'
repl1 = '.*<textarea id=\"source\">'
repl2 = '</textarea>.*'
# print(repl)
s1 = re.compile(repl1,re.DOTALL)
s2 = re.compile(repl2,re.DOTALL)
tweaked1 = re.sub(s1,'',doc)
tweaked2 = re.sub(s2,'',tweaked1)
tweaked2

out.write(tweaked2)
