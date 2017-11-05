set -x

if [ ! -e "tmp/train.txt" ]; then
	tar -C tmp -zxvf dac.tar.gz train.txt
fi


if [ ! -e "tmp/criteo.tsv.gz" ]; then
	echo -e 'label\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12\t13\t14\t15\t16\t17\t18\t19\t20\t21\t22\t23\t24\t25\t26\t27\t28\t29\t30\t31\t32\t33\t34\t35\t36\t37\t38\t39' > tmp/criteo.tsv
	cat tmp/train.txt | awk '{ OFS="\t";if ($1 == 0) $1='-1';$1=$1;print}' >> tmp/criteo.tsv
	rm tmp/train.txt
fi

if [ ! -e "tmp/criteo_train.tsv.gz" ]; then
	cat tmp/criteo.tsv | head -40000001 | gzip > tmp/criteo_train.tsv.gz
fi

if [ ! -e "tmp/criteo_test.tsv.gz" ]; then
	cat tmp/criteo.tsv | head -1 > tmp/criteo_test.tsv
	cat tmp/criteo.tsv | tail -n+40000002 >> tmp/criteo_test.tsv
	gzip tmp/criteo_test.tsv
fi
