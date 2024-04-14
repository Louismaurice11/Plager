# Author(s) : Conor Cowley, Xavier Parnell
from antlr4 import InputStream, CommonTokenStream

from algorithm.Preprocessors.Preprocessor import Preprocessor
from algorithm.Parsers.CParser.CLexer import CLexer
from algorithm.Parsers.CParser.CParser import CParser

from algorithm.Parsers.CParser.CVisitor import CVisitor

# PREPROCESSOR FOR C
class CPreprocessor(Preprocessor):

    #The `preprocess` method removes preprocessor directives from code, as well as unnecessary characters
    def preprocess(self):
        lexer = CLexer(InputStream(self.file)) # Generates the appropriate lexer from the file
        stream = CommonTokenStream(lexer) # This can be then used to generate a stream of common tokens
        parser = CParser(stream)  # We can then pass these stream of tokens to the parser, as it recognises them and can construct a parse tree from this
        self.tree = parser.translationUnit() # Finally, the tree is generated
        self.removeTreeNoise()
        self.processed_str = self.tree.getText() # Retrieve the text of the preprocessed code

    #The `removeTreeNoise` function aims to remove unnecessary noise such as print statements that could potentially impact the accuracy of the algorithm.
    def removeTreeNoise(self):
        visitor = CVisitor()
        visitor.visit(self.tree)        
        #This may be needed if ANTLR cannot remove the noise for us.
