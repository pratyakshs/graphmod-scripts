#!/bin/bash
# for prob in "50-12-5" "50-15-5" "50-16-5" "50-17-5" "50-18-5" "50-19-5" "50-20-5" "75-21-5" "75-22-5" "75-26-5" "90-20-5" "90-21-5" "90-30-5" "90-38-5" "90-50-5"
# for prob in "pedigree1" "pedigree13" "pedigree19" "pedigree20" "pedigree23" "pedigree30" "pedigree31" "pedigree33" "pedigree37" "pedigree38" "pedigree39" "pedigree41" "pedigree50" "pedigree51" "pedigree7" "pedigree9" 
# for prob in "1403.wcsp" "1504.wcsp" "404.wcsp" "505.wcsp" "driverlog02ac.wcsp" "graph05.wcsp" "zenotravel02ac.wcsp" "zenotravel04ac.wcsp"
# for prob in "pedigree1" "pedigree20" "pedigree33" "pedigree39" "pedigree23"
# for prob in  pdb1hyp pdb2ovo pdb1noa pdb1mjc pdb1j8e pdb1rb9 pdb1pef pdb1fxd pdb1b2v pdb1ajj pdb2mcm pdb2erl pdb2fdn pdb1not pdb1xy2 pdb1pen pdb1etm pdb1akg pdb1etn pdb1etl 
for prob in pedigree13 pedigree19 pedigree1 pedigree20 pedigree23 pedigree30 pedigree31 pedigree33 pedigree37 pedigree38 pedigree39 pedigree41 pedigree50 pedigree51 pedigree7 pedigree9
do
	for heur in "match" "jglp" "mbe"
	do
		for i in 2 4 6 8 10 14 18
		do
			for algo in "araobf" "aow" "braobb" "wbraobb" "waobb"
			do
				python3 scripts/extract.py stdout/$heur/${prob}_i$i-${algo}-sqrt-den4-del0.1_64-withTies.out.txt $heur ${prob} ${i} ${algo}
			done
		done
	done
done
