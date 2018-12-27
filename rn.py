#!/bin/python
#coding:utf-8

import os
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4 :
        sys.exit()
    if len(sys.argv) == 3:
        src_p = "./"
        src_tp = sys.argv[1]
        to_tp = sys.argv[2]
    else:
        src_p = sys.argv[1]
        src_tp = sys.argv[2]
        to_tp = sys.argv[3]

    src_tp = "." + src_tp if src_tp.startswith(".") else src_tp
    to_tp = "." + to_tp if to_tp.startswith(".") else to_tp

    for fpathe,dirs,fs in os.walk(src_p):
        for f in fs:
            ffp = os.path.join(fpathe,f)
            if not ffp.endswith(src_tp):
                continue
            toffp = ffp[:-1*len(src_tp)]+to_tp
            os.rename(ffp,toffp)


