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
        self._reduction_level = 1

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
        return f"""Machine(
            {self._wanted_state=},
            {self._current_state=},
            {self._buttons_pressed=},
            {self._reduction_level}
        )"""

    def __str__(self):
        return f"""Machine(
            {self._wanted_state=},
            {self._current_state=},
            {self._buttons_pressed=},
            {self._reduction_level=}
        )"""

    def __eq__(self, other):
        return self._buttons_pressed == other._buttons_pressed \
            and self._wanted_state == other._wanted_state \
            and self._current_state == other._current_state \
            and self._reduction_level == other._reduction_level

    def __hash__(self):
        return hash((tuple(self._buttons_pressed), tuple(self._wanted_state), tuple(self._current_state), self._reduction_level))

    def _get_max_push(self, idx):
        max_push = None
        for led_idx in self._buttons[idx]:
            n = self._wanted_state[led_idx] - self._current_state[led_idx]
            if max_push is None or n < max_push:
                max_push = n
        return max_push

    def check(self):
        if self._current_state == self._wanted_state:
            return 1
        if self._reduction_level > len(self._buttons) or all(b is not None for b in self._buttons_pressed):
            return -1
        return 0

    def solve(self):
        candidates = set([self])
        valid_candidates = set([])
        while len(candidates) > 0:
            print(f"{len(candidates)=}")
            new_candidates = set()
            for candidate in candidates:
                # print(f"{candidate=}")
                children = candidate.reducto()
                for c in children:
                    n = c.check()
                    if n == 1:
                        valid_candidates.add(c)
                    if n == 0:
                        new_candidates.add(c)

            candidates = new_candidates
        return min([sum(vcb if vcb is not None else 0 for vcb in vc._buttons_pressed) for vc in valid_candidates])

    def reduction_by_pression(self):
        buttons_indexes_min = len(self._buttons)
        choosen_led = None
        for led in range(len(self._current_state)):
            if len(self._buttons_idx_for_idx_led(led)) > 0 and buttons_indexes_min > len(self._buttons_idx_for_idx_led(led)):
                buttons_indexes_min = len(self._buttons_idx_for_idx_led(led))
                choosen_led = led
        if choosen_led is None:
            raise Exception('choose led false')
        buttons_len_max = 0
        buttons_idx_len_max = None
        for button_idx in self._buttons_idx_for_idx_led(choosen_led):
            if len(self._buttons[button_idx]) > buttons_len_max:
                buttons_len_max = len(self._buttons[button_idx])
                buttons_idx_len_max = button_idx
        if buttons_idx_len_max is None:
            print(self)
            raise Exception('button idx len max false')
        max_push = self._get_max_push(buttons_idx_len_max)
        clones = []
        for p in range(max_push + 1):
            clone = copy.deepcopy(self)
            clone._pressed_button(buttons_idx_len_max, p)
            clone._reduction_level = 1
            clones.append(clone)
        return clones

    def reducto(self, hard=False):
        if hard:
            return self.reduction_by_pression()

        for led in range(len(self._current_state)):
            buttons_indexes = self._buttons_idx_for_idx_led(led)
            target = self._wanted_state[led] - self._current_state[led]
            len_but_idx = len(buttons_indexes)
            if len(buttons_indexes) != self._reduction_level:
                continue
            max_pushes = [self._get_max_push(bi) for bi in buttons_indexes]
            max_push = max(max_pushes)
            clones = []
            # print(f"{buttons_indexes=}")
            # print(f"{max_push=}")

            def isValidSeq(seq):
                if sum(seq) != target:
                    return False
                for i in range(len_but_idx):
                    if seq[i] > max_pushes[i]:
                        return False
                return True
            for seq in itertools.permutations(range(max_push + 1), len_but_idx):
                # print(seq)
                if not isValidSeq(seq):
                    continue
                clone = copy.deepcopy(self)
                for s in range(len(seq)):
                    clone._pressed_button(buttons_indexes[s], seq[s])
                    clone._reduction_level = 1
                clones.append(clone)
            return clones

        self._reduction_level += 1
        if self._reduction_level > 2:
            return self.reducto(True)
        return [self]


def main():
    lines = read_file()
    machines = parse_machines(lines)
    # sum_ = 0
    # for machine in machines:
    #     comb = calc_combinaisons(machine["buttons"])
    #     buttons_to_press = solve(machine, comb)
    #     sum_ += len(buttons_to_press)
    # print('Star 1: ', sum_)

    sum_jolt = 0
    for i in range(len(machines)):
        print(f"machine: {i+1}")
        s = Machine(machines[i]["jolts"], machines[i]["buttons"])
        pushes = s.solve()
        print(f"\t{pushes=}")
        sum_jolt += pushes
    print('Star 2: ', sum_jolt)


main()
