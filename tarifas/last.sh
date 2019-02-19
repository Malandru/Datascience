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

printf "Analysing file [$file]\n\n"
cut -d , -f 5,17 $file --output-delimiter=' ' | ./process 0 100 0 200 | python analysis.py