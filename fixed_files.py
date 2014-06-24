# -*- coding: utf-8 -*-


from __future__ import absolute_import, unicode_literals
import json
from collections import namedtuple
from Exceptions import FieldLengthOverflow

__author__ = 'flavio@casacurta.com'

class Fixed_files(object):


    def __init__(self, filejson, dic=False, checklength=False):

        self.dic = dic
        self.checklength = checklength

        try:
            attrs = open('{}.json'.format(filejson)).readlines()
        except:
            attrs = []

        self.lattrs = []
        for line in attrs:
            self.lattrs.append(json.loads(line.decode('utf-8')))

        self.attr = []
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

        fmt_out_str = ''
        fmt_out_fmt = ''
        for att in self.lattrs:
            if att['type'] == 'str':
                fmt_out_str += "{}".format('{:<' + att['length'] + '}')
                if self.dic:
                    fmt_out_fmt += 'record["{}"][:{}], '.format(att['field'], att['length'])
                else:
                    fmt_out_fmt += 'record.{}[:{}], '.format(att['field'], att['length'])
            elif att['type'] == 'int':
                if int(att['decimals']):
                    dec = ' * {}'.format(int('{:<0{}}'.format('1', int(att['decimals'])+1)))
                else:
                    dec = ''
                fmt_out_str += '{}'.format('{:>0' + att['length'] + '}')
                if self.dic:
                    fmt_out_fmt += 'str(int(record["{}"]{}))[:{}]'.format(att['field'], dec, att['length'])
                else:
                    fmt_out_fmt += 'str(int(record.{}{}))[:{}]'.format(att['field'], dec, att['length'])
                fmt_out_fmt += ', '
        self.fmt_out = "'" + fmt_out_str + "\\n'.format(" + fmt_out_fmt + ")"


    def parse(self, record):

        Record = namedtuple('Record', self.attr)
        start = 0
        for att in self.lattrs:
            exec ("{} = slice({}, {})".format(att['field'], start, (start + int(att['length']))))
            start += int(att['length'])
        nt = eval("Record({})".format(self.slices))
        if self.dic:
            return self.to_dict(nt)
        else:
            return nt


    def to_dict(self, nt):

        return {k:nt[n] for n, k in enumerate(self.attr)}


    def unparse(self, record):

        if self.checklength:
            for att in self.lattrs:
                if att['type'] == 'str':
                    if self.dic:
                        check = 'len(record["{}"]) > {}'.format(att['field'], att['length'])
                    else:
                        check = 'len(record.{}) > {}'.format(att['field'], att['length'])
                elif att['type'] == 'int':
                    if int(att['decimals']):
                        dec = ' * {}'.format(int('{:<0{}}'.format('1', int(att['decimals'])+1)))
                    else:
                        dec = ''
                    if self.dic:
                        check = 'len(str(int(record["{}"]{}))) > {}'.format(att['field'], dec, att['length'])
                    else:
                        check = 'len(str(int(record.{}{}))) > {}'.format(att['field'], dec, att['length'])
                if eval(check):
                    raise FieldLengthOverflow

        return eval("{}".format(self.fmt_out))

