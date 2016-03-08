#!/usr/bin/env python 
#
# Note: If this script fails half-way, relationships break and the whole 
# thing is fucked. 
from __future__ import print_function

import json
import os
import random

from collections import defaultdict


CUR_SYM = 0
def gensym():
    global CUR_SYM
    
    CUR_SYM += 1
    return CUR_SYM


if __name__ == '__main__':
    remapped = defaultdict(gensym)

    for file_name in os.listdir(os.curdir):
        if file_name.endswith(".ids.json"):
            print(file_name, end=': ')

            with open(file_name) as fp:
                ids = json.load(fp)

            random.shuffle(ids)
            anonymized_ids = [remapped[i] for i in ids]

            # Sanity Check
            j, k = sum(ids), sum(anonymized_ids)
            print(j, k)
            assert j != k

            with open(file_name, 'w') as fp:
                json.dump(anonymized_ids, fp)
