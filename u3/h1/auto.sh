a=1
while [ $a -ne 11 ]
do
	python3 social_generate.py
	b=1
	echo '----------Random test data is generated.----------'
	cat stdin.txt | time java -jar ./xh.jar > stdout1.txt
	while [ $b -ne 8 ]
	do
		cat stdin.txt | time java -jar ./hackjars/$b.jar > stdout2.txt
		python3 check.py > ./log/$b/result_$a.txt
		cp stdout2.txt ./outputs/$b/stdout_$a.txt
		echo "--------------$b.jar tested--------------"
		b=$[$b+1]
		echo ''
	done
	echo "-----------------Test case $a over-----------------"
	cp stdin.txt ./inputs/stdin_$a.txt
	cp stdout1.txt ./outputs/stdout_$a.txt
	echo "--------------------All stored.--------------------"
	a=$[$a+1]
done
