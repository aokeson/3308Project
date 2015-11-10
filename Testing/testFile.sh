#!/bin/bash

oldPath=$(pwd);
newPath=$1;
file=$2;
cd $newPath;
TimeTaken=$({ time ./$file 1> /dev/null 2>> $oldPath/test.stderr ; } 2>&1 | head -n2 | tail -n1 );
cd $oldPath;
if [ -s test.stderr ]
then 
	echo "$file Failed";
	echo "--Begin Error Message--";
	cat test.stderr;
	echo "--End Error Message--";
fi
echo "$TimeTaken";
rm test.stderr;

