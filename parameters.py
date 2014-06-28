import sys
params = {
"type4b_100_16" : "(n=6969 k=5 w*=30 h=453)" ,
"type4b_100_19" : "(n=7308 k=5 w*=29 h=354)" ,
"type4b_120_17" : "(n=7766 k=5 w*=24 h=319)" ,
"type4b_130_21" : "(n=8883 k=5 w*=29 h=416)" ,

"50-12-5" : "(n=144 k=2 w*=15 h=48)" ,
"50-14-5" : "(n=196 k=2 w*=18 h=64)" ,
"50-15-5" : "(n=225 k=2 w*=19 h=76)" ,
"50-16-5" : "(n=256 k=2 w*=21 h=79)" ,
"50-17-5" : "(n=289 k=2 w*=22 h=84)" ,
"50-18-5" : "(n=324 k=2 w*=24 h=84)" ,
"50-19-5" : "(n=361 k=2 w*=25 h=93)" ,
"50-20-5" : "(n=400 k=2 w*=27 h=97)" ,
"75-16-5" : "(n=256 k=2 w*=21 h=73)" ,
"75-17-5" : "(n=289 k=2 w*=22 h=78)" ,
"75-18-5" : "(n=324 k=2 w*=24 h=85)" ,
"75-19-5" : "(n=361 k=2 w*=25 h=89)" ,
"75-20-5" : "(n=400 k=2 w*=27 h=99)" ,
"75-21-5" : "(n=441 k=2 w*=28 h=105)" ,
"75-22-5" : "(n=484 k=2 w*=30 h=107)" ,
"75-26-5" : "(n=676 k=2 w*=36 h=129)" ,
"90-20-5" : "(n=400 k=2 w*=27 h=99)" ,
"90-21-5" : "(n=441 k=2 w*=28 h=106)" ,
"90-22-5" : "(n=484 k=2 w*=30 h=109)" ,
"90-23-5" : "(n=529 k=2 w*=31 h=116)",
"90-30-5" : "(n=900 k=2 w*=42 h=151)" ,
"90-38-5" : "(n=1444 k=2 w*=55 h=203)",
"90-50-5" : "(n=2500 k=2 w*=74 h=312)",

"pedigree1" : "(n=334 k=5 w*=15 h=59)" ,
"pedigree7" : "(n=1068 k=4 w*=28 h=140)" ,
"pedigree9" : "(n=1118 k=4 w*=25 h=123)" ,
"pedigree13" : "(n=1077 k=4 w*=30 h=125)" ,
"pedigree19" : "(n=793 k=5 w*=21 h=107)" ,
"pedigree20" : "(n=437 k=4 w*=20 h=65)" ,
"pedigree23" : "(n=402 k=4 w*=21 h=51)" ,
"pedigree30" : "(n=1289 k=5 w*=20 h=105)" ,
"pedigree31" : "(n=1183 k=5 w*=29 h=115)" ,
"pedigree33" : "(n=798 k=5 w*=24 h=132)" ,
"pedigree37" : "(n=1032 k=4 w*=20 h=72)" ,
"pedigree38" : "(n=724 k=4 w*=16 h=52)" ,
"pedigree39" : "(n=1272 k=4 w*=20 h=77)" ,
"pedigree41" : "(n=1062 k=5 w*=29 h=119)" ,
"pedigree50" : "(n=514 k=4 w*=16 h=54)" ,
"pedigree51" : "(n=1152 k=4 w*=33 h=122)",

"1401.wcsp" : "(n=488 k=3 w*=89 h=293)" ,
"1403.wcsp" : "(n=665 k=3 w*=89 h=287)" ,
"1405.wcsp" : "(n=855 k=3 w*=89 h=304)" ,
"1407.wcsp" : "(n=1057 k=3 w*=89 h=296)" ,
"1502.wcsp" : "(n=209 k=3 w*=6 h=15)" ,
"1504.wcsp" : "(n=605 k=3 w*=19 h=80)" ,
"1506.wcsp" : "(n=940 k=3 w*=61 h=218)" ,
"28.wcsp" : "(n=230 k=3 w*=71 h=132)" ,
"29.wcsp" : "(n=82 k=2 w*=14 h=23)" ,
"404.wcsp" : "(n=100 k=3 w*=19 h=60)" ,
"408.wcsp" : "(n=200 k=3 w*=35 h=84)" ,
"412.wcsp" : "(n=300 k=3 w*=35 h=105)" ,
"414.wcsp" : "(n=364 k=3 w*=81 h=185)" ,
"42.wcsp" : "(n=190 k=3 w*=26 h=80)" ,
"503.wcsp" : "(n=143 k=3 w*=9 h=43)" ,
"505.wcsp" : "(n=240 k=3 w*=22 h=71)" ,
"507.wcsp" : "(n=311 k=3 w*=55 h=165)" ,
"509.wcsp" : "(n=348 k=3 w*=71 h=187)" ,
"54.wcsp" : "(n=67 k=3 w*=11 h=19)" ,
"5.wcsp" : "(n=309 k=3 w*=39 h=137)" ,
"bwt5ac.wcsp" : "(n=431 k=2 w*=62 h=202)" ,
"capa.wcsp" : "(n=1100 k=2 w*=100 h=100)" ,
"capb.wcsp" : "(n=1100 k=2 w*=100 h=100)" ,
"capc.wcsp" : "(n=1100 k=2 w*=100 h=100)" ,
"capmo1.wcsp" : "(n=200 k=2 w*=100 h=100)" ,
"capmo2.wcsp" : "(n=200 k=2 w*=100 h=100)" ,
"capmo3.wcsp" : "(n=200 k=2 w*=100 h=100)" ,
"capmo4.wcsp" : "(n=200 k=2 w*=100 h=100)" ,
"capmo5.wcsp" : "(n=200 k=2 w*=100 h=100)" ,
"CELAR6.wcsp" : "(n=16 k=2 w*=7 h=8)" ,
"driverlog02ac.wcsp" : "(n=301 k=2 w*=45 h=132)" ,
"driverlog04ac.wcsp" : "(n=272 k=2 w*=56 h=132)" ,
"driverlog05ac.wcsp" : "(n=351 k=2 w*=66 h=202)" ,
"driverlog08ac.wcsp" : "(n=408 k=2 w*=90 h=270)" ,
"DSJC125.wcsp" : "(n=125 k=2 w*=61 h=75)" ,
"GEOM30a_3.wcsp" : "(n=30 k=2 w*=6 h=17)" ,
"GEOM30a_4.wcsp" : "(n=30 k=2 w*=6 h=15)" ,
"GEOM30a_5.wcsp" : "(n=30 k=2 w*=6 h=17)" ,
"GEOM40_2.wcsp" : "(n=40 k=2 w*=0 h=0)" ,
"GEOM40_3.wcsp" : "(n=40 k=2 w*=0 h=0)" ,
"GEOM40_4.wcsp" : "(n=40 k=2 w*=0 h=0)" ,
"GEOM40_5.wcsp" : "(n=40 k=2 w*=0 h=0)" ,
"graph05.wcsp" : "(n=100 k=2 w*=24 h=39)" ,
"graph06.wcsp" : "(n=200 k=2 w*=48 h=75)" ,
"graph11.wcsp" : "(n=340 k=2 w*=88 h=122)" ,
"graph13.wcsp" : "(n=458 k=2 w*=122 h=151)" ,
"le450_5a_2.wcsp" : "(n=450 k=2 w*=284 h=311)" ,
"le450_5a_3.wcsp" : "(n=450 k=2 w*=287 h=332)" ,
"le450_5a_4.wcsp" : "(n=450 k=2 w*=291 h=331)" ,
"myciel5g_3.wcsp" : "(n=47 k=2 w*=19 h=22)" ,
"myciel5g_4.wcsp" : "(n=47 k=2 w*=19 h=22)" ,
"myciel5g_5.wcsp" : "(n=47 k=2 w*=19 h=22)" ,
"queen5_5_3.wcsp" : "(n=25 k=2 w*=18 h=20)" ,
"queen5_5_4.wcsp" : "(n=25 k=2 w*=18 h=21)" ,
"rovers02ac.wcsp" : "(n=152 k=2 w*=34 h=54)" ,
"satellite01ac.wcsp" : "(n=79 k=2 w*=19 h=49)" ,
"satellite02ac.wcsp" : "(n=182 k=2 w*=25 h=152)" ,
"scen06.wcsp" : "(n=100 k=2 w*=11 h=30)" ,
"scen07.wcsp" : "(n=200 k=2 w*=16 h=44)" ,
"scen08.wcsp" : "(n=458 k=2 w*=0 h=0)" ,
"zenotravel02ac.wcsp" : "(n=116 k=2 w*=18 h=45)" ,
"zenotravel04ac.wcsp" : "(n=239 k=2 w*=31 h=54)" , 

"6_23_s.binary" :  "(n=237 k=2 w*=16 h=51)" ,
"7_11_s.binary" :  "(n=235 k=2 w*=17 h=52)" ,
"10_16_s.binary" :  "(n=233 k=2 w*=15 h=63)" ,
"11_3_s.binary" :  "(n=232 k=2 w*=18 h=47)" ,
"20_5_s.binary" :  "(n=232 k=2 w*=16 h=51)" ,
"9_24_s.binary" :  "(n=232 k=2 w*=17 h=55)" ,
"10_14_s.binary" :  "(n=231 k=2 w*=15 h=50)" ,
"19_12_s.binary" :  "(n=233 k=2 w*=17 h=56)" ,
"16_18_s.binary" :  "(n=232 k=2 w*=16 h=52)" ,
"7_9_s.binary" :  "(n=233 k=2 w*=16 h=53)" ,
"6_3_s.binary" :  "(n=231 k=2 w*=14 h=52)" ,
"3_20_s.binary" :  "(n=232 k=2 w*=16 h=51)" ,
"19_20_s.binary" :  "(n=232 k=2 w*=16 h=59)" ,
"15_3_s.binary" :  "(n=231 k=2 w*=16 h=59)" ,
"19_4_s.binary" :  "(n=230 k=2 w*=17 h=56)" ,
"9_10_s.binary" :  "(n=230 k=2 w*=16 h=53)" ,
"12_15_s.binary" :  "(n=231 k=2 w*=15 h=56)" ,
"12_20_s.binary" :  "(n=230 k=2 w*=15 h=65)" ,
"11_4_s.binary" :  "(n=230 k=2 w*=16 h=57)" ,
"11_17_s.binary" :  "(n=228 k=2 w*=17 h=60)" ,
"7_12_s.binary" :  "(n=233 k=2 w*=16 h=47)" ,
"18_30_s.binary" :  "(n=229 k=2 w*=16 h=63)" ,
"14_30_s.binary" :  "(n=228 k=2 w*=16 h=64)" ,
"7_15_s.binary" :  "(n=231 k=2 w*=16 h=54)" ,
"14_26_s.binary" :  "(n=228 k=2 w*=15 h=55)" ,
"2_28_s.binary" :  "(n=229 k=2 w*=16 h=50)" ,
"3_16_s.binary" :  "(n=229 k=2 w*=17 h=52)" ,
"1_28_s.binary" :  "(n=230 k=2 w*=15 h=53)" ,
"7_29_s.binary" :  "(n=229 k=2 w*=15 h=52)" ,
"18_21_s.binary" :  "(n=231 k=2 w*=16 h=44)" ,
"19_25_s.binary" :  "(n=228 k=2 w*=17 h=57)" ,
"8_18_s.binary" :  "(n=226 k=2 w*=16 h=56)" ,
"2_17_s.binary" :  "(n=228 k=2 w*=16 h=57)" ,
"2_2_s.binary" :  "(n=227 k=2 w*=15 h=64)" ,
"16_16_s.binary" :  "(n=226 k=2 w*=16 h=57)" ,
"4_30_s.binary" :  "(n=229 k=2 w*=17 h=53)" ,
"13_30_s.binary" :  "(n=227 k=2 w*=15 h=55)" ,
"13_9_s.binary" :  "(n=228 k=2 w*=15 h=58)" ,
"4_24_s.binary" :  "(n=228 k=2 w*=15 h=51)" ,
"13_14_s.binary" :  "(n=221 k=2 w*=17 h=47)" ,
"8_8_s.binary" :  "(n=224 k=2 w*=15 h=57)" ,
"5_3_s.binary" :  "(n=225 k=2 w*=16 h=54)" ,
"12_4_s.binary" :  "(n=224 k=2 w*=16 h=48)" ,
"8_25_s.binary" :  "(n=223 k=2 w*=15 h=59)" ,
"18_1_s.binary" :  "(n=225 k=2 w*=15 h=50)" ,
"18_11_s.binary" :  "(n=222 k=2 w*=17 h=53)" ,

"pdb1a1x" :  "(n=95 k=81 w*=13 h=28)" ,
"pdb1a3c" :  "(n=144 k=81 w*=13 h=35)" ,
"pdb1a62" :  "(n=105 k=81 w*=10 h=31)" ,
"pdb1a7w" :  "(n=53 k=81 w*=6 h=25)" ,
"pdb1a8o" :  "(n=56 k=81 w*=9 h=23)" ,
"pdb1aac" :  "(n=85 k=81 w*=11 h=22)" ,
"pdb1aba" :  "(n=76 k=81 w*=8 h=30)" ,
"pdb1acf" :  "(n=90 k=81 w*=9 h=22)" ,
"pdb1ad2" :  "(n=177 k=81 w*=9 h=33)" ,
"pdb1aho" :  "(n=54 k=81 w*=6 h=20)" ,
"pdb1aie" :  "(n=26 k=81 w*=6 h=15)" ,
"pdb1ail" :  "(n=62 k=81 w*=8 h=25)" ,
"pdb1aiu" :  "(n=92 k=81 w*=10 h=27)" ,
"pdb1ajj" :  "(n=32 k=81 w*=5 h=12)" ,
"pdb1akg" :  "(n=14 k=18 w*=2 h=4)" ,
"pdb1alu" :  "(n=144 k=81 w*=16 h=43)" ,
"pdb1aly" :  "(n=122 k=81 w*=10 h=34)" ,
"pdb1amx" :  "(n=137 k=81 w*=14 h=37)" ,
"pdb1at0" :  "(n=122 k=81 w*=8 h=25)" ,
"pdb1atg" :  "(n=175 k=81 w*=10 h=41)" ,
"pdb1b0b" :  "(n=97 k=81 w*=9 h=29)" ,
"pdb1b0y" :  "(n=60 k=81 w*=8 h=16)" ,
"pdb1b2v" :  "(n=132 k=36 w*=9 h=25)" ,
"pdb1b7d" :  "(n=50 k=81 w*=6 h=17)" ,
"pdb1b8e" :  "(n=133 k=81 w*=12 h=28)" ,
"pdb1bd8" :  "(n=121 k=81 w*=9 h=28)" ,
"pdb1be7" :  "(n=48 k=81 w*=6 h=19)" ,
"pdb1bea" :  "(n=95 k=81 w*=11 h=24)" ,
"pdb1bgc" :  "(n=130 k=81 w*=12 h=37)" ,
"pdb1bhp" :  "(n=39 k=81 w*=6 h=16)" ,
"pdb1bkb" :  "(n=111 k=81 w*=8 h=30)" ,
"pdb1bkr" :  "(n=97 k=81 w*=15 h=32)" ,
"pdb1bm8" :  "(n=85 k=81 w*=12 h=26)" ,
"pdb1bqk" :  "(n=94 k=81 w*=10 h=26)" ,
"pdb1bt0" :  "(n=64 k=81 w*=11 h=22)" ,
"pdb1btn" :  "(n=92 k=81 w*=10 h=31)" ,
"pdb1buo" :  "(n=108 k=81 w*=11 h=32)" ,
"pdb1buu" :  "(n=126 k=81 w*=9 h=40)" ,
"pdb1bv1" :  "(n=134 k=81 w*=11 h=28)" ,
"pdb1bxe" :  "(n=88 k=81 w*=9 h=30)" ,
"pdb1bxv" :  "(n=74 k=81 w*=9 h=23)" ,
"pdb1c3m" :  "(n=113 k=81 w*=12 h=26)" ,
"pdb1c44" :  "(n=98 k=81 w*=12 h=27)" ,
"pdb1c52" :  "(n=99 k=81 w*=14 h=29)" ,
"pdb1c75" :  "(n=47 k=81 w*=6 h=21)" ,
"pdb1c9x" :  "(n=108 k=81 w*=9 h=25)" ,
"pdb1cbs" :  "(n=123 k=81 w*=13 h=29)" ,
"pdb1cc8" :  "(n=66 k=81 w*=10 h=22)" ,
"pdb1cei" :  "(n=75 k=81 w*=11 h=29)" ,
"pdb1cew" :  "(n=96 k=81 w*=9 h=28)" ,
"pdb1cjw" :  "(n=139 k=81 w*=14 h=41)" ,
"pdb1co6" :  "(n=86 k=81 w*=11 h=26)" ,
"pdb1cot" :  "(n=96 k=81 w*=10 h=26)" ,
"pdb1cpq" :  "(n=84 k=81 w*=7 h=20)" ,
"pdb1cqy" :  "(n=91 k=81 w*=9 h=26)" ,
"pdb1ctf" :  "(n=47 k=81 w*=6 h=13)" ,
"pdb1ctj" :  "(n=61 k=81 w*=8 h=18)" ,
"pdb1cuo" :  "(n=104 k=81 w*=11 h=24)" ,
"pdb1cxc" :  "(n=93 k=81 w*=11 h=28)" ,
"pdb1cxy" :  "(n=69 k=81 w*=9 h=19)" ,
"pdb1cyo" :  "(n=78 k=81 w*=9 h=21)" ,
"pdb1dbu" :  "(n=123 k=81 w*=10 h=22)" ,
"pdb1df4" :  "(n=51 k=81 w*=6 h=21)" ,
"pdb1dfx" :  "(n=103 k=81 w*=8 h=30)" ,
"pdb1dg6" :  "(n=131 k=81 w*=14 h=38)" ,
"pdb1di6" :  "(n=154 k=81 w*=14 h=31)" ,
"pdb1dk8" :  "(n=130 k=81 w*=12 h=40)" ,
"pdb1dlw" :  "(n=83 k=81 w*=8 h=23)" ,
"pdb1dly" :  "(n=100 k=81 w*=10 h=25)" ,
"pdb1doi" :  "(n=109 k=81 w*=12 h=28)" ,
"pdb1dqg" :  "(n=118 k=81 w*=13 h=30)" ,
"pdb1duw" :  "(n=241 k=81 w*=9 h=32)" ,
"pdb1dvo" :  "(n=127 k=81 w*=9 h=50)" ,
"pdb1dzo" :  "(n=91 k=81 w*=8 h=26)" ,
"pdb1e29" :  "(n=117 k=81 w*=11 h=29)" ,
"pdb1e3b" :  "(n=139 k=81 w*=15 h=31)" ,
"pdb1e85" :  "(n=91 k=81 w*=8 h=32)" ,
"pdb1ej8" :  "(n=121 k=81 w*=10 h=24)" ,
"pdb1ek0" :  "(n=139 k=81 w*=13 h=36)" ,
"pdb1ekg" :  "(n=103 k=81 w*=11 h=27)" ,
"pdb1en2" :  "(n=65 k=81 w*=5 h=18)" ,
"pdb1esl" :  "(n=140 k=81 w*=15 h=32)" ,
"pdb1etl" :  "(n=9 k=27 w*=1 h=3)" ,
"pdb1etm" :  "(n=10 k=27 w*=1 h=3)" ,
"pdb1etn" :  "(n=9 k=27 w*=1 h=2)" ,
"pdb1euo" :  "(n=157 k=81 w*=14 h=35)" ,
"pdb1ew4" :  "(n=92 k=81 w*=13 h=31)" ,
"pdb1exr" :  "(n=125 k=81 w*=8 h=45)" ,
"pdb1f1e" :  "(n=116 k=81 w*=11 h=41)" ,
"pdb1f4p" :  "(n=112 k=81 w*=10 h=35)" ,
"pdb1f5f" :  "(n=147 k=81 w*=15 h=34)" ,
"pdb1f94" :  "(n=58 k=81 w*=6 h=19)" ,
"pdb1fas" :  "(n=55 k=81 w*=6 h=16)" ,
"pdb1fit" :  "(n=107 k=81 w*=11 h=26)" ,
"pdb1fjj" :  "(n=122 k=81 w*=11 h=34)" ,
"pdb1fk5" :  "(n=66 k=81 w*=6 h=18)" ,
"pdb1fna" :  "(n=75 k=81 w*=6 h=18)" ,
"pdb1fnl" :  "(n=157 k=81 w*=9 h=29)" ,
"pdb1fny" :  "(n=199 k=81 w*=13 h=30)" ,
"pdb1fxd" :  "(n=51 k=81 w*=5 h=17)" ,
"pdb1g2b" :  "(n=55 k=81 w*=7 h=21)" ,
"pdb1g2r" :  "(n=83 k=81 w*=10 h=23)" ,
"pdb1g3p" :  "(n=165 k=81 w*=10 h=33)" ,
"pdb1g6x" :  "(n=44 k=81 w*=7 h=19)" ,
"pdb1g9o" :  "(n=75 k=81 w*=10 h=22)" ,
"pdb1gdv" :  "(n=66 k=81 w*=9 h=18)" ,
"pdb1gmx" :  "(n=86 k=81 w*=9 h=22)" ,
"pdb1gvp" :  "(n=76 k=81 w*=7 h=23)" ,
"pdb1h6h" :  "(n=125 k=81 w*=12 h=34)" ,
"pdb1h75" :  "(n=64 k=81 w*=8 h=24)" ,
"pdb1h98" :  "(n=68 k=81 w*=8 h=19)" ,
"pdb1h9k" :  "(n=108 k=81 w*=7 h=24)" ,
"pdb1hbk" :  "(n=83 k=81 w*=10 h=31)" ,
"pdb1hby" :  "(n=109 k=81 w*=11 h=34)" ,
"pdb1hcz" :  "(n=211 k=81 w*=9 h=34)" ,
"pdb1hg7" :  "(n=56 k=81 w*=6 h=16)" ,
"pdb1hh5" :  "(n=54 k=81 w*=5 h=14)" ,
"pdb1hoe" :  "(n=60 k=81 w*=5 h=16)" ,
"pdb1hpi" :  "(n=57 k=81 w*=7 h=18)" ,
"pdb1huw" :  "(n=152 k=81 w*=15 h=43)" ,
"pdb1hxi" :  "(n=84 k=81 w*=8 h=28)" ,
"pdb1hyp" :  "(n=84 k=81 w*=8 h=28)" ,
"pdb1i27" :  "(n=67 k=81 w*=10 h=28)" ,
"pdb1i5g" :  "(n=122 k=81 w*=13 h=31)" ,
"pdb1i8o" :  "(n=85 k=81 w*=8 h=22)" ,
"pdb1ig5" :  "(n=68 k=81 w*=12 h=26)" ,
"pdb1ijt" :  "(n=107 k=81 w*=13 h=26)" ,
"pdb1iqz" :  "(n=67 k=81 w*=7 h=25)" ,
"pdb1j8e" :  "(n=39 k=81 w*=6 h=12)" ,
"pdb1j98" :  "(n=133 k=81 w*=14 h=32)" ,
"pdb1j9b" :  "(n=122 k=81 w*=12 h=42)" ,
"pdb1jb3" :  "(n=115 k=81 w*=12 h=31)" ,
"pdb1jbe" :  "(n=101 k=81 w*=11 h=29)" ,
"pdb1jer" :  "(n=96 k=81 w*=8 h=24)" ,
"pdb1jhg" :  "(n=88 k=81 w*=8 h=31)" ,
"pdb1jse" :  "(n=103 k=81 w*=11 h=28)" ,
"pdb1k51" :  "(n=57 k=81 w*=5 h=14)" ,
"pdb1kao" :  "(n=148 k=81 w*=15 h=41)" ,
"pdb1kgd" :  "(n=156 k=81 w*=12 h=46)" ,
"pdb1kid" :  "(n=153 k=81 w*=11 h=40)" ,
"pdb1kp6" :  "(n=64 k=81 w*=9 h=20)" ,
"pdb1kth" :  "(n=50 k=81 w*=7 h=20)" ,
"pdb1lit" :  "(n=115 k=81 w*=12 h=23)" ,
"pdb1lki" :  "(n=150 k=81 w*=12 h=33)" ,
"pdb1mho" :  "(n=79 k=81 w*=11 h=25)" ,
"pdb1mjc" :  "(n=54 k=81 w*=7 h=17)" ,
"pdb1mof" :  "(n=46 k=81 w*=4 h=16)" ,
"pdb1msc" :  "(n=106 k=81 w*=5 h=20)" ,
"pdb1ncg" :  "(n=88 k=81 w*=7 h=21)" ,
"pdb1neu" :  "(n=102 k=81 w*=10 h=26)" ,
"pdb1nkd" :  "(n=50 k=81 w*=7 h=22)" ,
"pdb1noa" :  "(n=80 k=81 w*=4 h=21)" ,
"pdb1not" :  "(n=11 k=81 w*=2 h=5)" ,
"pdb1npl" :  "(n=94 k=81 w*=8 h=25)" ,
"pdb1ntn" :  "(n=64 k=81 w*=6 h=15)" ,
"pdb1opc" :  "(n=87 k=81 w*=12 h=32)" ,
"pdb1pbv" :  "(n=170 k=81 w*=11 h=55)" ,
"pdb1pef" :  "(n=17 k=81 w*=6 h=11)" ,
"pdb1pen" :  "(n=13 k=18 w*=2 h=4)" ,
"pdb1piq" :  "(n=29 k=81 w*=4 h=20)" ,
"pdb1plc" :  "(n=82 k=81 w*=8 h=20)" ,
"pdb1puc" :  "(n=92 k=81 w*=10 h=21)" ,
"pdb1qad" :  "(n=91 k=81 w*=11 h=25)" ,
"pdb1qhq" :  "(n=106 k=81 w*=9 h=19)" ,
"pdb1qhv" :  "(n=173 k=81 w*=14 h=38)" ,
"pdb1qjp" :  "(n=106 k=81 w*=10 h=24)" ,
"pdb1qnt" :  "(n=132 k=81 w*=10 h=26)" ,
"pdb1qre" :  "(n=175 k=81 w*=9 h=28)" ,
"pdb1qt9" :  "(n=83 k=81 w*=8 h=19)" ,
"pdb1qto" :  "(n=97 k=81 w*=9 h=20)" ,
"pdb1r69" :  "(n=54 k=81 w*=9 h=19)" ,
"pdb1rb9" :  "(n=42 k=81 w*=7 h=14)" ,
"pdb1rcy" :  "(n=123 k=81 w*=10 h=28)" ,
"pdb1rfs" :  "(n=102 k=81 w*=8 h=24)" ,
"pdb1rh4" :  "(n=21 k=81 w*=4 h=14)" ,
"pdb1ris" :  "(n=88 k=81 w*=10 h=26)" ,
"pdb1rl6" :  "(n=137 k=81 w*=9 h=38)" ,
"pdb1rro" :  "(n=93 k=81 w*=12 h=28)" ,
"pdb1rsy" :  "(n=119 k=81 w*=12 h=28)" ,
"pdb1rzl" :  "(n=65 k=81 w*=5 h=14)" ,
"pdb1sfp" :  "(n=99 k=81 w*=10 h=28)" ,
"pdb1skz" :  "(n=92 k=81 w*=9 h=19)" ,
"pdb1svy" :  "(n=80 k=81 w*=8 h=25)" ,
"pdb1t1d" :  "(n=92 k=81 w*=13 h=31)" ,
"pdb1tfe" :  "(n=121 k=81 w*=14 h=46)" ,
"pdb1thx" :  "(n=97 k=81 w*=9 h=24)" ,
"pdb1tif" :  "(n=66 k=81 w*=10 h=31)" ,
"pdb1tig" :  "(n=76 k=81 w*=10 h=27)" ,
"pdb1tmy" :  "(n=97 k=81 w*=10 h=23)" ,
"pdb1tn3" :  "(n=111 k=81 w*=12 h=26)" ,
"pdb1utg" :  "(n=65 k=81 w*=7 h=23)" ,
"pdb1vfy" :  "(n=63 k=81 w*=8 h=21)" ,
"pdb1vls" :  "(n=119 k=81 w*=9 h=46)" ,
"pdb1vpi" :  "(n=101 k=81 w*=9 h=27)" ,
"pdb1wad" :  "(n=91 k=81 w*=6 h=18)" ,
"pdb1wba" :  "(n=151 k=81 w*=14 h=40)" ,
"pdb1whi" :  "(n=101 k=81 w*=9 h=26)" ,
"pdb1who" :  "(n=80 k=81 w*=9 h=23)" ,
"pdb1xer" :  "(n=85 k=81 w*=8 h=21)" ,
"pdb1xy2" :  "(n=7 k=36 w*=2 h=2)" ,
"pdb1ycc" :  "(n=89 k=81 w*=14 h=31)" ,
"pdb1ypc" :  "(n=56 k=81 w*=7 h=18)" ,
"pdb2cbp" :  "(n=77 k=81 w*=8 h=22)" ,
"pdb2cdv" :  "(n=85 k=81 w*=9 h=24)" ,
"pdb2cy3" :  "(n=96 k=81 w*=6 h=19)" ,
"pdb2e2c" :  "(n=142 k=81 w*=11 h=34)" ,
"pdb2eif" :  "(n=112 k=81 w*=8 h=29)" ,
"pdb2erl" :  "(n=34 k=81 w*=4 h=12)" ,
"pdb2fcb" :  "(n=158 k=81 w*=10 h=31)" ,
"pdb2fcr" :  "(n=143 k=81 w*=14 h=29)" ,
"pdb2fdn" :  "(n=42 k=81 w*=4 h=11)" ,
"pdb2hbg" :  "(n=97 k=81 w*=10 h=22)" ,
"pdb2hft" :  "(n=190 k=81 w*=10 h=39)" ,
"pdb2hts" :  "(n=81 k=81 w*=12 h=27)" ,
"pdb2i1b" :  "(n=140 k=81 w*=14 h=32)" ,
"pdb2igd" :  "(n=50 k=81 w*=6 h=19)" ,
"pdb2ilk" :  "(n=142 k=81 w*=10 h=41)" ,
"pdb2lhb" :  "(n=122 k=81 w*=12 h=33)" ,
"pdb2mcm" :  "(n=80 k=81 w*=4 h=18)" ,
"pdb2ovo" :  "(n=48 k=81 w*=6 h=17)" ,
"pdb2pii" :  "(n=94 k=81 w*=9 h=24)" ,
"pdb2pvb" :  "(n=80 k=81 w*=12 h=27)" ,
"pdb2rhe" :  "(n=92 k=81 w*=6 h=19)" ,
"pdb2rta" :  "(n=88 k=81 w*=9 h=20)" ,
"pdb2sn3" :  "(n=53 k=81 w*=6 h=18)" ,
"pdb2tgi" :  "(n=100 k=81 w*=7 h=24)" ,
"pdb2tir" :  "(n=87 k=81 w*=8 h=31)" ,
"pdb3c2c" :  "(n=89 k=81 w*=12 h=32)" ,
"pdb3cao" :  "(n=84 k=81 w*=5 h=21)" ,
"pdb3cyr" :  "(n=91 k=81 w*=6 h=24)" ,
"pdb3ebx" :  "(n=57 k=81 w*=6 h=20)" ,
"pdb3ezm" :  "(n=88 k=81 w*=3 h=13)" ,
"pdb3il8" :  "(n=64 k=81 w*=8 h=18)" ,
"pdb3kvt" :  "(n=92 k=81 w*=12 h=31)" ,
"pdb3nul" :  "(n=101 k=81 w*=10 h=29)" ,
"pdb3vub" :  "(n=92 k=81 w*=11 h=28)" ,
"pdb451c" :  "(n=62 k=81 w*=9 h=20)" ,
"pdb4rhn" :  "(n=94 k=81 w*=10 h=25)" ,
"pdb5nul" :  "(n=119 k=81 w*=12 h=35)" ,
"pdb7fd1" :  "(n=96 k=81 w*=10 h=23)" 

}

print(params[sys.argv[1]])