package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
	"log"
	"math"
)

func day05() {
	inputs := input.Load("5").ToStringArray()

	// part 1
	var passportsId []int
	var id int
	for _, input := range inputs {
		if len(input) != 10 {
			log.Fatal("line with wrong length", len(input))
		}

		id = 0
		for i, letter := range input {
			if letter == 'B' || letter == 'R' {
				id += int(math.Pow(2, float64(9-i)))
			}
		}
		passportsId = append(passportsId, id)
	}
	max := arrays.IntMax(passportsId)
	fmt.Printf("Star 1 : %v\n", max)

	// part 2
	var seat int
	for i := 7; i < max; i++ {
		if !arrays.IntIn(i, passportsId) {
			seat = i
		}
	}
	fmt.Printf("Star 2 : %v\n", seat)
}
