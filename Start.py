from Parser import Parser
code = """@0
MD=M-1
D;JGT"""
code_array = code.split("\n")

parser = Parser(code_array)

# parser.printArray()
# parser.printArrayLen()

# print(parser.array_postn)

print(parser.commandType())
print(parser.symbol())

parser.advance()
print(parser.dest())
print(parser.comp())

parser.advance()
print(parser.dest())
print(parser.comp())