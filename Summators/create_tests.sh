#!/bin/bash

for type in Simple LogHeight
do
	python3 sum_alg.py -n $1 -m $2 -t $type
done
