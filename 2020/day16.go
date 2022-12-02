package main

import (
	"aoc/input"
	"fmt"
	"strconv"
	"strings"
	"time"
)

type bound struct {
	min int
	max int
}

func (b bound) valid(i int) bool {
	if i >= b.min && i <= b.max {
		return true
	}

	return false
}

type field struct {
	name           string
	possibleValues []bound
}

func day16() {
	start := time.Now()
	inputs := input.Load("16").ToDoubleStringGroupedArray()
	// get fields
	var fields []field
	for _, line := range inputs[0] {
		var field field
		var elements = strings.Split(line, ":")
		field.name = elements[0]
		valuesSeparatedByOr := elements[1]
		values := strings.Split(valuesSeparatedByOr, "or")
		for _, value := range values {
			minAndMax := strings.Split(strings.TrimSpace(value), "-")
			min, _ := strconv.Atoi(minAndMax[0])
			max, _ := strconv.Atoi(minAndMax[1])
			bound := bound{min: min, max: max}
			field.possibleValues = append(field.possibleValues, bound)
		}
		fields = append(fields, field)
	}
	// my ticket
	var myTicket []int
	values := strings.Split(inputs[1][1], ",")
	for _, value := range values {
		n, _ := strconv.Atoi(value)
		myTicket = append(myTicket, n)
	}

	// all ticket
	var tickets [][]int
	for _, line := range inputs[2][1:] {
		values := strings.Split(line, ",")
		var ticket []int
		for _, value := range values {
			n, _ := strconv.Atoi(value)
			ticket = append(ticket, n)
		}
		tickets = append(tickets, ticket)
	}

	// part 1
	errorRate := 0
	for _, ticket := range tickets {
		for _, value := range ticket {
			valid := false
		out:
			for _, field := range fields {
				for _, bound := range field.possibleValues {
					if bound.valid(value) {
						valid = true
						break out
					}
				}
			}
			if !valid {
				errorRate += value
			}
		}
	}
	fmt.Printf("Star 1: %v\n", errorRate)

	// part 2
	var validTickets [][]int
	for _, ticket := range tickets {
		valid := true
		for _, value := range ticket {
			valueValid := false
		vv:
			for _, field := range fields {
				for _, bound := range field.possibleValues {
					if bound.valid(value) {
						valueValid = true
						break vv
					}
				}
			}
			if !valueValid {
				valid = false
				break
			}
		}
		if valid {
			validTickets = append(validTickets, ticket)
		}
	}
	potentialFields := make([][]field, len(myTicket))
	for i := 0; i < len(myTicket); i++ {
		potentialFields[i] = fields
	}
	for {
		for _, ticket := range validTickets {
			for i, value := range ticket {
				for _, field := range fields {
					validField := false
					for _, bound := range field.possibleValues {
						if bound.valid(value) {
							validField = true
						}
					}
					if !validField {
						potentialFields[i] = removeIfContains(potentialFields[i], field)
					}
				}
			}
		}
		minLength := 1
		for i, _ := range potentialFields {
			if len(potentialFields[i]) == 1 {
				potentialFields = removeFromAll(potentialFields, i)
			} else {
				minLength = len(potentialFields[i])
			}
		}
		if minLength == 1 {
			break
		}
	}

	star2 := 1
	for i, p := range potentialFields {
		f := p[0]
		if strings.Contains(f.name, "departure") {
			star2 *= myTicket[i]
		}
	}
	fmt.Printf("Star 2: %v\n", star2)

	fmt.Println("Execution duration: " + time.Now().Sub(start).String())
}

func removeIfContains(list []field, f field) []field {
	var f3 []field
	for _, f2 := range list {
		if f2.name == f.name {
			continue
		}
		f3 = append(f3, f2)
	}
	return f3
}

func removeFromAll(list [][]field, ind int) [][]field {
	fieldToRemove := list[ind][0]
	newList := make([][]field, len(list))
	for i, fields := range list {
		if i == ind {
			newList[i] = list[i]
			continue
		}
		var fieldToAdd []field
		for _, f := range fields {
			if fieldToRemove.name == f.name {
				continue
			}
			fieldToAdd = append(fieldToAdd, f)
		}
		newList[i] = fieldToAdd
	}
	return newList
}
