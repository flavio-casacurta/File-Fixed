from HOFsGenericas import *


isCopy = lambda line: 'COPY' in words(line)[1]
isInclude = lambda line: ('INCLUDE' in words(line)[1] and 'SQLCA' not in words(line)[1])
isLink = lambda line: 'LINK' in words(line)[1]
isXctl = lambda line: 'XCTL' in words(line)[1]
isCall = lambda line: 'CALL' in words(line)[1]
isPic = lambda line: 'PIC' in words(line)[1]
procRe = re.compile(r'PROCEDURE[\s]+DIVISION', re.UNICODE)
isProcedure = lambda line: truth(procRe.findall(line))
l672 = lambda line: line[6:72].rstrip()
isNotBlank = lambda line: len(l672(line).strip()) > 0

