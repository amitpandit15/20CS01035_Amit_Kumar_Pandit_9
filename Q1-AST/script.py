# script to run the following commands:
# 1. yacc AST.y -d
# 2. lex AST.l
# 3. gcc y.tab.c
# 4. ./a.out

import os

os.system("yacc AST.y -d")
os.system("lex AST.l")
os.system("gcc y.tab.c")
os.system("./a.out")