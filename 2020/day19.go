package main

import (
	"aoc/input"
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

type Rule struct {
	sets      [][]int
	hardcoded bool
	value     string
}

func day19() {
	data := input.Load("19").ToStringArray()
	var data_rules []string
	var messages []string
	for i, l := range data {
		if l == "" {
			data_rules = data[:i]
			messages = data[i+1:]
			break
		}
	}

	// parse rules
	rules := make(map[int]*Rule)
	for _, rule := range data_rules {
		parts := strings.Split(rule, ":")
		numRule, _ := strconv.Atoi(parts[0])
		rules[numRule] = &Rule{hardcoded: false}

		if strings.Contains(parts[1], "\"") {
			rules[numRule].hardcoded = true
			rules[numRule].value = strings.Trim(parts[1], "\" ")
		} else {
			sets := strings.Split(parts[1], "|")
			rules[numRule].hardcoded = false
			rules[numRule].sets = make([][]int, len(sets))
			for i, set := range sets {
				trimedSet := strings.Trim(set, " ")
				trimedSets := strings.Split(trimedSet, " ")
				rules[numRule].sets[i] = make([]int, len(trimedSets))
				for j, v := range trimedSets {
					intV, _ := strconv.Atoi(v)
					rules[numRule].sets[i][j] = intV
				}
			}
		}
	}

	// part 1
	nbValid := 0
	for i := 0; i < len(messages); i++ {
		layer := [][]int{[]int{0}}
		for {
			layer = buildNewLayer(layer, rules)
			layer = cleanLayer(rules, layer, messages[i])
			if len(layer) == 0 {
				//fmt.Printf("invalid\n")
				break
			}
			if oneMatch(rules, layer) {
				nbValid++
				fmt.Printf("%v\n", messages[i])
				fmt.Printf("valid\n")
				break
			}
		}
	}

	fmt.Printf("Star 1: %v\n", nbValid)
}

func buildNewLayer(layer [][]int, rules map[int]*Rule) [][]int {
	var nextLayer [][]int
	for _, candidate := range layer {
		newPossibilities := developCandidate(rules, candidate)
		nextLayer = append(nextLayer, newPossibilities...)
	}
	return nextLayer
}

func oneMatch(rules map[int]*Rule, layer [][]int) bool {
	for _, candidate := range layer {
		hardCoded := true
		for _, n := range candidate {
			if !rules[n].hardcoded {
				hardCoded = false
				break
			}
		}
		if hardCoded {
			fmt.Printf("can: %v\n", candidate)
			return true
		}
	}

	return false
}

func cleanLayer(rules map[int]*Rule, layer [][]int, message string) [][]int {
	cleanedLayer := make([][]int, 0)
	for _, candidate := range layer {
		regex := buildRegex(rules, candidate)
		matched, err := regexp.MatchString(regex, message)
		if err != nil {
			log.Fatal(err)
		}
		if matched {
			cleanedLayer = append(cleanedLayer, candidate)
		}
	}

	return cleanedLayer
}

func buildRegex(rules map[int]*Rule, candidate []int) string {
	regex := `^`
	for _, n := range candidate {
		if rules[n].hardcoded {
			regex = regex + rules[n].value
		} else {
			regex = regex + `[ab]+`
		}
	}
	regex = regex + `$`

	return regex
}

func developCandidate(rules map[int]*Rule, candidate []int) [][]int {
	newCandidates := make([][]int, 0)
	for _, num := range candidate {
		newCandidatesTemp := make([][]int, 0)
		if rules[num].hardcoded == false {
			if len(newCandidates) == 0 {
				for _, set := range rules[num].sets {
					newCandidatesTemp = append(newCandidatesTemp, set)
				}
			} else {
				for _, can := range newCandidates {
					for _, set := range rules[num].sets {
						newCandidatesTemp = append(newCandidatesTemp, append(can, set...))
					}
				}
			}
		} else {
			if len(newCandidates) == 0 {
				newCandidatesTemp = append(newCandidatesTemp, []int{num})
			} else {
				for _, can := range newCandidates {
					newCandidatesTemp = append(newCandidatesTemp, append(can, num))
				}
			}
		}
		newCandidates = newCandidatesTemp
	}

	return newCandidates
}
