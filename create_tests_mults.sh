#!/bin/bash


cd Multipliers

./create_tests.sh $1 $2

cd ..

cd Multipliers_LEC

./create_lec_tests.sh $1 $2