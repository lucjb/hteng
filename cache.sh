zcat $1 | pypy csvvw.py -t $3 | vw -b 32 --sparse_weights -t --cache_file tmp/train.cache -k 
zcat $2 | pypy csvvw.py -t $3 | vw -b 32 --sparse_weights -t --cache_file tmp/test.cache -k 

