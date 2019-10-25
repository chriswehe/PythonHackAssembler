from Parser import Parser
from CodeModule import CodeModule
from SymbolTableModule import SymbolModule

code = """@0
D=M
@INFINITE_LOOP
D;JLE
@counter
M=D
@SCREEN
D=A
@address
M=D
(LOOP)
@address
A=M
M=-1
@address
D=M
@32
D=D+A
@address
M=D
@counter
MD=M-1
@LOOP
D;JGT
(INFINITE_LOOP)
(hellothere)
@INFINITE_LOOP
0;JMP
"""

def assembler(codeString):
    code_array = codeString.split("\n")
    parser1 = Parser(code_array)
    parser2 = Parser(code_array)
    parser3 = Parser(code_array)
    codeModule = CodeModule()
    symbolModule = SymbolModule()
    counter = 0
    new_code_array = []
    current_symbol_address = 0

    while parser2.hasMoreCommands():
        if parser2.commandType() == "L_COMMAND":
            symbolModule.addEntry(parser2.symbol(), current_symbol_address)
            current_symbol_address = current_symbol_address - 1
        current_symbol_address = current_symbol_address + 1
        parser2.advance()
        
    print(symbolModule.symbolTable)

    while parser3.hasMoreCommands():
        if parser2.commandType() == "A_COMMAND":
            try:
                pass
            except expression as identifier:
                pass


    while parser1.hasMoreCommands():
        machineCode = None
        if parser1.commandType() == "C_COMMAND":
            compCommand = codeModule.comp(parser1.comp())
            destCommand = codeModule.dest(parser1.dest())
            jumpCommand = codeModule.jump(parser1.jump())
            machineCode = compCommand + destCommand + jumpCommand
        elif parser1.commandType() == "A_COMMAND":
            num = parser1.symbol()
            machineCode = '{0:016b}'.format(int(num))
        if (parser1.commandType() == "C_COMMAND") or (parser1.commandType() == "A_COMMAND"):
            new_code_array.append(machineCode)
            counter = counter + 1
            parser1.advance()

    return new_code_array

print(assembler(code))