from Parser import Parser
from CodeModule import CodeModule
from SymbolTableModule import SymbolModule

code = """@0
D=M
@23
D;JLE
@16
M=D
@16384
D=A
@17
M=D
@17
A=M
M=-1
@17
D=M
@32
D=D+A
@17
M=D
@16
MD=M-1
@10
D;JGT
@23
0;JMP
"""

def assembler(codeString):
    code_array = codeString.split("\n")
    parser1 = Parser(code_array)
    codeModule = CodeModule()
    counter = 0
    new_code_array = []

    while parser1.hasMoreCommands():
        machineCode = None
        if parser1.commandType() == "C_COMMAND":
            print("c command")
            compCommand = codeModule.comp(parser1.comp())
            destCommand = codeModule.dest(parser1.dest())
            jumpCommand = codeModule.jump(parser1.jump())
            machineCode = compCommand + destCommand + jumpCommand
            print(machineCode)
        elif parser1.commandType() == "A_COMMAND":
            num = parser1.symbol()
            machineCode = '{0:016b}'.format(int(num))
        if (parser1.commandType() == "C_COMMAND") or (parser1.commandType() == "A_COMMAND"):
            new_code_array.append(machineCode)
            counter = counter + 1
            parser1.advance()

    return new_code_array

print(assembler(code))