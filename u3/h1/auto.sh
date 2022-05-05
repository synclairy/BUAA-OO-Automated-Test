a=1
while [ $a -ne 51 ]
do
	python3 social_generate.py
	echo '----------Random test data is generated.----------'
		cat stdin.txt | time java -jar ./xh.jar > stdout1.txt
		cat stdin.txt | time java -jar ./dhy.jar > stdout2.txt
		python3 check.py > ./log/result_$a.txt
	echo "-----------------Test case $a over-----------------"
	cp stdin.txt ./inputs/stdin_$a.txt
	cp stdout1.txt ./outputs/stdout_1_$a.txt
	cp stdout2.txt ./outputs/stdout_2_$a.txt
	echo "--------------------All stored.--------------------"
	a=$[$a+1]
done
