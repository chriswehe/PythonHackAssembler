from Parser import Parser
from CodeModule import CodeModule
from SymbolTableModule import SymbolModule

code = """MD=M-1
D;JLE
MD=M-1
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
            
        if (parser1.commandType() == "C_COMMAND") or (parser1.commandType() == "A_COMMAND"):
            print('bye')
            new_code_array.append = machineCode
            counter = counter + 1
            parser1.advance()

    return new_code_array

print(assembler(code))