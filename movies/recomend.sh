pattern=$1
file=$2

python analysis.py $file $pattern | python compute.py output.csv