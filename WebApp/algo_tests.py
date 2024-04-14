from algorithm.fingerprintDetection import Winnow
from algorithm.winnowLib import winnowLib

from algorithm.Preprocessors.CPreprocessor import CPreprocessor
from algorithm.Preprocessors.CPPPreprocessor import CPPPreprocessor
from algorithm.Preprocessors.CSPreprocessor import CSPreprocessor
from algorithm.Preprocessors.JavaPreprocessor import JavaPreprocessor
from algorithm.Preprocessors.PyPreprocessor import PyPreprocessor

#UPDATE EXTENSION TO TEST EACH LANGUAGE
path1 = 'algorithm/TestFiles/C/source.c'
path2 = 'algorithm/TestFiles/C/plagiarised.c'

sourcefile = open(path1, 'r')
source = sourcefile.read()
sourcefile.seek(0)
srcLines = sourcefile.readlines()

pfile = open(path2, 'r')
plagiarised = pfile.read()
pfile.seek(0)
plgLines = pfile.readlines()

winnowed = winnowLib(source, plagiarised)
winnowed.compareWinnowedFiles()

_, file_type = sourcefile.name.split('.')

if file_type == 'c':
    src_preprocessor = CPreprocessor(path1)
    plg_preprocessor = CPreprocessor(path2)
elif file_type == 'cpp':
    src_preprocessor = CPPPreprocessor(path1)
    plg_preprocessor = CPPPreprocessor(path2)
elif file_type == 'cs':
    src_preprocessor = CSPreprocessor(path1)
    plg_preprocessor = CSPreprocessor(path2)
elif file_type == 'java':
    src_preprocessor = JavaPreprocessor(path1)
    plg_preprocessor = JavaPreprocessor(path2)
elif file_type == 'py':
    src_preprocessor = PyPreprocessor(path1)
    plg_preprocessor = PyPreprocessor(path2)

detection = Winnow(src_preprocessor.tree, plg_preprocessor.tree, 50)

detection.runDetection()