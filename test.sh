#!bin/bash

for i in $( seq 70 85)
do
	python src/hac.py ${i} > res/${i}.txt
done
