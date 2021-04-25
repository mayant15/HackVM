from typing import List
from translations import *


class Writer(object):

    __file = None
    __currentName = ""
    __nLine = 1
    __nRet = 1

    def __init__(self, path: str):
        self.__file = open(path, "w")

    def set_file_name(self, name: str) -> None:
        self.__currentName = name

    def close(self) -> None:
        self.__file.close()

    def write_init(self) -> None:
        self.__file.write(init)

    def write_end(self) -> None:
        self.__file.write(end)

    def write_comment(self, tokens: List[str]) -> None:
        string = " ".join(tokens)
        self.__file.write(f'\n; {string}\n')

    def write_arithmetic(self, op: str) -> None:
        n = self.__nLine
        n += 1
        self.__file.write(arithmetic[op].format(n, n))
        self.__nLine = n

    def write_push(self, segment: str, arg: int) -> None:
        line = ""
        if segment == "pointer":
            line = push[segment].format("that" if arg else "this")
        elif segment == "temp":
            line = push[segment].format(5 + arg)
        elif segment == "static":
            line = push[segment].format(self.__currentName, arg)
        else:
            line = push[segment].format(arg)
        self.__file.write(line)

    def write_pop(self, segment: str, arg: str) -> None:
        line = ""
        if segment == "pointer":
            line = pop[segment].format("that" if int(arg) else "this")
        elif segment == "temp":
            line = pop[segment].format(5 + int(arg))
        elif segment == "static":
            line = pop[segment].format(self.__currentName, arg)
        else:
            line = pop[segment].format(arg)
        self.__file.write(line)

    def write_label(self, arg: str) -> None:
        self.__file.write(label.format(arg))

    def write_goto(self, arg: str) -> None:
        self.__file.write(goto.format(arg))

    def write_if(self, arg: str) -> None:
        self.__file.write(if_goto.format(arg))

    def write_function(self, func: str, varc: int) -> None:
        self.__file.write(f'({func})')
        for i in range(varc):
            self.__file.write(push0)

    def write_return(self) -> None:
        self.__file.write(return_)

    def write_call(self, func: str, argc: int) -> None:
        n = self.__nRet
        n = n + 1
        self.__file.write(call.format(func, n, 5 + int(argc), func, func, n))
        self.__nRet = n
