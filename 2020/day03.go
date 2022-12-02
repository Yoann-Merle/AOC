package main

import (
	"aoc/input"
	"fmt"
)

func day03() {
	lines := input.Load("3").ToStringArray()

	// part 1
	x := 0
	treeInTheFace := 0
	for _, line := range lines {
		lengthString := len(line)
		relativPos := x % lengthString
		if (string)(line[relativPos]) == "#" {
			treeInTheFace++
		}
		x = 3 + x
	}

	fmt.Printf("Star 1 : %v\n", treeInTheFace)

	// part 2
	factor := 1
	var slopes = [5][2]int{
		{1, 1},
		{3, 1},
		{5, 1},
		{7, 1},
		{1, 2},
	}
	for _, slope := range slopes {
		tree := 0
		x := 0
		i := 0
		for _, line := range lines {
			if i%slope[1] != 0 {
				i++
				continue
			}
			i++
			lengthString := len(line)
			relativPos := x % lengthString
			if (string)(line[relativPos]) == "#" {
				tree++
			}
			x = slope[0] + x
		}
		factor = factor * tree
	}
	fmt.Printf("Star 2 : %v\n", factor)
}
