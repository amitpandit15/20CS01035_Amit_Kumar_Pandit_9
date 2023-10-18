# script to run the following commands:
# 1. yacc 3ac.y -d
# 2. lex 3ac.l
# 3. gcc y.tab.c
# 4. ./a.out

import os

os.system("yacc 3ac.y -d")
os.system("lex 3ac.l")
os.system("gcc y.tab.c")
os.system("./a.out")