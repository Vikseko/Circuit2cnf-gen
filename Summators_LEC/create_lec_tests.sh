#!/bin/bash

mkdir -p cnfs

python3 ../Scripts/LEC_by_two_circuits.py -nf ../Summators/aags/SumSimple$1+$2.aag -ns ../Summators/aags/SumLogHeight$1+$2.aag -o ../Summators_LEC/cnfs/lec_sum_SvLH_$1x$2.cnf
