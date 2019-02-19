#!/bin/sh
regex=$1
archive=$2

bin/syntaxis $regex < $archive > res/clean.csv
python src/values.py $regex res/clean.csv