pattern=$1
file=$2

if [ $pattern -ge 0 2>/dev/null ]
then
    year=$pattern
    python analysis.py $file $year
else
    python analysis.py $file $pattern | wc -l
fi