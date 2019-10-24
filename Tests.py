from Parser import Parser
from CodeModule import CodeModule
from SymbolTableModule import SymbolModule

code = """@0
MD=M-1
D;JGT"""
code_array = code.split("\n")

parser = Parser(code_array)
CodeModule = CodeModule()
SymbolModule = SymbolModule()

# parser.printArray()
# parser.printArrayLen()

# print(parser.array_postn)

# print(parser.commandType())
# print(parser.symbol())

# parser.advance()
# print("command two")
# print(parser.commandType())
# print(parser.symbol())
# print(parser.dest())
# print(parser.comp())
# print(parser.jump())

# parser.advance()
# print("command three")
# print(parser.commandType())
# print(parser.symbol())
# print(parser.dest())
# print(parser.comp())
# print(parser.jump())

# # code module test
# print(CodeModule.jumpMap)

# print(CodeModule.jump("JEQ"))

# symbol table module test

print(SymbolModule.symbolTable)
SymbolModule.addEntry("R16", 16)
print(SymbolModule.symbolTable)

print(SymbolModule.getAddress("R16"))
