package main

import (
	"aoc/input"
	"fmt"
	"log"
	"strconv"
	"strings"
)

type shuttle struct {
	indice int
	id     int
}

func day13() {
	inputs := input.Load("13").ToStringArray()

	earliestDepart, err := strconv.Atoi(inputs[0])
	if err != nil {
		log.Fatal("Could not convert : " + inputs[0])
	}
	var shuttlesIds = strings.Split(inputs[1], ",")
	var shuttles []shuttle
	for indice, id := range shuttlesIds {
		shuttleId, err := strconv.Atoi(id)
		if err != nil || id == "x" {
			continue
		}
		shuttles = append(shuttles, shuttle{indice: indice, id: shuttleId})
	}

	// part 1
	var minWaitingTime int
	var minWaitingId int
	for i, shuttle := range shuttles {
		waitingTime := shuttle.id - earliestDepart%shuttle.id
		if waitingTime < minWaitingTime || i == 0 {
			minWaitingTime = waitingTime
			minWaitingId = shuttle.id
		}
	}
	fmt.Printf("Star 1: %v\n", minWaitingTime*minWaitingId)

	// part 2
	startTime := 0
	incrementFactor := 1
	for _, shuttle := range shuttles {
		var firstHit = true
		for timeStamp := startTime; ; timeStamp += incrementFactor {
			if (timeStamp+shuttle.indice)%shuttle.id == 0 {
				if firstHit {
					startTime = timeStamp
					firstHit = false
				} else {
					incrementFactor = timeStamp - startTime
					break
				}
			}
		}
	}
	fmt.Printf("Star 2: %v\n", startTime)
}
