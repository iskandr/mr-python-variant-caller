#!/usr/bin/env python

from operator import itemgetter
import sys
from collections import Counter

current_locus = None
current_count = None


# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    locus, base = line.split('\t', 1)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_locus == locus:
        current_count[base] += 1
    else:
        if current_locus:
            # write result to STDOUT
            print '%s\t%s' % (current_locus, current_count)
        current_count = Counter()
        current_count[base] += 1
        current_locus = locus

# do not forget to output the last word if needed!
if current_locus == locus:
    print '%s\t%s' % (current_locus, current_count)