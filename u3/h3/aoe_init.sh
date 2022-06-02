a=0
mkdir inputs
mkdir outputs
mkdir log
mkdir hackjars
while [ $a -ne $1 ]
do
	a=$[$a+1]
	mkdir log/$a 
    mkdir outputs/$a 
done
mkdir outputs/0/
