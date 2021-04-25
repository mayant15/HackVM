# Contains translations for sentences

# TODO: Reorganize?

init = """
SETION .data
lcl  db 0
arg  db 0
this db 0
that db 0
temp db 0

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
        push 0
    lt_{}:
        push -1
    """,
}

push = {
    "constant": """
        push {}
    """,

    "local"   : """
        mov eax, lcl
        add eax, {}
        push [eax]
    """,
    
    "argument": """
        mov eax, arg
        add eax, {}
        push [eax]
    """,

    "this": """
        mov eax, this
        add eax, {}
        push [eax]
    """,

    "that": """
        mov eax, that
        add eax, {}
        push [eax]
    """,

    "pointer" : """
        push {}
    """,

    "temp": """
        mov eax, temp
        add eax, {}
        push [eax]
    """,

    "static": "..."
}

pop = {
    "constant": """
        pop eax
    """,

    "local": """
        pop eax
        mov ebx, lcl
        add ebx, {}
        mov [ebx], eax
    """,

    "argument": """
        pop eax
        mov ebx, arg
        add ebx, {}
        mov [ebx], eax
    """,

    "this": """
        pop eax
        mov ebx, this
        add ebx, {}
        mov [ebx], eax
    """,

    "that": """
        pop eax
        mov ebx, that
        add ebx, {}
        mov [ebx], eax
    """,

    "pointer": """
        pop eax
        mov {}, eax
    """,

    "temp": """
        pop eax
        mov ebx, temp
        add ebx, {}
        mov [ebx], eax
    """,

    "static"  : "pop ...n"
}

label = """
{}:
"""

goto = """
jmp {}
"""

if_goto = """
    pop eax
    cmp eax, 0
    jne {}
"""

call = "call"

return_ = "return"