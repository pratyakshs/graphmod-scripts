#!/bin/bash
# for prob in "pedigree1" "pedigree20" "pedigree33" "pedigree39" "pedigree23"
# for prob in "pedigree1" "pedigree20" "pedigree33" "pedigree39" "pedigree23"

echo "Comparison of heuristics with different algorithms on 8 WCSP benchmarks, across all time bounds, all i-bounds" 
echo -e "Algorithm\tJGLP\tMBE-MM\tMBE\tTotal"
# for heur in "match" "mbe" "jglp"
for algo in "waobb" "braobb" "aow" "araobf" "wbraobb"
do
	jglp=0
	match=0
	mbe=0
for prob in "1403.wcsp" "1504.wcsp" "404.wcsp" "505.wcsp" "driverlog02ac.wcsp" "graph05.wcsp" "zenotravel02ac.wcsp" "zenotravel04ac.wcsp"
# for prob in "pedigree1" "pedigree20" "pedigree23" "pedigree33" "pedigree39"
# for prob in "50-12-5" "50-15-5" "50-16-5" "50-17-5" "50-18-5" "50-19-5" "50-20-5" "75-21-5" "75-22-5" "75-26-5" "90-20-5" "90-21-5" "90-30-5" "90-38-5" "90-50-5"

do

for t in 10 60 600 3600 10800 21600

	do
	for i in 2 4 6 8 10 14 18

		do
				c=`python3 scripts/compare.py extracted/jglp-${prob}-i${i}-${algo}-t${t}.ext extracted/match-${prob}-i${i}-${algo}-t${t}.ext extracted/mbe-${prob}-i${i}-${algo}-t${t}.ext`
				if [ $c -eq 0 ]
				then
					jglp=$((${jglp}+1))
				elif [ $c -eq 1 ]
				then
					match=$((${match}+1))
				elif [ $c -eq 2 ]
				then
					mbe=$((${mbe}+1))
				fi
			done
		done
	done
	echo -e "${algo}\t\t${jglp}\t${match}\t${mbe}\t$((${jglp}+${match}+${mbe}))"
done


