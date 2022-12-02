package arrays

func StringIn(a string, list []string) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}

	return false
}

func CountString(a string, list []string) int {
	count := 0
	for _, b := range list {
		if b == a {
			count++
		}
	}

	return count
}

func DoubleIntIn(a []int, list [][]int) bool {
	for _, b := range list {
		if EqualInt(b, a) {
			return true
		}
	}
	return false
}

func IntIn(a int, list []int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func ByteIn(a byte, list []byte) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}

func IntMax(list []int) int {
	var max int
	for i, b := range list {
		if i == 0 {
			max = b
		} else if b > max {
			max = b
		}
	}
	return max
}

func IntMin(list []int) int {
	var min int
	for i, b := range list {
		if i == 0 {
			min = b
		} else if b < min {
			min = b
		}
	}
	return min
}

func Index(list []string, elem string) int {
	for i, v := range list {
		if v == elem {
			return i
		}
	}
	return -1
}

func Unique(l []string) []string {
	l2 := []string{}
	for _, s := range l {
		if !StringIn(s, l2) {
			l2 = append(l2, s)
		}
	}

	return l2
}

func Reverse(a []byte) []byte {
	rev := []byte{}
	for i := len(a) - 1; i >= 0; i-- {
		rev = append(rev, a[i])
	}

	return rev
}

func EqualInt(a []int, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func Equal(a []byte, b []byte) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}
