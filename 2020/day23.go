package main

import (
    "fmt"
    )

func day23() {
    cups := []int{4, 8, 7, 9, 1, 2, 3, 6, 5}
    // cups := []int{3, 8, 9, 1, 2, 5, 4, 6, 7}

    // part 1
    numberOfCycles := 100
    currentCupIndex := 0
    for i := 0; i < numberOfCycles; i++ {
        cupsTemp := append([]int{}, cups[0])
        cupsTemp = append(cupsTemp, cups[4:]...)

        currentCupIndex = findNextIndex(cupsTemp)
        start := cupsTemp[:currentCupIndex + 1]
        end := make([]int, len(cupsTemp) - currentCupIndex - 1)
        copy(end, cupsTemp[currentCupIndex + 1:])
        cups = append(start, cups[1:4]...)
        cups = append(cups, end...)
        cups = append(cups[1:], cups[:1]...)
    }
    fmt.Printf("Star 1 : %v\n", cups)

    // part 2
    cups = []int{4, 8, 7, 9, 1, 2, 3, 6, 5}
    // cups := []int{3, 8, 9, 1, 2, 5, 4, 6, 7}
    for j:= len(cups) + 1; j <= 1000000; j++ {
        cups = append(cups, j)
    }
    numberOfCycles = 10000000
    currentCupIndex = 0
    for i := 0; i < numberOfCycles; i++ {
        cupsTemp := append([]int{}, cups[0])
        cupsTemp = append(cupsTemp, cups[4:]...)

        currentCupIndex = findNextIndex(cupsTemp)
        start := cupsTemp[:currentCupIndex + 1]
        end := make([]int, len(cupsTemp) - currentCupIndex - 1)
        copy(end, cupsTemp[currentCupIndex + 1:])
        cups = append(start, cups[1:4]...)
        cups = append(cups, end...)
        cups = append(cups[1:], cups[:1]...)
    }

    // temporary solution
    // indexOne := 0
    // for i, v := range cups {
    //     if v == 1 {
    //         indexOne = i
    //     }
    // }
    // resp := cups[(indexOne + 1) % len(cups)] * cups[(indexOne + 2) % len(cups)]
    // fmt.Printf("Star 2 : %v\n", resp)
}

func findNextIndex(slice []int) int {
    j := -1
    initValue := slice[0]
    for {
        if j + initValue <= 0 {
            j += len(slice) + 3
        }
        for i, v := range slice {
            if v == j+initValue {
                return i
            }
        }

        j -= 1
    }
}
