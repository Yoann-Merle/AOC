package main

import (
	"aoc/input"
	"aoc/arrays"
	"fmt"
	"strconv"
)

func day22() {
	decks := input.Load("22").ToDoubleStringGroupedArray()
    deck_p1 := []int{}
    deck_p2 := []int{}
    for _, card := range decks[0][1:] {
        val, _ := strconv.Atoi(card)
        deck_p1 = append(deck_p1, val)
    }
    for _, card := range decks[1][1:] {
        val, _ := strconv.Atoi(card)
        deck_p2 = append(deck_p2, val)
    }

	// part 1
    winingDeck := game(deck_p1, deck_p2)
	fmt.Printf("Star 1: %v\n", score(winingDeck))

	// part 2
    _, winingDeck = recursiveGame(deck_p1, deck_p2)
	fmt.Printf("Star 2: %v\n", score(winingDeck))

}

func recursiveGame(deck_p1 []int, deck_p2[]int) (int , []int) {
    previousDeckP1 := [][]int{}
    previousDeckP2 := [][]int{}
    for {
        if len(deck_p1) == 0 {
            return 2, deck_p2
        } else if len(deck_p2) == 0 {
            return 1, deck_p1
        }
        if arrays.DoubleIntIn(deck_p1, previousDeckP1) || arrays.DoubleIntIn(deck_p2, previousDeckP2) {
            return 1, deck_p1
        } else {
            previousDeckP1 = append(previousDeckP1, deck_p1)
            previousDeckP2 = append(previousDeckP2, deck_p2)
        }
        if len(deck_p1) - 1 >= deck_p1[0] && len(deck_p2) - 1 >= deck_p2[0] {
            copyDeck1 := make([]int, len(deck_p1))
            copyDeck2 := make([]int, len(deck_p2))
            copy(copyDeck1, deck_p1)
            copy(copyDeck2, deck_p2)
            w, _ := recursiveGame(copyDeck1[1:copyDeck1[0]+1], copyDeck2[1:copyDeck2[0]+1])
            if w == 1 {
                deck_p1 = append(deck_p1[1:], deck_p1[0], deck_p2[0])
                deck_p2 = deck_p2[1:]
            } else {
                deck_p2 = append(deck_p2[1:], deck_p2[0], deck_p1[0])
                deck_p1 = deck_p1[1:]
            }
        } else {
            if deck_p1[0] > deck_p2[0] {
                deck_p1 = append(deck_p1[1:], deck_p1[0], deck_p2[0])
                deck_p2 = deck_p2[1:]
            } else {
                deck_p2 = append(deck_p2[1:], deck_p2[0], deck_p1[0])
                deck_p1 = deck_p1[1:]
            }
        }
    }
}
func game(deck_p1 []int, deck_p2[]int) []int {
    for {
        if len(deck_p1) == 0 {
            return deck_p2
        } else if len(deck_p2) == 0 {
            return deck_p1
        }
        if deck_p1[0] > deck_p2[0] {
            deck_p1 = append(deck_p1[1:], deck_p1[0], deck_p2[0])
            deck_p2 = deck_p2[1:]
        } else {
            deck_p2 = append(deck_p2[1:], deck_p2[0], deck_p1[0])
            deck_p1 = deck_p1[1:]
        }
    }
}

func score(deck []int) int {
    sum := 0
    for i := len(deck) -1; i >=0; i-- {
        sum += deck[i] * (len(deck) - i)
    }
    return sum
}

