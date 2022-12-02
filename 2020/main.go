package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	day20()
	fmt.Println("Execution duration: " + time.Now().Sub(start).String())
}
