package main

import (
	"aoc/arrays"
	"aoc/input"
	"fmt"
	"log"
	"regexp"
	"strconv"
)

func day20() {
	input := input.Load("20-test").ToDoubleStringGroupedArray()
	re := regexp.MustCompile(`^Tile\s(\d+):`)
	allPictures := []picture{}
	for _, lines := range input {
		matches := re.FindStringSubmatch(lines[0])
		if len(matches) != 2 {
			log.Fatal("Parsing error")
		}
		id, _ := strconv.Atoi(matches[1])
		p := picture{id: id, orient: 0}
		p.pixels = make([][]byte, len(lines[1:]))
		for i, subline := range lines[1:] {
			p.pixels[i] = make([]byte, len(subline))
			for j, c := range subline {
				p.pixels[i][j] = byte(c)
			}
		}
		allPictures = append(allPictures, p)
	}

	// part 1
	productAngle := 1
	for i, p := range allPictures {
		fitCount := 0
		for j, p2 := range allPictures {
			if i == j {
				continue
			}
			if v, _ := p.fit(&p2); v == true {
				fitCount++
			}
		}
		if fitCount == 2 {
			productAngle *= p.id
		}
	}

	fmt.Printf("Star 1: %v\n", productAngle)

	bigPic := BigPicture{content: make(map[int]map[int]*picture)}
	bigPic.content[0] = make(map[int]*picture)
	for {
		if len(allPictures) == 0 {
			break
		}
		for i, p := range allPictures {
			if bigPic.place(&p) {
				allPictures = append(allPictures[:i], allPictures[i+1:]...)
				break
			}
		}
	}
	trimPicture := bigPic.generateTrimPicture()
	for _, line := range trimPicture {
		for _, c := range line {
			fmt.Print(string(c))
		}
		fmt.Print("\n")
	}
	// orientation not kept inside bigPicture
	fmt.Printf("Star 2: %v\n", bigPic)
}

type BigPicture struct {
	content map[int]map[int]*picture
}

func (bp *BigPicture) generateTrimPicture() [][]byte {
	globImage := [][]byte{}
	minX := 0
	maxX := 0
	minY := 0
	maxY := 0
	for x, my := range bp.content {
		if x < minX {
			minX = x
		}
		if x > maxX {
			maxX = x
		}
		for y, p := range my {
			p.trim()
			if y < minY {
				minY = y
			}
			if y > maxY {
				maxY = y
			}
		}
	}
	for y := minY; y <= maxY; y++ {
		for x := minX; x <= maxX; x++ {
			p := bp.content[x][y]
			if x == minX {
				for _, line := range p.pixels {
					globImage = append(globImage, line)
				}
			} else {
				for i, line := range p.pixels {
					globImage[i+len(p.pixels)*(y-minY)] = append(globImage[i+len(p.pixels)*(y-minY)], line...)
				}
			}
		}
	}
	return globImage
}

func (bp *BigPicture) place(pic *picture) bool {
	if len(bp.content[0]) == 0 {
		bp.content[0][0] = pic
		return true
	} else {
		for x, my := range bp.content {
			for y, p := range my {
				if f, w := p.fit(pic); f == true {
					if w == "t" {
						if _, ok := bp.content[x][y-1]; ok {
							log.Fatal("case already used")
						}
						if bp.content[x] == nil {
							bp.content[x] = make(map[int]*picture)
						}
						bp.content[x][y-1] = pic
						return true
					} else if w == "b" {
						if _, ok := bp.content[x][y+1]; ok {
							log.Fatal("case already used")
						}
						if bp.content[x] == nil {
							bp.content[x] = make(map[int]*picture)
						}
						bp.content[x][y+1] = pic
						return true
					} else if w == "l" {
						if _, ok := bp.content[x-1][y]; ok {
							log.Fatal("case already used")
						}
						if bp.content[x-1] == nil {
							bp.content[x-1] = make(map[int]*picture)
						}
						bp.content[x-1][y] = pic
						return true
					} else if w == "r" {
						if _, ok := bp.content[x+1][y]; ok {
							log.Fatal("case already used")
						}
						if bp.content[x+1] == nil {
							bp.content[x+1] = make(map[int]*picture)
						}
						bp.content[x+1][y] = pic
						return true
					}
				}
			}
		}
	}

	return false
}

type picture struct {
	pixels [][]byte
	id     int
	orient int
}

func (p *picture) fit(p2 *picture) (bool, string) {
	for i := 0; i < 8; i++ {
		if arrays.Equal(p.getBottom(), p2.getTop()) {
			return true, "b"
		}
		if arrays.Equal(p.getTop(), p2.getBottom()) {
			return true, "t"
		}
		if arrays.Equal(p.getLeft(), p2.getRight()) {
			return true, "l"
		}
		if arrays.Equal(p.getRight(), p2.getLeft()) {
			return true, "r"
		}
		p2.flip()
	}
	return false, ""
}

func (p *picture) trim() {
	newPixels := [][]byte{}
	for i, line := range p.pixels {
		if i != 0 && i != len(p.pixels)-1 {
			newLine := line[1 : len(line)-1]
			newPixels = append(newPixels, newLine)
		}
	}
	p.pixels = newPixels
}

func (p *picture) flip() {
	newPixels := [][]byte{}
	if p.orient%2 == 0 {
		for _, line := range p.pixels {
			newLine := arrays.Reverse(line)
			newPixels = append(newPixels, newLine)
		}
	} else if p.orient%4 == 1 {
		for i := len(p.pixels) - 1; i >= 0; i-- {
			newPixels = append(newPixels, p.pixels[i])
		}
	} else if p.orient%4 == 3 {
		for i := 0; i < len(p.pixels); i++ {
			newPixelLine := []byte{}
			for _, line := range p.pixels {
				newPixelLine = append(newPixelLine, line[i])
			}
			newPixels = append(newPixels, newPixelLine)
		}
	}

	p.pixels = newPixels
	p.orient += 1
	p.orient %= 8
}

func (p *picture) show() {
	fmt.Printf("\nid:%v\n", p.id)
	for _, l := range p.pixels {
		for _, c := range l {
			fmt.Printf("%v", string(c))
		}
		fmt.Printf("\n")
	}
}

func (p *picture) getTop() []byte {
	return p.pixels[0]
}

func (p *picture) getBottom() []byte {
	return p.pixels[len(p.pixels)-1]
}

func (p *picture) getLeft() []byte {
	line := []byte{}
	for _, pix := range p.pixels {
		line = append(line, pix[0])
	}
	return line
}

func (p *picture) getRight() []byte {
	line := []byte{}
	for _, pix := range p.pixels {
		line = append(line, pix[len(pix)-1])
	}
	return line
}
