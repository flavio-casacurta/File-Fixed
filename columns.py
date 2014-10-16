from HOFs import *
from attribute import Attribute

class Columns(object):

    def __init__(self):
        self.attr = Attribute(lenVar=4)

    def columns(self, file):
        lines = open(file).readlines()
        clearLines = map(l672, filter(all3(isNotRem, isNotBlank, isNotEjectOrSkip), lines))
        joinLines = []
        holder = []
        for l in clearLines:
            holder.append(l if not holder else l.strip())
            if l.endswith('.'):
                joinLines.append(" ".join(holder))
                holder = []
        lines = joinLines

        addColumns = []
        filler = 0
        redefines = False
        lvlAnt = 0

        for lin in lines:

            line = lin[:-1]
            wrd, wrds = words(line)

            if not wrds[0].isdigit():
                continue

            level = int(wrds[0])

            if redefines:
                if level > lvlAnt:
                    continue
            redefines = False

            if 'REDEFINES' in wrds:
                lvlAnt = level
                redefines = True
                continue

            if 'PIC' not in wrds:
                continue

            dataName = wrds[1].lower().replace('-','_')
            if dataName == 'filler':
                continue
            picture = line.split('PIC')[1].split()
            pic = picture[0]
            usage = picture[1] if len(picture) > 1 and picture[1] != 'VALUE' else None
            occurs = picture[2:] if len(picture) > 2 and picture[2] == 'OCCURS' else None
            type, length, decimals = self.attr.attribute_json(pic, usage, occurs)

            tCol = '"field": "{}", "length": "{}", "type": "{}", "decimals":  "{}"'.format(dataName,
                                                                                             length,
                                                                                             type,
                                                                                             decimals)
            tCol = '{'+ tCol +'}\n'
            addColumns.append(tCol)
        return addColumns
