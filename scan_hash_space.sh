#!/bin/bash

for i in {18..26}
do
        vw --cache_file tmp/train.cache -b $i --loss_function logistic -f tmp/model --ftrl 2>/dev/null;
	echo $i $(vw --cache_file tmp/test.cache -i tmp/model --loss_function logistic -t 2>&1 | grep 'average loss' | sed -e 's/average loss = //g') >> $1
done

for i in {27..32}
do
	vw --cache_file tmp/train.cache -b $i --sparse_weights --loss_function logistic -f tmp/model --ftrl 2>/dev/null;
	echo $i $(vw --sparse_weights --cache_file tmp/test.cache -i tmp/model --loss_function logistic -t 2>&1 | grep 'average loss' | sed -e 's/average loss = //g') >> $1
done
