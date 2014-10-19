#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Gera o arquivo .json com a imagem do copybook COBOL

para todos os books do diretório no properties ['DIRSOUVAL'] com a extenção ['EXTCPY']

'pathProp.txt' default do diretório do properties
'''

import os
from columns import Columns
from DirFileList import *

class Montajson(object):

    def __init__(self, properties = 'pathProp.txt'):
        self.properties = properties
        self.col = Columns()

    def montajson(self):
        path = ''.join(open(self.properties).readline().replace("'", "").split())
        config = open(os.path.join(path,'config.properties')).readlines()
        diccnfg = {line.split()[0]:line.split()[1] for line in config}
        isbook = lambda book: book[-3:].upper() == diccnfg['EXTCPY']

        dirfilelist = DirFileList()
        dirfilelist.setDirFileList(diccnfg['DIRSOULIB'])
        booklist = dirfilelist.getDirFileList()

        for book in filter(isbook, booklist):
            basename = os.path.basename(book).split('.')[0]
            print book
            bookwrite = open('{}{}'.format(diccnfg['DIRCNVJSON'], basename + '.json'), 'w')
            bookwrite.writelines(self.col.columns(book))
            bookwrite.close()
