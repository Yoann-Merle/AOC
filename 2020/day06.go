package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
)

func day06() {
	inputs := input.Load("6").ToDoubleStringGroupedArray()
	total := 0
	for _, groupedSequences := range inputs {
		group := GroupAnswers{}
		for _, sequence := range groupedSequences {
			group.AddUniqs([]byte(sequence))
		}
		total += group.Count()
	}
	fmt.Printf("Star 1 : %v\n", total)

	total = 0
	for _, groupedSequences := range inputs {
		group := GroupAnswers{}
		for _, sequence := range groupedSequences {
			group.Merge([]byte(sequence))
		}
		total += group.Count()
	}
	fmt.Printf("Star 2 : %v\n", total)
}

type GroupAnswers struct {
	L []byte
	N int
}

func (ga *GroupAnswers) AddUniq(letter byte) {
	for _, element := range ga.L {
		if element == letter {
			return
		}
	}
	ga.L = append(ga.L, letter)
}

func (ga *GroupAnswers) AddUniqs(letters []byte) {
	for _, letter := range letters {
		ga.AddUniq(letter)
	}
	ga.N++
}

func (ga GroupAnswers) Count() int {
	return len(ga.L)
}

func (ga *GroupAnswers) Merge(letters []byte) {
	if ga.N == 0 {
		ga.AddUniqs(letters)
		return
	}

	var temp []byte
	for _, element := range ga.L {
		if arrays.ByteIn(element, letters) {
			temp = append(temp, element)
		}
	}
	ga.L = temp
	ga.N++
}
