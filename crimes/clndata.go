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
