package main

import (
	"aoc/input"
	"fmt"
)

type coord struct {
	x int
	y int
}

func day24() {
	input_ := input.Load("24").ToStringArray()
	listCoord := make([]coord, 0)

	// day 1
	for _, l := range input_ {
		x, y := getCoordonate(l)
		present := false
		for i, p := range listCoord {
			if p.x == x && p.y == y {
				present = true
				listCoord = append(listCoord[:i], listCoord[i+1:]...)
			}
		}
		if !present {
			listCoord = append(listCoord, coord{x: x, y: y})
		}
	}
	fmt.Printf("Star 1: %v\n", len(listCoord))
}

func getCoordonate(instruct string) (int, int) {
	x := 0
	y := 0
	for i := 0; i < len(instruct); {
		if instruct[i] == 'w' || instruct[i] == 'e' {
			if instruct[i] == 'e' {
				x += 2
			} else {
				x -= 2
			}
			i += 1
			continue
		}

		if instruct[i] == 's' || instruct[i] == 'n' {
			if instruct[i] == 'n' {
				y += 1
			} else {
				y -= 1
			}
			if instruct[i+1] == 'e' {
				x += 1
			} else {
				x -= 1
			}
			i += 2
		}
	}

	return x, y
}
