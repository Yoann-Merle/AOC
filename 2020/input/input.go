package input

import (
	"bufio"
	"log"
	"os"
	"strconv"
)

type Content struct {
	lines []string
}

func Load(numFile string) Content {
	file, err := os.Open("inputs/input" + numFile + ".txt")
	if err != nil {
		log.Fatal(err)
	}
	defer func() {
		if err = file.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	content := Content{lines: []string{}}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		input := scanner.Text()
		content.lines = append(content.lines, input)
	}

	return content
}

func (c Content) ToDoubleByteArray() [][]byte {
	byteArray := make([][]byte, len(c.lines))
	for i, line := range c.lines {
		byteArray[i] = []byte(line)
	}

	return byteArray
}

func (c Content) ToIntArray() []int {
	intArray := make([]int, len(c.lines))
	for i, line := range c.lines {
		value, err := strconv.Atoi(line)
		if err != nil {
			log.Fatal("Line " + line + "cannot be converted to int")
		}
		intArray[i] = value
	}

	return intArray
}

func (c Content) ToStringArray() []string {
	return c.lines
}

func (c Content) ToSpaceConcatenateStringArray() []string {
	var groupedLines []string
	var group string
	for _, line := range c.lines {
		if line == "" {
			groupedLines = append(groupedLines, group)
			group = ""
		} else {
			group += " " + line
		}
	}
	groupedLines = append(groupedLines, group)

	return groupedLines
}

func (c Content) ToDoubleStringGroupedArray() [][]string {
	var groupedLines [][]string
	var group []string
	for _, line := range c.lines {
		if line == "" {
			groupedLines = append(groupedLines, group)
			group = []string{}
		} else {
			group = append(group, line)
		}
	}
	groupedLines = append(groupedLines, group)

	return groupedLines
}
