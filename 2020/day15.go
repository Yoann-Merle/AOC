package main

import (
	"fmt"
)

type Positions struct {
	last   int
	before int
}

type Collection struct {
	history    map[int]Positions
	lastValue  int
	lastIndice int
}

func (p *Positions) add(i int) {
	if p.last != 0 {
		p.before = p.last
	}
	p.last = i
}

func (p *Positions) diff() int {
	if p.last != 0 && p.before != 0 {
		return p.last - p.before
	}
	return 0
}

func (c *Collection) add() {
	pos := c.history[c.lastValue]
	diff := pos.diff()
	pos2 := c.history[diff]
	pos2.add(c.lastIndice + 1)
	c.history[diff] = pos2
	c.lastIndice += 1
	c.lastValue = diff
}

func day15() {
	// part 1
	startingNumbers := []int{1, 20, 11, 6, 12, 0}
	collection := Collection{history: make(map[int]Positions)}
	for i, n := range startingNumbers {
		if pos, ok := collection.history[n]; ok {
			pos.add(i + 1)
		} else {
			pos := Positions{last: i + 1}
			collection.history[n] = pos
		}
		collection.lastValue = n
		collection.lastIndice = i + 1
	}

	for i := 0; i <= 30000000; i++ {
		collection.add()
		if collection.lastIndice == 2020 {
			fmt.Printf("Star 1: %v\n", collection.lastValue)
		}
		if collection.lastIndice == 30000000 {
			fmt.Printf("Star 2: %v\n", collection.lastValue)
		}
	}
}
