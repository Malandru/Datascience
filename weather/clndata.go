package main

import (
	"encoding/csv"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"strings"
)

func noEmptyElem(line []string) bool {
	i := 0
	for i < len(line) {
		if line[i] == "" {
			return false
		}
		i++
	}
	return true
}

func getMonth(num string) string {
	switch num {
	case "01":
		return "January"
	case "02":
		return "February"
	case "03":
		return "March"
	case "04":
		return "April"
	case "05":
		return "May"
	case "06":
		return "June"
	case "07":
		return "July"
	case "08":
		return "August"
	case "09":
		return "September"
	case "10":
		return "October"
	case "11":
		return "November"
	case "12":
		return "December"
	}
	return num
}

func main() {
	if len(os.Args) != 2 {
		fmt.Println("[Filename argument missing]")
		fmt.Println("Usage: clndt file")
		fmt.Println("---------------------------")
		fmt.Println("Example: clndt crimes.csv")
	}

	file, err := ioutil.ReadFile(os.Args[1])
	if err != nil {
		fmt.Print(err)
	}

	r := csv.NewReader(strings.NewReader(string(file)))

	for {
		record, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}

		if noEmptyElem(record) {
			aux := record[1]
			record[1] = getMonth(aux[:2]) + aux[2:]
			i := 0
			size := len(record)
			for i < size {
				fmt.Print("\"", record[i], "\"")
				if i+1 < size {
					fmt.Print(",")
				}
				i++
			}
			fmt.Println()
		}
		// fmt.Println(record)
	}
}
