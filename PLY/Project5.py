tokens = ('BOOK', 'NAME', 'STR', 'THEME', 'BY', 'DATE', 'FOR', 'WHERE', 'STATS', 'CHAPTERS', 'VERSES', 'WORDS', 'MISC', 'INTEGER')
literals = ['.', ':', ',' ]

# Tokens
t_BOOK = r'BOOK'
t_NAME = r'NAME'
t_STR = r'[A-Z][a-z]+.*'
t_THEME = r'^THEME.*$'
t_BY = r'^BY.*$'
t_DATE = r'^DATE.*$'
t_FOR = r'^FOR.*$'
t_WHERE = r'^WHERE.*$'
t_STATS = r'^STATISTICS'
t_CHAPTERS = r'chapters*'
t_VERSES = r'verses'
t_WORDS = r'words'
t_MISC = r'^MISC.*$'

# Ignored characters
t_ignore = " \r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    # print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Build the lexer
import ply.lex as lex   # ply.lex comes from the ply folder in the PLY download.
lexer = lex.lex()

# Parsing rules

global time_step
time_step = 0

def p_start(t):
    '''start : booknum
             | book
             | THEME
             | BY
             | DATE
             | FOR
             | WHERE
             | data
             | MISC
             | empty
    '''
    # print("Saw: ", t[1])

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

def p_booknum(t):
    'booknum : BOOK INTEGER'
    t[0]= str(t[1]) + ' ' + str(t[2])
    print (t[0])

def p_book(t):
    'book : BOOK NAME ":" STR'
    t[0]= str(t[4])
    print (t[0])

def p_data(t):
    'data : STATS ":" INTEGER CHAPTERS "," INTEGER VERSES "," INTEGER WORDS'
    t[0] = str(t[3]) + ' ' + str(t[4]) + ' ' + str(t[6]) + ' ' + str(t[7]) + ' ' + str(t[9]) + ' ' + str(t[10])
    print (t[0])

def p_empty(t):
    'empty : '
    pass

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: cat biblestats.txt | python Project5.py
