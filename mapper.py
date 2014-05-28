#!/usr/bin/env python

import sys

"""
SAM file looks like:

@HD VN:1.3  SO:coordinate
@SQ SN:artificial   LN:1120
read1   67  artificial  1   90  10M10D50M   =   1   0   AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA    IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII    AS:i:70 XS:i:70 NM:i:20 MD:Z:10^AAAAAAAAAA50

Making each tab into a newline gives:
read2
67
artificial
1 
90
10M10D50M
=
1
0 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGGGGGGGGGAAAAAA
IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
AS:i:70 XS:i:70 NM:i:30 MD:Z:10^AAAAAAAAAA34AAAAAAAAAA6
"""


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    if line.startswith("@"):
        continue
    # split the line into words
    parts = line.split('\t')
    (qname, flag, rname, pos, mapq, cigar, rnext, pnext, tlen, seq, qual) = parts[:11]
    pos = int(pos)
    for i, char in enumerate(seq):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        print '%s\t%s' % (rname +  ":" + str(pos + i), char)