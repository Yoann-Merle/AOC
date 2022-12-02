package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
	"log"
	"regexp"
	"strings"
)

type list struct {
	ingredients []string
}

func (l *list) fusion(l2 []string) {
	if len(l.ingredients) == 0 {
		copy(l.ingredients, l2)
	} else {
		tempList := []string{}
		for _, i := range l2 {
			if arrays.StringIn(i, l.ingredients) {
				tempList = append(tempList, i)
			}
		}
		l.ingredients = tempList
	}
}

func (l *list) remove(l2 string) {
	tempList := []string{}
	for _, i := range l.ingredients {
		if i != l2 {
			tempList = append(tempList, i)
		}
	}
	l.ingredients = tempList
}

func day21() {
	input_ := input.Load("21").ToStringArray()
	piba := make(map[string]*list) //piba : potential igredient by allergen
	allIngs := []string{}
	re := regexp.MustCompile(`(.+)\(contains (.+)\)`)
	for _, li := range input_ {
		matches := re.FindAllStringSubmatch(li, -1)
		if len(matches[0]) != 3 {
			log.Fatal("erro")
		}
		ings := strings.Split(matches[0][1], " ")
		for i, ing := range ings {
			ings[i] = strings.Trim(ing, " ")
		}
		allIngs = append(allIngs, ings...)
		all := strings.Split(matches[0][2], ",")
		for _, a := range all {
			if _, ok := piba[strings.Trim(a, " ")]; ok {
				piba[strings.Trim(a, " ")].fusion(ings)
			} else {
				l := &list{ingredients: ings}
				piba[strings.Trim(a, " ")] = l
			}
		}
	}
	safe := []string{}
	for _, ing := range arrays.Unique(allIngs) {
		in := false
		for _, list := range piba {
			if arrays.StringIn(ing, list.ingredients) {
				in = true
				break
			}
		}
		if !in {
			safe = append(safe, ing)
		}
	}

	//part 1
	sum := 0
	for a, l := range piba {
		fmt.Print(a)
		fmt.Println(l.ingredients)
	}
	fmt.Println(sum)

	// part2
	for _, s := range safe {
		sum += arrays.CountString(s, allIngs)
	}
	//fqhpsl,zxncg,clzpsl,zbbnj,jkgbvlxh,dzqc,ppj,glzb
}
