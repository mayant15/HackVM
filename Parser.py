from typing import List, Tuple


C_NULL       = 0
C_ARITHMETIC = 1
C_PUSH       = 2
C_POP        = 3
C_LABEL      = 4
C_GOTO       = 5
C_IF         = 6
C_FUNCTION   = 7
C_RETURN     = 8
C_CALL       = 9

__keywords = {
    "push": C_PUSH,
    "pop" : C_POP,

    "label"  : C_LABEL,
    "goto"   : C_GOTO,
    "if-goto": C_IF,

    "function": C_FUNCTION,
    "return"  : C_RETURN,
    "call"    : C_CALL,

    "add": C_ARITHMETIC,
    "sub": C_ARITHMETIC,
    "neg": C_ARITHMETIC,
    "eq" : C_ARITHMETIC,
    "gt" : C_ARITHMETIC,
    "lt" : C_ARITHMETIC,
    "and": C_ARITHMETIC,
    "or" : C_ARITHMETIC,
    "not": C_ARITHMETIC
}

def parse_line(line: str) -> Tuple:
    line = line.split('//', 1)[0]
    tokens = line.split()
    print(tokens)
    return __keywords[tokens[0]], tokens
