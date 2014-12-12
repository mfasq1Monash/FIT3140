class FunctionList():

    def __init__(self):
        self.codeList = []

    def insertInstruction(self, instruction, index):
        self.codeList.insert(instruction, index)

    def removeInstruction(self, index):
        self.codeList.del(index)

    def getInstruction(self, index):
        return self.codeList[index]
