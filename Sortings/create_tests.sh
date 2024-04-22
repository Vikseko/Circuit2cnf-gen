#!/bin/bash

mkdir -p aags
mkdir -p aigs
mkdir -p cnfs

for type in Bubble Pancake Selection # Insert
do
	python3 sort_alg.py -n $1 -s $2 -t $type
done
