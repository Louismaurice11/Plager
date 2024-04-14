# Author: Conor Cowley
# Author: Terrence Parr C2014
import sys
from typing import TextIO

from antlr4 import Lexer, InputStream




class CSharpLexerBase(Lexer):
    verbatium = False

    interpolatedStringLevel = 0

    interpolatedVerbatiums = []

    curlyLevels = []

    def __init__(self, input: InputStream, output: TextIO = sys.stdout):
        super().__init__(input, output)

    def OnInterpolatedRegularStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(False)
        self.verbatium = False

    def OnInterpolatedVerbatiumStringStart(self):
        self.interpolatedStringLevel += 1
        self.interpolatedVerbatiums.append(True)
        self.verbatium = True

    def OnOpenBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(self.curlyLevels.pop() - 1)

    def OnCloseBrace(self):
        if self.interpolatedStringLevel > 0:
            self.curlyLevels.append(self.curlyLevels.pop() - 1)
            if self.curlyLevels[-1] == 0:
                self.curlyLevels.pop()
                self.Skip()
                self.PopMode()

    def OnColon(self):
        if self.interpolatedStringLevel > 0:
            ind = 1
            switchToFormatString = True
            while self.inputStream.LA(ind) != '}':
                if self.inputStream.LA(ind) == ':' or self.inputStream.LA(ind) == ')':
                    switchToFormatString = False
                    break
                ind += 1
            from .CSharpLexer import CSharpLexer

            if switchToFormatString:
                self.mode(CSharpLexer.INTERPOLATION_FORMAT)

    def OpenBraceInside(self):
        self.curlyLevels.append(1)

    def OnDoubleQuoteInside(self):
        self.interpolatedStringLevel -= 1
        self.interpolatedVerbatiums.pop()
        if len(self.interpolatedVerbatiums) > 0:
            self.verbatium = self.interpolatedVerbatiums[-1]

        else:
            self.verbatium = False

    def OnCloseBraceInside(self):
        self.curlyLevels.pop()

    def IsRegularCharInside(self):
        return not self.verbatium

    def IsVerbatiumDoubleQuoteInside(self):
        return self.verbatium
