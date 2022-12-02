package main

import (
	"aoc/input"
	"fmt"
)

func day11() {
	matrice_input := input.Load("11").ToDoubleByteArray()

	var occupied int
	matrice := make([][]byte, len(matrice_input))
	copy(matrice, matrice_input)
	for {
		nextState := nextState(matrice)
		if equal(nextState, matrice) {
			occupied = countAllOccupied(matrice)
			break
		}
		matrice = nextState
	}
	fmt.Printf("Star 1 : %v\n", occupied)

	copy(matrice, matrice_input)
	for {
		nextState := nextStatePart2(matrice)
		if equal(nextState, matrice) {
			occupied = countAllOccupied(matrice)
			break
		}
		matrice = nextState
	}
	fmt.Printf("Star 2 : %v\n", occupied)
}

func nextState(origin [][]byte) [][]byte {
	next := make([][]byte, len(origin))
	for i, line := range origin {
		line_next := make([]byte, len(line))
		next[i] = line_next
		for j, letter := range line {
			if string(letter) == "L" && countAdjOccupied(j, i, origin) == 0 {
				next[i][j] = []byte("#")[0]
			} else if string(letter) == "#" && countAdjOccupied(j, i, origin) >= 4 {
				next[i][j] = []byte("L")[0]
			} else {
				next[i][j] = origin[i][j]
			}
		}
	}

	return next
}

func nextStatePart2(origin [][]byte) [][]byte {
	next := make([][]byte, len(origin))
	for i, line := range origin {
		line_next := make([]byte, len(line))
		next[i] = line_next
		for j, letter := range line {
			if string(letter) == "L" && countVisuOccupied(j, i, origin) == 0 {
				next[i][j] = []byte("#")[0]
			} else if string(letter) == "#" && countVisuOccupied(j, i, origin) >= 5 {
				next[i][j] = []byte("L")[0]
			} else {
				next[i][j] = origin[i][j]
			}
		}
	}

	return next
}

func equal(matrice1 [][]byte, matrice2 [][]byte) bool {
	for i, line := range matrice1 {
		for j, letter := range line {
			if letter != matrice2[i][j] {
				return false
			}
		}
	}
	return true

}
func countAllOccupied(matrice [][]byte) int {
	nb := 0
	for _, line := range matrice {
		for _, letter := range line {
			if string(letter) == "#" {
				nb++
			}
		}
	}

	return nb
}
func countAdjOccupied(i int, j int, matrice [][]byte) int {
	maxX := getX(matrice)
	maxY := getY(matrice)
	occupied := 0
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			if x == 0 && y == 0 {
				continue
			}
			if i+x >= 0 && i+x <= maxX-1 && j+y >= 0 && j+y <= maxY-1 {
				if string(matrice[j+y][i+x]) == "#" {
					occupied++
				}
			}
		}
	}

	return occupied
}

func getX(list [][]byte) int {
	var max int
	for i, b := range list {
		if i == 0 {
			max = len(b)
		} else if len(b) > max {
			max = len(b)
		}
	}
	return max
}

func getY(list [][]byte) int {
	return len(list)
}

func countVisuOccupied(i int, j int, matrice [][]byte) int {
	maxX := getX(matrice)
	maxY := getY(matrice)
	occupied := 0
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			if x == 0 && y == 0 {
				continue
			}
			if searchDirection(i, j, x, y, matrice, maxX, maxY) {
				occupied++
			}
		}
	}

	return occupied
}

func searchDirection(i, j, x, y int, matrice [][]byte, maxX, maxY int) bool {
	for i+x >= 0 && i+x <= maxX-1 && j+y >= 0 && j+y <= maxY-1 {
		if string(matrice[j+y][i+x]) == "#" {
			return true
		}
		if string(matrice[j+y][i+x]) == "L" {
			return false
		}
		i += x
		j += y
	}

	return false
}
