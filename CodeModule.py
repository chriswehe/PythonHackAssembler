compMap = {
    "0":  "1110101010",
    "1":  "1110111111",
    "-1": "1110111010",
    "D":  "1110001100",
    
    "A":  "1110110000",
    "M":  "1111110000",
    
    "!D": "1110001101",
    "!A": "1110110001",
    "!M": "1111110001",
    
    "-D": "1110001111",
    "-A": "1110110011",
    "-M": "1111110011",
    
    "D+1": "1110011111",
    "A+1": "1110110111",
    "M+1": "1111110111",
    
    "D-1": "1110001110",
    "A-1": "1110110010",
    "M-1": "1111110010",
    
    "D+A": "1110000010",
    "D+M": "1111000010",
    
    "D-A": "1110010011",
    "D-M": "1111010011",
    
    "A-D": "1110000111",
    "M-D": "1111000111",
    "D&A": "1110000000",
    "D&M": "1111000000",
    "D|A": "1110010101",
    "D|M": "1111010101",
    "null": "no value"
}

destMap = {
    "null": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111"
}

jumpMap = {
    "null": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111",
}
class CodeModule:
    def __init__(self):
        self.compMap = compMap
        self.destMap = destMap
        self.jumpMap = jumpMap

    def comp(self, command):
        translation = self.compMap[command]
        return translation

    def dest(self, command):
        translation = self.destMap[command]
        return translation
    
    def jump(self, command):
        translation = self.jumpMap[command]
        return translation
    
        
