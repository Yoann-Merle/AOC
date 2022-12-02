package main

import (
	"aoc/input"
	"fmt"
	"log"
	"math"
	"regexp"
	"strconv"
	"strings"
)

type MaskedData struct {
	mask string
	data []pair
}
type pair struct {
	adress uint64
	value  uint64
}

func reverse(s string) string {
	rns := []rune(s)
	for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
		rns[i], rns[j] = rns[j], rns[i]
	}

	return string(rns)
}

func (i MaskedData) update(memory map[uint64]uint64) {
	for _, pair := range i.data {
		mask1, err := strconv.ParseUint(strings.Replace(i.mask, "X", "0", -1), 2, 64)
		mask2, err2 := strconv.ParseUint(strings.Replace(i.mask, "X", "1", -1), 2, 64)
		if err != nil || err2 != nil {
			log.Fatal("Error while converting to int")
		}
		newValue := pair.value | mask1
		newValue &= mask2
		memory[pair.adress] = newValue
	}
}

func (i MaskedData) update2(memory map[uint64]uint64) {
	for _, pair := range i.data {
		mask1, err := strconv.ParseUint(strings.Replace(i.mask, "X", "0", -1), 2, 64)
		if err != nil {
			log.Fatal("Error while converting to int")
		}
		newlocation := pair.adress | mask1
		var locations []uint64
		locations = append(locations, newlocation)
		for i, x := range reverse(i.mask) {
			if x == []rune("X")[0] {
				var newLocations []uint64
				for _, location := range locations {
					newlocation = uint64(location ^ uint64(math.Pow(2, float64(i))))
					newLocations = append(newLocations, newlocation)
				}
				locations = append(locations, newLocations...)
			}
		}
		for _, location := range locations {
			memory[location] = pair.value
		}
	}
}

func day14() {
	inputs := input.Load("14").ToStringArray()
	instructions := convertInputToMaskAndMemory(inputs)

	// part 1
	var memory = make(map[uint64]uint64)
	for _, instruction := range instructions {
		instruction.update(memory)
	}
	var star1 uint64
	for _, v := range memory {
		star1 += v
	}
	fmt.Printf("Star 1: %v\n", star1)

	// part 2
	memory = make(map[uint64]uint64)
	for _, instruction := range instructions {
		instruction.update2(memory)
	}

	var star2 uint64
	for _, v := range memory {
		star2 += v
	}
	fmt.Printf("Star 2: %v\n", star2)
}

func convertInputToMaskAndMemory(inputs []string) []MaskedData {
	var instructions []MaskedData
	var instruc = MaskedData{}
	for _, line := range inputs {
		var splits = strings.Split(line, "=")
		if strings.Contains(splits[0], "mask") {
			if instruc.mask != "" {
				instructions = append(instructions, instruc)
				instruc = MaskedData{}
			}
			instruc.mask = strings.Trim(splits[1], " ")
		} else {
			re := regexp.MustCompile(`(mem\[(\d+)\])`)
			matched := re.FindAllStringSubmatch(splits[0], -1)
			location, err := strconv.Atoi(matched[0][2])
			value, err2 := strconv.Atoi(strings.Trim(splits[1], " "))
			if err != nil || err2 != nil {
				log.Fatal("Error while parsing input")
			}
			instruc.data = append(instruc.data, pair{adress: uint64(location), value: uint64(value)})
		}
	}
	instructions = append(instructions, instruc)

	return instructions
}
