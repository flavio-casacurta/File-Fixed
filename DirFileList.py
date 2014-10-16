# -*- coding: utf-8 -*-

import os


class DirFileList:
    def __init__(self):
        self._dirFileList = []

    def __listDirs(self, path):
        try:
            if os.path.isfile(path) is True:
                self._dirFileList.append(path)
            else:
                abspath = map(lambda x: os.path.join(path, x),
                              os.listdir(path))
                if abspath is not []:
                    map(lambda x: self.__listDirs(x), abspath)
        except:
            self._dirFileList.extend(path)

    def getDirFileList(self):
        return self._dirFileList

    def setDirFileList(self, path):
        self.__listDirs(path)

    dirFileList = property(fget=getDirFileList, fset=setDirFileList)

