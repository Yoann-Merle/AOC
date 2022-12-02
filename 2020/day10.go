package main

import (
	"aoc/input"
	"fmt"
	"sort"
)

func day10() {
	inputs := input.Load("10").ToIntArray()
	sort.Ints(inputs)

	// part 1
	jolt := 0
	three_joltDelta := 1
	one_joltDelta := 0
	for i := 0; i < len(inputs); i++ {
		if inputs[i] == jolt+1 {
			jolt++
			one_joltDelta++
		}
		if inputs[i] == jolt+3 {
			three_joltDelta++
		}
		jolt = inputs[i]
	}
	fmt.Printf("Star 1: %v\n", one_joltDelta*three_joltDelta)

	// part 2
	possArrang := make([]int, len(inputs))
	for i := 0; i <= 3; i++ {
		if inputs[i] <= 3 {
			possArrang[i] = 1
		}
	}

	for i := 0; i < len(inputs); i++ {
		for j := 1; j <= 3; j++ {
			if i+j < len(inputs) {
				if inputs[i+j] <= inputs[i]+3 {
					possArrang[i+j] += possArrang[i]
				}
			}
		}
	}
	fmt.Printf("Star 2: %v\n", possArrang[len(possArrang)-1])
}
