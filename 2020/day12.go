package main

import (
	"aoc/input"
	"fmt"
	"log"
	"math"
	"strconv"
	"strings"
)

func day12() {
	input := input.Load("12").ToStringArray()
	var instructions []Command
	for _, line := range input {
		value, err := strconv.Atoi(line[1:])
		if err != nil {
			log.Fatal(err)
		}
		instruct := Command{
			direction: string(line[0]),
			value:     value,
		}
		instructions = append(instructions, instruct)
	}

	// part 1
	boat := Boat{
		direction: "E",
		position: Position{
			north: 0,
			east:  0,
		},
	}
	for _, instruct := range instructions {
		boat.exec(instruct)
	}

	fmt.Printf("Star 1 : %v\n", math.Abs(float64(boat.position.north))+math.Abs(float64(boat.position.east)))

	//part 2
	boat = Boat{
		direction: "E",
		position: Position{
			north: 0,
			east:  0,
		},
		waypoint: Position{
			north: 1,
			east:  10,
		},
	}
	for _, instruct := range instructions {
		boat.exec2(instruct)
	}

	fmt.Printf("Star 2 : %v\n", math.Abs(float64(boat.position.north))+math.Abs(float64(boat.position.east)))
}

type Position struct {
	north int
	east  int
}

type Command struct {
	direction string
	value     int
}

type Boat struct {
	direction string
	position  Position
	waypoint  Position
}

func (b *Boat) move(dir string, value int) {
	switch dir {
	case "N":
		b.position.north += value
	case "S":
		b.position.north -= value
	case "E":
		b.position.east += value
	case "W":
		b.position.east -= value
	}
}

func (b *Boat) turn1(instr Command) {
	compass := "NESW"
	index := strings.Index(compass, b.direction)
	angle := instr.value / 90
	if instr.direction == "R" {
		b.direction = string(compass[(index+angle)%len(compass)])
	} else if instr.direction == "L" {
		b.direction = string(compass[(len(compass)+index-angle)%len(compass)])
	}
}

func (b *Boat) exec(inst Command) {
	switch inst.direction {
	case "N", "S", "E", "W":
		b.move(inst.direction, inst.value)
	case "F":
		b.move(b.direction, inst.value)
	case "R", "L":
		b.turn1(inst)
	default:
		log.Fatal(inst.direction + " : action possible")
	}
}

func (p *Position) move(dir string, value int) {
	switch dir {
	case "N":
		p.north += value
	case "S":
		p.north -= value
	case "E":
		p.east += value
	case "W":
		p.east -= value
	}
}

func (b *Boat) move2(value int) {
	b.position.north += b.waypoint.north * value
	b.position.east += b.waypoint.east * value
}

func (p *Position) rotate(instr Command) {
	var angle float64
	if instr.direction == "R" {
		angle = -1
	} else {
		angle = 1
	}
	angle *= float64(instr.value) * math.Pi / 180
	north := int(math.Sin(angle))*p.east + int(math.Cos(angle))*p.north
	east := int(math.Cos(angle))*p.east - int(math.Sin(angle))*p.north
	p.north = north
	p.east = east
}

func (b *Boat) exec2(inst Command) {
	switch inst.direction {
	case "N", "S", "E", "W":
		b.waypoint.move(inst.direction, inst.value)
	case "F":
		b.move2(inst.value)
	case "R", "L":
		b.waypoint.rotate(inst)
	default:
		log.Fatal(inst.direction + " : action possible")
	}

}
