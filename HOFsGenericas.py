import re

#------------------- combinatorial.py -------------------#
from operator import mul, add, truth
apply_each = lambda fns, args=[]: map(apply, fns, [args]*len(fns))
bools = lambda lst: map(truth, lst)
bool_each = lambda fns, args=[]: bools(apply_each(fns, args))
conjoin = lambda fns, args=[]: reduce(mul, bool_each(fns, args))
all = lambda fns: lambda arg, fns=fns: conjoin(fns, (arg,))
both = lambda f,g: all((f,g))
all3 = lambda f,g,h: all((f,g,h))
and_ = lambda f,g: lambda x, f=f, g=g: f(x) and g(x)
disjoin = lambda fns, args=[]: reduce(add, bool_each(fns, args))
some = lambda fns: lambda arg, fns=fns: disjoin(fns, (arg,))
either = lambda f,g: some((f,g))
anyof3 = lambda f,g,h: some((f,g,h))
compose = lambda f,g: lambda x, f=f, g=g: f(g(x))
compose3 = lambda f,g,h: lambda x, f=f, g=g, h=h: f(g(h(x)))
ident = lambda x: x

#------------------- combinatorial.py -------------------#
wordsRe = re.compile(r'\S+', re.UNICODE)
words = lambda line: [len(wordsRe.findall(line)), wordsRe.findall(line)]
word = lambda line, arg: wordsRe.findall(line)[arg-1 if arg > 0 else 0] if arg <= words(line) else ''
pos = lambda arg, line: line.find(arg)
nextWord = lambda arg, line: word(line[pos(arg,line):],2) if pos(arg,line) > -1 else ''
isNotRem = lambda line: truth(re.match(r'^.{6}[\s|-]', line, re.UNICODE))
isRem = lambda line: not isNotRem(line)
isEjectOrSkip = lambda line: truth(re.search(r'\b(EJECT|SKIP)\b', line, re.UNICODE))
isNotEjectOrSkip = lambda line: not isEjectOrSkip(line)
sanitize = lambda line: ' '.join(line.split())
isStartswith = lambda line, arg: line.strip().startswith(arg)

#blank = re.compile(r'^$', re.UNICODE)
#isBlank = lambda line: truth(blank.match(line))

isBlank = lambda line: not line.strip()
isNotBlank = lambda line: len(line.strip()) > 0

def iterInv(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
