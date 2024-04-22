#!/bin/bash


cd Sortings

./create_tests.sh $1 $2

cd ../Sortings_LEC

./create_lec_tests.sh $1 $2