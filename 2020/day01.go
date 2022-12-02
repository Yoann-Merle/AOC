package main

import "fmt"
import "aoc/input"

func day01() {
	input := input.Load("1").ToIntArray()
	// part 1
	for i, n := range input {
		for _, n2 := range input[i:] {
			if n+n2 == 2020 {
				fmt.Printf("Star 1 : %v\n", n*n2)
			}
		}
	}

	// part 2
	for i, n := range input {
		for j, n2 := range input[i:] {
			for _, n3 := range input[j:] {
				if n+n2+n3 == 2020 {
					fmt.Printf("Star 2 : %v\n", n*n2*n3)
				}
			}
		}
	}
}
