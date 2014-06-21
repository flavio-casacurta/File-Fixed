# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals
import json
from collections import namedtuple


class Fixed_files(object):

    def __init__(self, fjson):
        try:
            attrs = open('{}.json'.format(fjson)).readlines()
        except:
            attrs = []

        self.lattrs = []
        for line in attrs:
            self.lattrs.append(json.loads(line.decode('utf-8')))

        self.attr=[]
        for att in self.lattrs:
            self.attr.append(att['field'])

        self.slices = ''
        for att in self.lattrs:
            if att['type'] == 'str':
                self.slices += 'record[{}], '.format(att['field'])
            elif att['type'] == 'int':
                self.slices += 'int(record[{}])'.format(att['field'])
                if int(att['decimals']):
                    self.slices += ' * .{:>0{}}'.format('1', att['decimals'])
                self.slices += ', '

        fmt_out_str=''
        fmt_out_fmt=''
        for att in self.lattrs:
            if att['type'] == 'str':
                fmt_out_str += "{}".format('{:<' + att['length'] + '}')
                fmt_out_fmt += 'record["{}"], '.format(att['field'])
            elif att['type'] == 'int':
                if int(att['decimals']):
                   dec = ' * {}'.format(int('{:<0{}}'.format('1', int(att['decimals'])+1)))
                else:
                   dec = ''
                fmt_out_str += '{}'.format('{:>0' + att['length'] + '}')
                fmt_out_fmt += 'str(int(record["{}"]{}))'.format(att['field'], dec)
                fmt_out_fmt += ', '
        self.fmt_out = "'" + fmt_out_str + "'.format(" + fmt_out_fmt + ")"


    def parse(self, record):
        Record = namedtuple('Record', self.attr)
        start = 0
        for att in self.lattrs:
            exec compile("{} = slice({}, {})".format(att['field'], start, (start + int(att['length']))), '', 'exec')
            start += int(att['length'])
        nt = eval("Record({})".format(self.slices))
        return self.dictionarize(nt)


    def dictionarize(self, nt):
        return {k:nt[n] for n, k in enumerate(self.attr)}


    def unparse(self, record):
        return eval("{}".format(self.fmt_out))

