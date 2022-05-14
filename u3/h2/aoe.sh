a=0
while [ $a -ne $3 ]
do
	a=$[$a+1]
	python3 social_generate.py
	b=0
	echo '----------Random test data is generated.----------'
	cat stdin.txt | time java -jar ./$1.jar > stdout1.txt
	while [ $b -ne $2 ]
	do
		b=$[$b+1]
		cat stdin.txt | time java -jar ./hackjars/$b.jar > stdout2.txt
		python3 check.py > ./log/$b/result_$a.txt
		cp stdout2.txt ./outputs/$b/stdout_$a.txt
		echo "--------------$b.jar tested--------------"
		echo ''
	done
	echo "-----------------Test case $a over-----------------"
	cp stdin.txt ./inputs/stdin_$a.txt
	cp stdout1.txt ./outputs/0/stdout_$a.txt
	echo "--------------------All stored.--------------------"
done
