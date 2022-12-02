package main

import (
	"aoc/input"
	"fmt"
)

type point struct {
	x int
	y int
	z int
}

type hyperpoint struct {
	x int
	y int
	z int
	w int
}

type cube struct {
	points map[int]map[int]map[int]int
	minX   int
	minY   int
	minZ   int
	maxX   int
	maxY   int
	maxZ   int
}

type hypercube struct {
	points map[int]map[int]map[int]map[int]int
	minX   int
	maxX   int
	minY   int
	maxY   int
	minZ   int
	maxZ   int
	minW   int
	maxW   int
}

func day17() {
	input := input.Load("17").ToDoubleByteArray()

	// part 1
	cube := cube{points: make(map[int]map[int]map[int]int)}
	for y, line := range input {
		for x, v := range line {
			if v == '#' {
				point := point{x: x, y: y, z: 0}
				cube.applyState(point, 1)
			}
		}
	}

	//part 1
	for c := 1; c <= 6; c++ {
		cube = cube.nextState()
	}
	fmt.Printf("Star 1 : %v\n", cube.mesure())

	// part 2
	hypercube := hypercube{points: make(map[int]map[int]map[int]map[int]int)}
	for y, line := range input {
		for x, v := range line {
			if v == '#' {
				point := hyperpoint{x: x, y: y, z: 0, w: 0}
				hypercube.applyState(point, 1)
			}
		}
	}
	for c := 1; c <= 6; c++ {
		hypercube = hypercube.nextState()
	}
	fmt.Printf("Star 2 : %v\n", hypercube.mesure())
}

func (c *cube) show() {
	for z := c.minZ; z <= c.maxZ; z++ {
		fmt.Printf("\nz:%v", z)
		for y := c.minY; y <= c.maxY; y++ {
			fmt.Printf("\n")
			for x := c.minX; x <= c.maxX; x++ {
				if v, ok := c.points[x][y][z]; ok && v != 0 {
					fmt.Printf("#")
				} else {
					fmt.Printf(".")
				}
			}
		}
	}
	fmt.Printf("\n")
}

func (c *hypercube) show() {
	for w := c.minW; w <= c.maxW; w++ {
		for z := c.minZ; z <= c.maxZ; z++ {
			fmt.Printf("\nz:%v", z)
			for y := c.minY; y <= c.maxY; y++ {
				fmt.Printf("\n")
				for x := c.minX; x <= c.maxX; x++ {
					if v, ok := c.points[x][y][z][w]; ok && v != 0 {
						fmt.Printf("#")
					} else {
						fmt.Printf(".")
					}
				}
			}
		}
	}
	fmt.Printf("\n")
}

func (c *hypercube) applyState(p hyperpoint, state int) {
	if _, ok := c.points[p.x]; !ok {
		c.points[p.x] = make(map[int]map[int]map[int]int)
	}
	if _, ok := c.points[p.x][p.y]; !ok {
		c.points[p.x][p.y] = make(map[int]map[int]int)
	}
	if _, ok := c.points[p.x][p.y][p.z]; !ok {
		c.points[p.x][p.y][p.z] = make(map[int]int)
	}
	c.points[p.x][p.y][p.z][p.w] = state

	if p.x >= c.maxX {
		c.maxX = p.x + 1
	}
	if p.x <= c.minX {
		c.minX = p.x - 1
	}
	if p.y >= c.maxY {
		c.maxY = p.y + 1
	}
	if p.y <= c.minY {
		c.minY = p.y - 1
	}
	if p.z >= c.maxZ {
		c.maxZ = p.z + 1
	}
	if p.z <= c.minZ {
		c.minZ = p.z - 1
	}
	if p.w >= c.maxW {
		c.maxW = p.w + 1
	}
	if p.w <= c.minW {
		c.minW = p.w - 1
	}
}
func (c *cube) applyState(p point, state int) {
	if _, ok := c.points[p.x]; !ok {
		c.points[p.x] = make(map[int]map[int]int)
	}
	if _, ok := c.points[p.x][p.y]; !ok {
		c.points[p.x][p.y] = make(map[int]int)
	}
	c.points[p.x][p.y][p.z] = state

	if p.x >= c.maxX {
		c.maxX = p.x + 1
	}
	if p.x <= c.minX {
		c.minX = p.x - 1
	}
	if p.y >= c.maxY {
		c.maxY = p.y + 1
	}
	if p.y <= c.minY {
		c.minY = p.y - 1
	}
	if p.z >= c.maxZ {
		c.maxZ = p.z + 1
	}
	if p.z <= c.minZ {
		c.minZ = p.z - 1
	}
}

func (c cube) mesure() int {
	count := 0
	for x := c.minX; x <= c.maxX; x++ {
		for y := c.minY; y <= c.maxY; y++ {
			for z := c.minZ; z <= c.maxZ; z++ {
				if v, ok := c.points[x][y][z]; ok && v != 0 {
					count++
				}
			}
		}
	}

	return count
}

func (c hypercube) mesure() int {
	count := 0
	for x := c.minX; x <= c.maxX; x++ {
		for y := c.minY; y <= c.maxY; y++ {
			for z := c.minZ; z <= c.maxZ; z++ {
				for w := c.minW; w <= c.maxW; w++ {
					if v, ok := c.points[x][y][z][w]; ok && v != 0 {
						count++
					}
				}
			}
		}
	}

	return count
}
func (c cube) countNextTo(p point) int {
	count := 0
	for x := -1; x <= 1; x++ {
		for y := -1; y <= 1; y++ {
			for z := -1; z <= 1; z++ {
				if x != 0 || y != 0 || z != 0 {
					if v, ok := c.points[p.x+x][p.y+y][p.z+z]; ok && v != 0 {
						count++
					}
				}
			}
		}
	}

	return count
}

func (c hypercube) countNextTo(p hyperpoint) int {
	count := 0
	for w := -1; w <= 1; w++ {
		for x := -1; x <= 1; x++ {
			for y := -1; y <= 1; y++ {
				for z := -1; z <= 1; z++ {
					if x != 0 || y != 0 || z != 0 || w != 0 {
						if v, ok := c.points[p.x+x][p.y+y][p.z+z][p.w+w]; ok && v != 0 {
							count++
						}
					}
				}
			}
		}
	}

	return count
}

func (c cube) nextState() cube {
	nextCube := cube{points: make(map[int]map[int]map[int]int)}
	for x := c.minX; x <= c.maxX; x++ {
		for y := c.minY; y <= c.maxY; y++ {
			for z := c.minZ; z <= c.maxZ; z++ {
				count := c.countNextTo(point{x: x, y: y, z: z})
				if v, ok := c.points[x][y][z]; ok && v == 1 {
					if count < 2 || count > 3 {
						nextCube.applyState(point{x: x, y: y, z: z}, 0)
					} else {
						nextCube.applyState(point{x: x, y: y, z: z}, 1)
					}
				} else {
					if count == 3 {
						nextCube.applyState(point{x: x, y: y, z: z}, 1)
					} else {
						nextCube.applyState(point{x: x, y: y, z: z}, 0)
					}
				}
			}
		}
	}
	return nextCube
}

func (c hypercube) nextState() hypercube {
	nextCube := hypercube{points: make(map[int]map[int]map[int]map[int]int)}
	for x := c.minX; x <= c.maxX; x++ {
		for y := c.minY; y <= c.maxY; y++ {
			for z := c.minZ; z <= c.maxZ; z++ {
				for w := c.minW; w <= c.maxW; w++ {
					count := c.countNextTo(hyperpoint{x: x, y: y, z: z, w: w})
					if v, ok := c.points[x][y][z][w]; ok && v == 1 {
						if count < 2 || count > 3 {
							nextCube.applyState(hyperpoint{x: x, y: y, z: z, w: w}, 0)
						} else {
							nextCube.applyState(hyperpoint{x: x, y: y, z: z, w: w}, 1)
						}
					} else {
						if count == 3 {
							nextCube.applyState(hyperpoint{x: x, y: y, z: z, w: w}, 1)
						} else {
							nextCube.applyState(hyperpoint{x: x, y: y, z: z, w: w}, 0)
						}
					}
				}
			}
		}
	}
	return nextCube
}

// func equal(matrice1 [][]byte, matrice2 [][]byte) bool {
// 	for i, line := range matrice1 {
// 		for j, letter := range line {
// 			if letter != matrice2[i][j] {
// 				return false
// 			}
// 		}
// 	}
// 	return true

// }

// func countVisuOccupied(i int, j int, matrice [][]byte) int {
// 	maxX := getX(matrice)
// 	maxY := getY(matrice)
// 	occupied := 0
// 	for x := -1; x <= 1; x++ {
// 		for y := -1; y <= 1; y++ {
// 			if x == 0 && y == 0 {
// 				continue
// 			}
// 			if searchDirection(i, j, x, y, matrice, maxX, maxY) {
// 				occupied++
// 			}
// 		}
// 	}

// 	return occupied
// }

// func searchDirection(i, j, x, y int, matrice [][]byte, maxX, maxY int) bool {
// 	for i+x >= 0 && i+x <= maxX-1 && j+y >= 0 && j+y <= maxY-1 {
// 		if string(matrice[j+y][i+x]) == "#" {
// 			return true
// 		}
// 		if string(matrice[j+y][i+x]) == "L" {
// 			return false
// 		}
// 		i += x
// 		j += y
// 	}

// 	return false
// }
