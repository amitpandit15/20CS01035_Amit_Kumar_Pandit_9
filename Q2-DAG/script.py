# script to run the following commands:
# 1. yacc DAG.y -d
# 2. lex DAG.l
# 3. gcc y.tab.c
# 4. ./a.out

import os

# supress warnings while running the script caused by yacc and lex
os.system("export LC_ALL=C")

os.system("yacc DAG.y -d")
os.system("lex DAG.l")
os.system("gcc y.tab.c")
os.system("./a.out")