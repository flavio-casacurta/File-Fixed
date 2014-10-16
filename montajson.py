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
        path = ''.join(open(self.properties).readline().replace("'","").split())
        config = open(os.path.join(path,'config.properties')).readlines()
        dCnfg  ={line.split()[0]:line.split()[1] for line in config}
        ehBook = lambda book: book[-3:].upper() == dCnfg['EXTCPY']

        dirFileList = DirFileList()
        dirFileList.setDirFileList(dCnfg['DIRSOULIB'])
        book_list = dirFileList.getDirFileList()

        for book in filter(ehBook, book_list):
            baseName = os.path.basename(book).split('.')[0]
            print book
            bookWrite = open('{}{}'.format(dCnfg['DIRCNVJSON'], baseName + '.json'),'w')
            bookWrite.writelines(self.col.columns(book))
            bookWrite.close()
