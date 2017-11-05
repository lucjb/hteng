#!/usr/bin/python
__author__ = 'ikangas'
import sys
import argparse

parser = argparse.ArgumentParser(description='Computes a ground truth file where every feature value is present exactly once. This is mainly aimed to speed up the hash invertion process.')
parser.add_argument('-sep', help='Separator. Default: tab.', required=False, dest='sep', default='\t')
parser.add_argument('-num_index', help='Everything after num_index is numeric', required=False, dest='num_index', type=int)
parser.add_argument('-w', help='Weight index', required=False, dest='weight_index', type=int)
parser.add_argument('-t', help='Target index, default: -1.', required=False, dest='target_index', type=int, default=-1)
args = parser.parse_args()
sep, num_index, wi, ti= args.sep, args.num_index, args.weight_index, args.target_index

data = sys.stdin
out = sys.stdout
ft_store = {}
 
headers = data.readline()
out.write(headers)
headers = headers.rstrip().split(sep)

if ti<0:
    ti = len(headers)+ti

if wi and wi<0:
    wi = len(headers)+wi

for i, h in enumerate(headers):
    if i == ti or i == wi:
        continue
    ft_store[h] = set()


for line in data:
    row = line.rstrip().split(sep)
    out_line = ''
    emit = False
    for i, f in enumerate(row):
        if i == ti or i == wi:
            out_line += f + sep
            continue
        a = ft_store[headers[i]]
        if f not in a:
            out_line += f + sep
            a.add(f)
            emit = True
        else:
            out_line += sep

    if emit:
        out.write(out_line[:-1]+'\n')
out.close()
