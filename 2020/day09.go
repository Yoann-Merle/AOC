package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
	"log"
)

func day09() {
	inputs := input.Load("9").ToIntArray()
	block := 25
	var encodErr int
	for i := block; i < len(inputs); i++ {
		b := i - block
		if !sumOfTwoBefore(inputs[b:i], inputs[i]) {
			encodErr = i
			break
		}
	}
	fmt.Printf("Star 1 : %v\n", inputs[encodErr])
	consecNum := findConsecutivSum(inputs, encodErr)
	fmt.Printf("Star 2 : %v\n", arrays.IntMin(consecNum)+arrays.IntMax(consecNum))
}

func findConsecutivSum(table []int, ind int) []int {
	for start := 0; start < ind; start++ {
		sum := table[start]
		for i := start + 1; i < ind; i++ {
			sum += table[i]
			if sum > table[ind] {
				break
			}
			if sum == table[ind] {
				return table[start:i]
			}
		}
	}
	return nil
}

func sumOfTwoBefore(table []int, sum int) bool {
	if len(table) != 25 {
		log.Fatal("Table length invalid")
	}
	for i, a := range table {
		for _, b := range table[i:] {
			if a+b == sum {
				return true
			}
		}
	}

	return false
}
