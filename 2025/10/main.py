#!/bin/python
import itertools
import copy
import sys


def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines


def parse_machines(lines):
    machines = []
    for line in lines:
        blocks = line.split()
        leds_s = blocks[0]
        leds = []
        for led in leds_s:
            if led == '.':
                leds.append(0)
            if led == '#':
                leds.append(1)
        buttons_s = blocks[1:-1]
        buttons = []
        for button in buttons_s:
            button = button.replace('(', '').replace(')', '')
            button_number = [int(b) for b in button.split(',')]
            buttons.append(button_number)
        jolts_s = blocks[-1]
        jolts_s = jolts_s.replace('{', '').replace('}', '')
        jolts = [int(b) for b in jolts_s.split(',')]
        machines.append({'leds': leds, 'buttons': buttons, 'jolts': jolts})

    return machines


def apply_button(leds, button):
    new_leds = copy.deepcopy(leds)
    for b in button:
        new_leds[b] = (leds[b] + 1) % 2

    return new_leds


def solve(machine, combs):
    target = machine['leds']
    solution = []
    for comb in combs:
        leds = [0 for _ in target]
        for button in comb:
            leds = apply_button(leds, button)
        if leds == target:
            if len(solution) == 0 or len(solution) > len(comb):
                solution = comb
    return solution


def calc_combinaisons(buttons):
    comb = []
    for b in range(len(buttons) + 1):
        comb += itertools.combinations(buttons, b)
    return comb


class Machine:
    def __init__(self, wanted_state, buttons):
        self._buttons = buttons
        self._wanted_state = wanted_state
        self._current_state = [0 for _ in range(len(wanted_state))]
        self._buttons_pressed = [None for _ in range(len(buttons))]

    def _buttons_idx_for_idx_led(self, idx):
        buttons_idx = []
        for b in range(len(self._buttons)):

            if idx in self._buttons[b] and self._buttons_pressed[b] == None:
                buttons_idx.append(b)
        return buttons_idx

    def _pressed_button(self, idx, n):
        if self._buttons_pressed[idx] is not None:
            self._buttons_pressed[idx] += n
        else:
            self._buttons_pressed[idx] = n

        for led in self._buttons[idx]:
            self._current_state[led] += n

    def __repr__(self):
        return f"Machine({self._current_state=}, {self._buttons_pressed=})"

    def __str__(self):
        return f"{self._buttons=}, {self._current_state=}"

    def solve(self):
        pass

    def _get_max_push(self, idx):
        max = 0
        for led_idx in self._buttons[idx]:
            n = self._wanted_state[led_idx] - self._current_state[led_idx]
            if n > max:
                max = n
        return max

    def solve(self):
        states = [self]
        self.reducto(1)
        new_states = self.reducto(2)
        return new_states

    def reduce_states(self, states):
        new_states = []
        for state in states:
            new_states += state.reducto(1)

        return new_states

    def reducto(self, level=1):
        for led in range(len(self._current_state)):
            buttons_indexes = self._buttons_idx_for_idx_led(led)
            target = self._wanted_state[led] - self._current_state[led]
            len_but_idx = len(buttons_indexes)
            if len(buttons_indexes) != level:
                continue
            max_pushes = [self._get_max_push(bi) for bi in buttons_indexes]
            max_push = max(max_pushes)
            clones = []
            def isValidSeq():
                if sum(seq) != target:
                    return False
                for i in range(len_but_idx):
                    if seq[i] > max_pushes[i]:
                        return False
                return True
            for seq in itertools.combinations(range(max_push + 1), len_but_idx):
                if not isValidSeq:
                    continue
                clone = copy.deepcopy(self)
                for s in range(len(seq)):
                    clone._pressed_button(buttons_indexes[s], seq[s])
                clones.append(clone)
            return clones


def main():
    lines = read_file()
    machines = parse_machines(lines)
    sum_ = 0
    for machine in machines:
        comb = calc_combinaisons(machine["buttons"])
        buttons_to_press = solve(machine, comb)
        sum_ += len(buttons_to_press)
    print('Star 1: ', sum_)

    sum_jolt = 0
    for machine in machines:
        s = Machine(machine["jolts"], machine["buttons"])
        print(s.solve())
        break
    print('Star 2: ', sum_jolt)


main()
