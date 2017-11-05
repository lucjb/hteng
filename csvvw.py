#!/usr/bin/python

__author__ = 'lbernardi'
import gzip
import sys
import fileinput
import argparse
import math
from math import sin, cos, sqrt, atan2, radians

from collections import defaultdict
import csv
from csv import DictReader


parser = argparse.ArgumentParser(description='')
parser.add_argument('-sep', help='Separator. Default: tab.', required=False, dest='sep', default='\t')
parser.add_argument('-num_index', help='Everything after num_index is numeric', required=False, dest='num_index', type=int)
parser.add_argument('-w', help='Weight index', required=False, dest='weight_index', type=int)
parser.add_argument('-t', help='Target index, default: -1.', required=False, dest='target_index', type=int, default=-1)
parser.add_argument('-pos_w', help='Fixed weight for all instances labeled as positive.', required=False, dest='pos_w', type=float)
parser.add_argument('-c', help='Include a constant feature.', required=False, dest='constant', action='store_true')
args = parser.parse_args()
sep, num_index, wi, ti, pos_w, include_constant = args.sep, args.num_index, args.weight_index, args.target_index, args.pos_w, args.constant

data = csv.reader(sys.stdin, delimiter=sep)
out = sys.stdout

header = data.next()
row_len = len(header)


if num_index == None:
    num_index = row_len
else:
    if num_index < 0:
        num_index = row_len + num_index

pos_count = 0
total_count = 0

for row in data:
    label = row[ti]
    w = 1

    if pos_w:
        if label =='1':
            w = pos_w
    if wi:
        w = float(row[wi])

    line = label + ' ' + str(w) + '  '

    if include_constant:
        line += '|bias 1 '

    fields = []
    for i, v in enumerate(row[:num_index]):
        if (i == ti) or ((ti< 0) and (i == row_len + ti)) or (wi and ((i == wi) or ((wi< 0) and (i == row_len + wi)))):
            continue
        fn = header[i]
        fields.append('|'+fn)
        fields.append(v)
    line +=' '.join(fields) + ' '

    if num_index != row_len:
        line+='|num '

    for j, v in enumerate(row[num_index:-1]):
        i = j+num_index
        if (i == ti) or ((ti< 0) and (i == row_len + ti)) or (wi and ((i == wi) or ((wi< 0) and (i == row_len + wi)))):
            continue
	if v != 'NaN':
	        fn = header[i]
        	line += fn + ':' + v + ' '
    line+='\n'


    out.write(line)
out.close()

