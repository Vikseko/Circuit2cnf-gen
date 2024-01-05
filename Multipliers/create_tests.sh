#!/bin/bash

for type in Column Dadda Karatsuba Wallace
do
	python3 mult_alg.py -n $1 -m $2 -t $type
done
