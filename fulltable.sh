weight_sched="sqrt"
den=4
del=0.1
wt=64

temp_file="~temp"$RANDOM

echo "\documentclass{article}"
echo "\usepackage[margin=0.15in]{geometry}"

echo "\usepackage{multirow}"
echo "\usepackage[table]{xcolor}"
echo "\begin{document}"

for problem in $*
do
	echo "\section{${problem}}" >> $temp_file
	j=0
	for i in 18 14 10 8 6 4 2
	do
		if [ -e stdout/jglp/${problem}_i$i-braobb-sqrt-den4-del0.1_64-withTies.out.txt ]
		then

			if grep -q "Mini bucket finished" stdout/jglp/${problem}_i$i-braobb-sqrt-den4-del0.1_64-withTies.out.txt 
			then
				echo "\subsection{i=$i}" >>$temp_file
	
				echo "\begin{tabular}{|r|c|c|c|c|c|c|c|c|}" >> $temp_file
				echo "\hline" >> $temp_file
			
				echo " Algorithm & & t = 10s & t = 60s & t = 600s & t = 3600s & t = 10800s & t = 21600s \\\\" >> $temp_file
				echo "\hline" >> $temp_file
				./scripts/rawtable.sh jglp $problem $i $weight_sched $den $del $wt $temp_file
				echo "\end{tabular}" >> $temp_file
				echo "\newline" >> $temp_file
				echo "\newline" >> $temp_file
				echo "\newline" >> $temp_file
				j=$(($j+1))
			fi
		fi
	done
	echo "\newpage" >>$temp_file
done
cat $temp_file | sed 's/ARAOBF/wR-AOBF/g' | sed 's/AOW/wAOBF/g' | sed 's/WAOBB/wAOBB/g' | sed 's/WBRAOBB/wBRAOBB/g' | sed 's/_/\\_/g'
rm $temp_file
echo "\end{document}"
