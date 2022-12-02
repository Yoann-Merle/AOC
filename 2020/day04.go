package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func day04() {
	passports := input.Load("4").ToSpaceConcatenateStringArray()
	var mandatoryFields = []string{"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
	valid := 0

	// part 1
	for _, passport := range passports {
		var elements = strings.Split(passport, " ")
		var presentFields []string
		for _, element := range elements {
			var keyValue = strings.Split(element, ":")
			key := keyValue[0]
			if arrays.StringIn(key, mandatoryFields) && !arrays.StringIn(key, presentFields) {
				presentFields = append(presentFields, key)
			}
		}
		if len(presentFields) > 6 {
			valid++
		}
	}
	fmt.Printf("Star 1 : %v\n", valid)

	// part 2
	valid = 0
	for _, passport := range passports {
		var elements = strings.Split(passport, " ")
		var presentFields []string
		for _, element := range elements {
			if element == "" {
				continue
			}
			var keyValue = strings.Split(element, ":")
			key := keyValue[0]
			if isValid(keyValue) && arrays.StringIn(key, mandatoryFields) && !arrays.StringIn(key, presentFields) {
				presentFields = append(presentFields, key)
			}
		}
		if len(presentFields) > 6 {
			valid++
		}
	}
	fmt.Printf("Star 2 : %v\n", valid)
}

func isValid(keyValue []string) bool {
	key := keyValue[0]
	value := keyValue[1]
	switch key {
	case "byr":
		i, _ := strconv.Atoi(value)
		if i >= 1920 && i <= 2002 {
			return true
		}
	case "iyr":
		i, _ := strconv.Atoi(value)
		if i >= 2010 && i <= 2020 {
			return true
		}
	case "eyr":
		i, _ := strconv.Atoi(value)
		if i >= 2020 && i <= 2030 {
			return true
		}
	case "hgt":
		re := regexp.MustCompile(`^(\d{1,3})(cm|in)$`)
		matched := re.FindAllSubmatch([]byte(value), -1)
		if len(matched) == 1 && len(matched[0]) == 3 {
			n, _ := strconv.Atoi(string(matched[0][1]))
			if string(matched[0][2]) == "in" && n >= 59 && n <= 76 {
				return true
			}
			if string(matched[0][2]) == "cm" && n >= 150 && n <= 193 {
				return true
			}
		}
	case "hcl":
		matched, _ := regexp.Match(`^#(\d|[a-f]){6}$`, []byte(value))
		if matched {
			return true
		}
		return false
	case "ecl":
		matched, _ := regexp.Match(`^(amb|blu|brn|gry|grn|hzl|oth)$`, []byte(value))
		if matched {
			return true
		}
		return false
	case "pid":
		matched, _ := regexp.Match(`^\d{9}$`, []byte(value))
		if matched {
			return true
		}
		return false
	case "cid":
		return true

	}
	return false
}
