#!/bin/bash

mkdir -p cnfs

python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultColumn$1x$2.aag -ns ../Multipliers/aags/MultDadda$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_CvD_$1x$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultColumn$1x$2.aag -ns ../Multipliers/aags/MultKaratsuba$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_CvK_$1x$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultColumn$1x$2.aag -ns ../Multipliers/aags/MultWallace$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_CvW_$1x$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultDadda$1x$2.aag -ns ../Multipliers/aags/MultKaratsuba$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_DvK_$1x$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultDadda$1x$2.aag -ns ../Multipliers/aags/MultWallace$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_DvW_$1x$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Multipliers/aags/MultKaratsuba$1x$2.aag -ns ../Multipliers/aags/MultWallace$1x$2.aag -o ../Multipliers_LEC/cnfs/lec_mult_KvW_$1x$2.cnf
