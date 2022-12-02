package main

import (
	"aoc/arrays"
	"aoc/input"

	"fmt"
	"log"
	"strconv"
	"strings"
)

type Operation struct {
}

func day18() {
	list_operations := input.Load("18").ToStringArray()

	// part 1
	sum := 0
	for _, ope := range list_operations {
		sum += macro(ope, false)
	}
	fmt.Printf("Star 1: %v\n", sum)

	// part 2
	sum = 0
	for _, ope := range list_operations {
		sum += macro(ope, true)
	}
	fmt.Printf("Star 2: %v\n", sum)
}

func macro(formula string, advanced bool) int {
	lastIndexClosing := strings.Index(formula, ")")
	if lastIndexClosing == -1 {
		if !advanced {
			return calculate(formula)
		} else {
			return advancedCalculate(formula)
		}
	} else {
		partialResultInt := 0
		lastIndexOpening := strings.LastIndex(formula[:lastIndexClosing], "(")
		if !advanced {
			partialResultInt = calculate(formula[lastIndexOpening+1 : lastIndexClosing])
		} else {
			partialResultInt = advancedCalculate(formula[lastIndexOpening+1 : lastIndexClosing])
		}
		partialResult := strconv.Itoa(partialResultInt)
		return macro(formula[:lastIndexOpening]+partialResult+formula[lastIndexClosing+1:], advanced)
	}
}

func calculate(formula string) int {
	elems := strings.Split(formula, " ")
	nb, err := strconv.Atoi(elems[0])
	if err != nil {
		log.Fatal("Could not convert first element in calculate: " + elems[0])
	}

	for i := 0; i < len(elems)-2; i += 2 {
		switch elems[i+1] {
		case "+":
			nb2, _ := strconv.Atoi(elems[i+2])
			nb += nb2
		case "*":
			nb2, _ := strconv.Atoi(elems[i+2])
			nb *= nb2
		}
	}

	return nb
}

func advancedCalculate(formula string) int {
	elems := strings.Split(formula, " ")
	var nb int
	for {
		index := arrays.Index(elems, "+")
		if index == -1 {
			break
		}
		nb, _ = strconv.Atoi(elems[index-1])
		nb2, _ := strconv.Atoi(elems[index+1])
		nb += nb2
		nbString := strconv.Itoa(nb)
		tmpElems := append(elems[:index-1], nbString)
		if index+2 < len(elems) {
			tmpElems = append(tmpElems, elems[index+2:]...)
		}
		elems = tmpElems
	}
	nb = 1
	for i := 0; i < len(elems); i += 2 {
		nb2, _ := strconv.Atoi(elems[i])
		nb *= nb2
	}

	return nb
}
