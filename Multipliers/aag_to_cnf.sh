for file in aags/*
do
	IFS='/' read -ra FNAME <<< "$file"
	filename=${FNAME[${#FNAME[@]}-1]}
	#echo $file
	IFS='.' read -ra NAME <<< "$filename"
	nameonly=${NAME[0]}
	echo $file
	echo $filename
	echo $nameonly
	# for i in 1 2 3 4 5
	# do
	outname=$nameonly'_randinp_1.cnf'
	python3 ../Scripts/circuit2cnf_with_outp.py -n $file -o ./cnfs/$outname
	# done
done