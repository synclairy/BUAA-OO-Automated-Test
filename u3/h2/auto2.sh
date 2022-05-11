a=1
while [ $a -ne $2 ]
do
	python3 social_generate.py
	echo '----------Random test data is generated.----------'
	cat stdin.txt | time java -jar ./xh.jar > stdout1.txt
	cat stdin.txt | time java -jar ./$1.jar > stdout2.txt
	python3 check.py > ./log/result_$a.txt
	cp stdin.txt ./inputs/stdin_$a.txt
	cp stdout1.txt ./outputs/xh/stdout_$a.txt
	cp stdout2.txt ./outputs/partner/stdout_$a.txt
	echo "-----------------Test case $a over-----------------"
	echo "--------------------All stored.--------------------"
	a=$[$a+1]
done
