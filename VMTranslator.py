import sys
import os

from typing import List
from Writer import Writer
from Parser import *


def main(argv: List[str]) -> None:
    if len(argv) != 2:
        print('Wrong number of arguments.')
        return

    writer = None
    path = argv[1]
    files = []
    if os.path.isfile(path):
        files.append(path)
        name = os.path.basename(path).split('.')[0] + '.asm'
        writer = Writer(os.path.join(os.path.dirname(path), name))
    else:
        for f in os.listdir(path):
            abspath = os.path.join(path, f)
            if str(abspath).endswith(".vm"):
                files.append(abspath)
        name = os.path.join(path, os.path.basename(path) + '.asm')
        print(name)
        writer = Writer(name)
        writer.write_init()

    for f in files:
        handle = open(f, "r")
        
        name = os.path.basename(f).split('.')[0]
        writer.set_file_name(name)
        
        for line in handle:
            line = str(line).strip()
            if line == '' or line.startswith('//'):
                continue

            t, tokens = parse_line(line)

            # Write the VM command as a comment for debugging
            writer.write_comment(tokens)

            # Write the actual translated command
            if   t == C_ARITHMETIC: writer.write_arithmetic(tokens[0])
            elif t == C_PUSH:       writer.write_push(tokens[1], tokens[2])
            elif t == C_POP:        writer.write_pop(tokens[1], tokens[2])
            elif t == C_LABEL:      writer.write_label(tokens[1])
            elif t == C_GOTO:       writer.write_goto(tokens[1])
            elif t == C_IF:         writer.write_if(tokens[1])
            elif t == C_FUNCTION:   writer.write_function(tokens[1], int(tokens[2]))
            elif t == C_RETURN:     writer.write_return()
            elif t == C_CALL:       writer.write_call(tokens[1], int(tokens[2]))
            else: print('Invalid command')
        
        handle.close()

    writer.close()


if __name__ == "__main__":
    main(sys.argv)
