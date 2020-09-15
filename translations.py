# Contains translations for sentences

# TODO: Reorganize?

init = """
SECTION .text
global _start

_start:
"""

end = """
jmp _end

_end:
    mov ebx, 0
    mov eax, 1
    int 80h
"""

arithmetic = {
    "add": """
        pop eax
        pop ebx
        add eax, ebx
        push eax
    """,

    "sub": """
        pop eax
        pop ebx
        sub ebx, eax
        push ebx
    """,

    "neg": """
        pop eax
        neg eax
        push eax
    """,

    "and": """
        pop eax
        pop ebx
        and eax, ebx
        push eax
    """,

    "or": """
        pop eax
        pop ebx
        or eax, ebx
        push eax
    """,

    "not": """
        pop eax
        not eax
        push eax
    """,

    "eq": """
        pop eax
        pop ebx
        xor eax, ebx
        not eax
        push eax
    """,

    "gt" : """
        pop eax
        pop ebx
        cmp ebx, eax
        jg gt_{}
        push 0
    gt_{}:
        push -1
    """,

    "lt" : """
        pop eax
        pop ebx
        cmp ebx, eax
        jl lt_{}
        push 00h
    lt_{}:
        push FFh
    """,
}

push = {
    "constant": "push {}\n",
    "local"   : "push ...",
    "argument": "push ...",
    "this"    : "push ...",
    "that"    : "push ...",
    "pointer" : "push ...",
    "temp"    : "push ...",
    "static"  : "push ...1"
}

pop = {
    "constant": "pop ...",
    "local"   : "pop ...",
    "argument": "pop ...",
    "this"    : "pop ...",
    "that"    : "pop ...",
    "pointer" : "pop ...",
    "temp"    : "pop ...",
    "static"  : "pop ...n"
}

label = "label"

goto = "goto"

if_goto = "if_goto"

call = "call"

return_ = "return"