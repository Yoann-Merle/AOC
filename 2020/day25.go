package main

import (
	"fmt"
)

func day25() {
	doorPubKey := 12320657
	cardPubKey := 9659666

	// cardPubKey := 5764801
	// doorPubKey := 17807724

	cardLoopSize := findLoopSize(7, cardPubKey)
	doorLoopSize := findLoopSize(7, doorPubKey)
	fmt.Println(cardLoopSize)
	fmt.Println(doorLoopSize)
	encryptKey := loopNTime(doorPubKey, cardLoopSize)
	fmt.Println(encryptKey)
	encryptKey2 := loopNTime(cardPubKey, doorLoopSize)
	fmt.Println(encryptKey2)
}

func findLoopSize(subNum int, pub int) int {
	n := 1
	for i := 1; ; i++ {
		n *= subNum
		n %= 20201227
		if n == pub {
			return i
		}
	}
}

func loopNTime(subNum int, nb int) int {
	n := 1
	for i := 1; ; i++ {
		n *= subNum
		n %= 20201227
		if i == nb {
			return n
		}
	}
}
