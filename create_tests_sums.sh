#!/bin/bash


cd Summators

./create_tests.sh $1 $2

cd ../Summators_LEC

./create_lec_tests.sh $1 $2