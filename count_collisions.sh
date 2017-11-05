#!/bin/bash
zcat $1 | pypy minfeatureset.py | pypy csvvw.py -t $2 | gzip > tmp/min_train.vw.gz
for i in {18..27}
do
	rm tmp/hash.csv
        zcat tmp/min_train.vw.gz | vw -b $i --invert_hash tmp/hash.csv --initial_weight 100 2>/dev/null;
        echo $i $(tail -n+12 tmp/hash.csv | wc -l) $(tail -n+12 tmp/hash.csv | awk -F: '{print $2}' | sort | uniq | wc -l) >> $3
done
for i in {28..40}
do
	rm tmp/hash.csv
	zcat tmp/min_train.vw.gz | vw -b $i --sparse_weights --invert_hash tmp/hash.csv --initial_weight 100 2>/dev/null;
	echo $i $(tail -n+12 tmp/hash.csv | wc -l) $(tail -n+12 tmp/hash.csv | awk -F: '{print $2}' | sort | uniq | wc -l) >> $3
done
