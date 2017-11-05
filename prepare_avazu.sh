set -x

if [ ! -e "tmp/avazu.tsv.gz" ]; then
	zcat avazu.gz | awk -F, '{ if ($2 == 0) $2='-1'; else $2 = $2;print}' | tr ' ' '\t' | gzip > tmp/avazu.tsv.gz
fi

if [ ! -e "tmp/avazu_train.tsv.gz" ]; then
	zcat tmp/avazu.tsv.gz | head -32000000 | gzip > tmp/avazu_train.tsv.gz
fi

if [ ! -e "tmp/avazu_test.tsv.gz" ]; then
	zcat tmp/avazu.tsv.gz | head -1 > tmp/avazu_test.tsv
	zcat tmp/avazu.tsv.gz | tail -n+32000001 >> tmp/avazu_test.tsv
	gzip tmp/avazu_test.tsv
fi

