package main

import (
    "os"
    "log"
    "fmt"
    "strings"
    "unicode"
)

func main() {
    b, err := os.ReadFile("../data/test_1.txt")
    if err != nil { log.Fatal(err) }

    str := string(b)

    for _, line := range strings.Split(str, "\n") {
        for i, char := range line {
            if unicode.IsNumber(char) {
                fmt.Printf("%d: %d\n", i, int(char - '0'))
            }
        }
    }
}
