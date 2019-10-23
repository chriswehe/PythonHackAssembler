from Parser import Parser
from CodeModule import CodeModule

code = """@0
MD=M-1
D;JGT"""
code_array = code.split("\n")

parser = Parser(code_array)
CodeModule = CodeModule()

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

print(CodeModule.jumpMap)

print(CodeModule.jump("JEQ"))