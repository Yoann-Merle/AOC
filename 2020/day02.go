package main

import (
	"aoc/input"
	"fmt"
	"strconv"
	"strings"
)

func day02() {
	lines := input.Load("2").ToStringArray()

	//part 1
	valid := 0
	for _, line := range lines {
		split := strings.Split(line, ":")
		rules := strings.Split(split[0], " ")
		targetLetter := rules[1]
		c := strings.Count(split[1], targetLetter)
		minAndMax := strings.Split(rules[0], "-")
		min, _ := strconv.Atoi(minAndMax[0])
		max, _ := strconv.Atoi(minAndMax[1])
		if c >= min && c <= max {
			valid++
		}
	}
	fmt.Printf("Star 1 : %v\n", valid)

	// part 2
	valid = 0
	for _, line := range lines {
		split := strings.Split(line, ":")
		rules := strings.Split(split[0], " ")
		targetLetter := rules[1]
		targetPositions := strings.Split(rules[0], "-")
		targetPos1, _ := strconv.Atoi(targetPositions[0])
		targetPos2, _ := strconv.Atoi(targetPositions[1])
		count := 0
		// No need to decrement 1. There is a space at the begining of each string
		if string(split[1][targetPos1]) == targetLetter {
			count++
		}
		if string(split[1][targetPos2]) == targetLetter {
			count++
		}
		if count == 1 {
			valid++
		}
	}

	fmt.Printf("Star 2 : %v\n", valid)
}
