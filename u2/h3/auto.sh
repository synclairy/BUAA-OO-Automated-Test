a=1
while [ $a -ne 30 ]
do
	b=1
	python3 Generate.py
	echo '----------Random test data is generated.----------'
	echo '----------------Running all code.----------------'
	echo '----------------Running all code.----------------' > ./log/log_$a.txt
	while [ $b -ne 8 ]
	do
		echo ""
		echo "" >> ./log/log_$a.txt
		echo "------------------Testing $b.jar------------------"
		echo "------------------Testing $b.jar------------------" >> ./log/log_$a.txt
		./datainput_student_darwin | java -jar ./Hack/$b.jar > stdout.txt
		echo '------------------Output is over.-----------------'
		cat stdin.txt > ./output/$b/all_$a.txt
		echo 'end' >> ./output/$b/all_$a.txt
		cat stdout.txt >> ./output/$b/all_$a.txt
		echo '----------------Checking output.-----------------'
		cat ./output/$b/all_$a.txt | java Check 
		cat ./output/$b/all_$a.txt | java Check >> ./log/log_$a.txt
		echo "------------------$b.jar tested------------------" >> ./log/log_$a.txt
		echo ""
		b=$[$b+1]
	done
	echo "-----------------Test case $a over-----------------"
	echo ""
	a=$[$a+1]
done
