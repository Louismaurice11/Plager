# Author : Xavier Parnell
import re
from winnowing import winnow


class winnowLib:
    processedSrcFile = []
    processedTrgFile = []
    matchedLines = []

    def __init__(self, srcFile, trgFile):
        self.processedSrcFile = self.winnow_with_line_numbers(srcFile)
        self.processedTrgFile = self.winnow_with_line_numbers(trgFile)

    def winnow_with_line_numbers(self, text):
        # split the text into lines
        lines = text.splitlines()
        hashes = []
        unhashed = []
        # iterate through list of lines
        for index, line in enumerate(lines):
            # if a line is blank ignore it
            if line == '':
                continue
            else:
                # append each line number and hashed fragment to list
                hashes.append((index+1, winnow(line)))


        # return the list of lines and associated hash values
        return hashes

    def compareWinnowedFiles(self):
        # initialise counters to zero and list of matched line numbers to the empty list
        hits = 0
        misses = 0
        self.matchedLines = []

        # iterate through the hashed source file fragments
        for item in self.processedSrcFile:
            # set the isHit boolean flag to False
            isHit = False
            # iterate through the hashed target file fragments
            for pair in self.processedTrgFile:
                # compare the hashed values in each tuple to detect a match
                if item[1] == pair[1]:
                    # a match has been found, increment the hits count
                    hits += 1
                    # append the matched line numbers for each file to lineNums list as a tuple
                    self.matchedLines.append((item[0], pair[0]))
                    # set the isHit flag to true, as a hit has been found
                    isHit = True
            # if no hit is found increment the miss count
            if not isHit:
                misses += 1

        return self.matchedLines
        # print the matched line tuples
        #print("Winnow library matched line numbers = " + str(self.matchedLines))


