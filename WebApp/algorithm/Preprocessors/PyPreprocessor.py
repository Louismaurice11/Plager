# Author(s) : Conor Cowley
from antlr4 import InputStream, CommonTokenStream

from algorithm.Preprocessors.Preprocessor import Preprocessor
from algorithm.Parsers.PyParser.Python3Lexer import Python3Lexer
from algorithm.Parsers.PyParser.Python3Parser import Python3Parser

# PREPROCESSOR FOR PYTHON
class PyPreprocessor(Preprocessor):
    
    #The `preprocessCode` method removes preprocessor directives from code, as well as unnecessary characters"""
    def preprocess(self):
        lexer = Python3Lexer(InputStream(self.file))
        stream = CommonTokenStream(lexer) # stream of common tokens are generated
        parser = Python3Parser(stream) # Generate a parser which uses the common stream of tokens generated by the lexer
        self.tree = parser.stmt()
        self.processed_str = self.tree.getText()

    #The `removeTreeNoise` function aims to remove unnecessary noise such as print statements that could potentially impact the accuracy of the algorithm.
    def removeTreeNoise(self):
        #This may be needed if ANTLR cannot remove the noise for us.
        pass
