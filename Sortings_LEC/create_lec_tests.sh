#!/bin/bash

mkdir -p cnfs

#python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortBubble_$1_$2.aag -ns ../Sortings/aags/SortInsert_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_BvI_$1_$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortBubble_$1_$2.aag -ns ../Sortings/aags/SortPancake_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_BvP_$1_$2.cnf
python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortBubble_$1_$2.aag -ns ../Sortings/aags/SortSelection_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_BvS_$1_$2.cnf

#python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortInsert_$1_$2.aag -ns ../Sortings/aags/SortPancake_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_IvP_$1_$2.cnf
#python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortInsert_$1_$2.aag -ns ../Sortings/aags/SortSelection_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_IvS_$1_$2.cnf

python3 ../Scripts/LEC_by_two_circuits.py -nf ../Sortings/aags/SortPancake_$1_$2.aag -ns ../Sortings/aags/SortSelection_$1_$2.aag -o ../Sortings_LEC/cnfs/lec_sum_PvS_$1_$2.cnf
