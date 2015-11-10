#!/bin/bash

dircs=(../siteEnv/ ../);
files=(index.py hourScrape.py);
for ind in `seq 0 1`; do
	name=$(./testFile.sh ${dircs[$ind]} ${files[$ind]});
	echo "${files[$ind]}: $name";
done

