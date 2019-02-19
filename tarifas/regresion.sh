file=$1

if [ $# -eq 0 ]; then
    echo 'Filename argument required'
    echo 'Example: ./regresion.sh filename.csv'
    exit 0
fi
if ! [ -e $file ]; then
    echo "File [$file] does not exist"
    exit 0
fi

printf "Analysing [$file]\n\n"
cut -d , -f 2,3,17 $file | python format.py | ./timediff | python analysis.py