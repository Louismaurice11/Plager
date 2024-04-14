#Author(s) : Conor Cowley, Xavier Parnell

# Preprocessor Base Class to generate an AST for a given programming language by implementing the preprocessCode method.
class Preprocessor:

    path = ""
    file = ""
    filename = ""
    tree = ""
    processed_str = ""

    def __init__(self, path):
        self.path = path
        self.file = open(self.path, 'r').read()
        self.getFilename()
        self.preprocess()

    #The `preprocessCode` method removes preprocessor directives from code, as well as unnecessary characters.
    def preprocessCode(self, file, name):
        pass

    # Writes preprocessed code to file given by 'path' as a string.
    def writeToFile(self, path):
        f = open(path, "w")
        f.write(self.processed_str)
        f.close()

    #Gets filename from path.
    def getFilename(self):
        file = open(self.path, "r")
        self.filename = file.name

    #The `removeTreeNoise` function aims to remove unnecessary noise such as print statements that could potentially impact the accuracy of the algorithm.
    def removeTreeNoise(self, t1):
        #This may be needed if ANTLR cannot remove the noise for us.
        pass
