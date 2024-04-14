from antlr4 import *
from antlr4.tree.Tree import TerminalNodeImpl


class Winnow:
    HashedSet1 = []
    HashedSet2 = []
    matchedLineNumbers = []

    def __init__(self, t1, t2, massThreshold):
        self.tree1 = t1
        self.tree2 = t2
        self.mThreshold = massThreshold
        self.matchedLineNumbers = []

    def findSubtrees(self, node):
        subtrees = [node]
        if not isinstance(node, TerminalNode):
            for child in node.getChildren():
                subtrees.extend(self.findSubtrees(child))
        return subtrees

    """ This function is used simply to generate hash's of all of the nodes so they 
        can be compared in the fingerprint/winnowing algorithm """

    def hashTreeNodes(self, trees):
        import hashlib
        uniqueTrees = list()

        for tree in trees:
            if isinstance(tree, TerminalNodeImpl):
                pass
            else:
                text = tree.getText()
                line = tree.start.line
            print(text)
            hashedNode = hashlib.sha256()
            hashedNode.update(text.encode("utf-8"))

            uniqueTrees.append((line, hashedNode.hexdigest()))

        uniqueTrees = set(uniqueTrees)

        return uniqueTrees

    def runDetection(self):

        hits = 0
        misses = 0

        treeSet1 = self.findSubtrees(self.tree1)
        self.HashedSet1 = self.hashTreeNodes(treeSet1)
        treeSet2 = self.findSubtrees(self.tree2)
        self.HashedSet2 = self.hashTreeNodes(treeSet2)

        for hash1 in self.HashedSet1:
            isDetected = False
            for hash2 in self.HashedSet2:
                if hash1[1] == hash2[1]:
                    hits += 1
                    self.matchedLineNumbers.append((hash1[0],hash2[0]))
                    isDetected = True
                    break
            if not isDetected:
                misses += 1

        similarity = hits / (misses + hits) * 100

        #print("similarity is " + str(similarity) + "% for winnowing")
        #print(self.matchedLineNumbers)
        return similarity
