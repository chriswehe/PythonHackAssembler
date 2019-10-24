class Parser:
    def __init__(self, code_array):
        self.code_array = code_array
        self.array_length = len(self.code_array) - 1
        self.array_postn = 0
        self.current_line = self.code_array[0]

    def printArray(self):
        print(self.code_array)

    def printArrayLen(self):
        print(self.array_length)

    def hasMoreCommands(self):
        if self.array_postn < self.array_length:
            return True
        else:
            return False
    
    def advance(self):
        if self.hasMoreCommands() == True:
            self.array_postn = self.array_postn + 1
            self.current_line = self.code_array[self.array_postn].strip() 

    def commandType(self):
        command = ""
        if self.current_line.startswith("("):
            command = "L_COMMAND"
        elif self.current_line.startswith("@"):
            command = "A_COMMAND"
        else:
            command = "C_COMMAND"
        
        return command
    
    def symbol(self):
        symbol = ""
        if self.commandType() == "A_COMMAND":
            symbol = self.current_line[1:len(self.current_line)]
            return symbol
        elif self.commandType() == "L_COMMAND":
            symbol = self.current_line[1:len(self.current_line)-1]
            return symbol
        else:
            return "C_COMMAND"
        
    def dest(self):
        dest = ""

        if self.commandType() == "C_COMMAND":
            if "=" in self.current_line:
                dest = self.current_line[0:self.current_line.find("=")]
                return dest
            else:
                return "null"
        else:
            return "null"

    def comp(self):
        if (self.commandType() == "C_COMMAND"):
            dest = ""
            begginingOfDest = None
            endOfDest = None

            if "=" in self.current_line:
                begginingOfDest = self.current_line.find("=") + 1
            else:
                begginingOfDest = 0
            
            if ";" in self.current_line:
                endOfDest = self.current_line.find(";")
            else:
                endOfDest = (len(self.current_line))
            
            dest = self.current_line[begginingOfDest:endOfDest]
            return dest
        return "null"
    
    def jump(self):
        jump = None

        if self.commandType() == "C_COMMAND":
            if ";" in self.current_line:
                begginingOfDest = self.current_line.find(";")+1
                endOfDest = len(self.current_line)

                jump = self.current_line[begginingOfDest:endOfDest]
                return jump
            else:
                return "null"
        else:
            return "null"
    



