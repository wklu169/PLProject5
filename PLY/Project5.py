tokens = ('BOOK', 'STATS', 'NAME', 'NUMBERS')
literals = ['.', ':' ]

# Tokens
t_BOOK  = r'BOOK NAME.*'
t_STATS =r'STATISTICS.*'
t_NAME = r'[A-Z][a-z]+|[A-Z][a-z]+\s[A-Z][a-z]+'
t_NUMBERS = r'[0-9]+\schapters,\s[0-9]+\sverses,\s[0-9]+\swords'

# Ignored characters
t_ignore = " \r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
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
    '''start : BOOK
             | STATS
             | NAME
             | NUMBERS
    '''
    print("Saw: ", t[1])

def p_error(t):
    if t == None:
        print("Syntax error at '%s'" % t)
    else:
        print("Syntax error at '%s'" % t.value)

def p_book(t):
    'book : BOOK '
    print('saw book')

def p_header(t):
    'header : BOOK ":" NAME'
    t[0] =  str(t[1]) + str(t[2])
    print(str(t[0]))

def p_data(t):
    'data : STATS ":" NUMBERS'
    t[0] =  str(t[1]) + str(t[2])
    print(str(t[0]))

import ply.yacc as yacc   # ply.yacc comes from the ply folder in the PLY download.
parser = yacc.yacc()

while True:
    try:
        s = raw_input('')
    except EOFError:
        break
    parser.parse(s)

# To run the parser do the following in a terminal window: plyParserInputs/mpstat.out | python Project5.py
