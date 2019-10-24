from Parser import Parser
from CodeModule import CodeModule
from SymbolTableModule import SymbolModule

code = """@0
"""

def assembler(codeString):
    code_array = codeString.split("\n")
    parser1 = Parser(code_array)
    codeModule = CodeModule()
    counter = 0
    new_code_array = []

    while parser1.hasMoreCommands():
        print('hello')
        machineCode = None
        if parser1.commandType() == "C_COMMAND":
            print("hello")
            compCommand = codeModule.comp(parser1.comp())
            destCommand = codeModule.dest(parser1.dest())
            jumpCommand =  codeModule.jump(parser1.jump())
            machineCode = "0" + compCommand + destCommand + jumpCommand
        elif parser1.commandType() == "A_COMMAND":
            print("hello")
        if (parser1.commandType() == "C_COMMAND") or (parser1.commandType() == "A_COMMAND"):
            new_code_array[counter] = "hello"
            counter = counter + 1
            parser1.advance()
            print('bye')
    
    return new_code_array

print(assembler(code))