# Author: Conor Cowley
# Author: Ken Domino
import sys
from typing import TextIO

from antlr4 import Parser, TokenStream




class CSharpParserBase(Parser):

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)



    def IsLocalVariableDeclaration(self):
        from Parsers.CSParser.CSharpParser import CSharpParser

        if not isinstance(self._ctx, CSharpParser.Local_variable_declarationContext):
            return False

        var = CSharpParser.Local_variable_declarationContext
        local_var_decl = CSharpParser.Local_variable_declarationContext(self._ctx)
        if local_var_decl is None:
            return True

        var = CSharpParser.Local_variable_typeContext

        local_variable_type = local_var_decl.local_variable_type()

        if local_variable_type is None:
            return True

        if local_variable_type.getText().equals("var"):
            return False

        return True
