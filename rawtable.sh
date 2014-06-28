#!/bin/bash

# $1 = heuristic. mbe or match or jglp
# $2 = problem instance. eg. pedigree1 or 1403.wcsp etc.
# $3 = i bound, eg 2, 4, 18 etc
# $4 = weight update policy. eg subtract or sqrt
# $5 = denominator. eg 0.1 or 4
# $6 = delta. eg 0.1 or 4
# $7 = initial weight. eg 8, 64 etc

h=$1
if [ $h == "mbe" ]
then 
	h="mplp"
fi

filename=$1'-'$2'_i'$3'-'$4'-''den'$5'-''del'$6'_'$7'.out'


echo "\multicolumn{8}{|c|}{\Large $2 $(python3 scripts/parameters.py $2) } \\\\" >> $filename
echo "\hline" >> $filename
echo "\multicolumn{8}{|c|}{\Large JGLP heuristic, i-bound = $3} \\\\" >> $filename
echo "\hline" >> $filename

# for i in "braobb"
# do	
# 	echo "\multirow{5}{*}{`echo "${i^^}(MBE-MM)"`}" >> $filename
# 	echo `python3 scripts/parsebraobb.py stdout/match/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
# 	echo "" >> $filename
# done
# 
# for i in "aow"
# do	
# 	echo "\multirow{5}{*}{`echo "${i^^}(MBE-MM)"`}" >> $filename
# 	echo `python3 scripts/parse.py stdout/match/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
# 	echo "" >> $filename
# done
# 
# for i in "braobb"
# do	
# 	echo "\multirow{5}{*}{`echo "${i^^}(JGLP)"`}" >> $filename
# 	echo `python3 scripts/parsebraobb.py stdout/jglp/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
# 	echo "" >> $filename
# done
# 
# for i in "aow"
# do	
# 	echo "\multirow{5}{*}{`echo "${i^^}(JGLP)"`}" >> $filename
# 	echo `python3 scripts/parse.py stdout/jglp/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
# 	echo "" >> $filename
# done

for i in "braobb"
do	
	echo "\multirow{5}{*}{`echo "${i^^}"`}" >> $filename
	echo `python3 scripts/parsebraobb.py stdout/jglp/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
	echo "" >> $filename
done
for i in "aow" "araobf" "waobb" "wbraobb"
do	
	echo "\multirow{5}{*}{`echo "${i^^}"`}" >> $filename
	echo `python3 scripts/parse.py stdout/jglp/$2_i$3-$i-$4-den$5-del$6_$7-withTies.out.txt` >> $filename
	echo "" >> $filename
done


python3 scripts/multi_highlight.py $filename $2 > ${filename}2
# cat $filename > ${filename}2

if [ $# == 8 ]
then
	cat ${filename}2 >> $8
#	cat ${filename} >> $8
	rm -f ${filename}
 	rm -f  ${filename}2
fi

