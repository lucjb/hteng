set -x
bash prepare_avazu.sh
bash cache.sh tmp/avazu_train.tsv.gz tmp/avazu_test.tsv.gz 1
bash scan_hash_space.sh avazu_hash_log.csv
bash count_collisions.sh tmp/avazu_train.tsv.gz 1 avazu_col_log.csv
