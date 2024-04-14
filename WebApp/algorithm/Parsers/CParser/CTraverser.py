from antlr4.Token import CommonToken
from antlr4.TokenStreamRewriter import TokenStreamRewriter
from antlr4.tree.Tree import TerminalNodeImpl

from algorithm.Parsers.CParser.CListener import CListener

from algorithm.Parsers.CParser.CParser import CParser
from algorithm.Parsers.CParser.CLexer import CLexer


class CTraverser(CListener):
    nodes = []

    def __init__(self,inputstream):
        self.inputStream = inputstream
        self. rewriter = TokenStreamRewriter(inputstream)


    text = ""

    def enterPostfixExpression(self, ctx: CParser.PostfixExpressionContext):
        if ctx.Identifier() is not None:
            new_name = "XX"
            iToken = ctx.Identifier()[0].getSymbol()
            stop = iToken.stop + 1
            self.rewriter.replace(ctx.start, stop, new_name)

    def enterEveryRule(self, ctx):
        self.text += ctx.getText()
        self.nodes.append(hash(ctx.getText()))

    def visit(self, ctx):
        if isinstance(ctx, CParser.Identifier):
            variable = ctx.geText()

            new_token = CommonToken(CLexer.Int, 10)
            new_node = TerminalNodeImpl(new_token)

            return new_node

    def clearNodes(self):
        self.nodes.clear()

    def getNodes(self):
        return self.nodes
