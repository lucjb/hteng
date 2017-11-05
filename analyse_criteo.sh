set -x
bash prepare_criteo.sh
bash cache.sh tmp/criteo_train.tsv.gz tmp/criteo_test.tsv.gz 0
bash scan_hash_space.sh criteo_log.csv
bash count_collisions.sh tmp/criteo_train.tsv.gz 0 criteo_log.csv
