#!/bin/python3
import copy
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def collect(s):
    for r in s["rob"].keys():
        s["res"][r] += s["rob"][r]

def add_robots(s, rs):
    for r in rs.keys():
        s["rob"][r] += rs[r]

def can_spend(s, rec):
    for ing in rec.keys():
        if rec[ing] > s["res"][ing]:
            return False
    return True

def spend(s, rec):
    new_s = copy.deepcopy(s)
    for ing in rec.keys():
        new_s["res"][ing] -= rec[ing]
    return new_s

def build_robots(s, b, nr = {}):
    new_build = [(s, nr)]
    for rob_rec in b.keys():
        if can_spend(s, b[rob_rec]):
            new_s = spend(s, b[rob_rec])
            new_r = copy.deepcopy(nr)
            if rob_rec in new_r:
                new_r[rob_rec] += 1
            else:
                new_r[rob_rec] = 1
            new_build += build_robots(new_s, b, new_r)
    return new_build


def build_scenario(blu: dict, sce):
    new_sce = []
    # print("sce", sce)
    for s in sce:
        # print("s_", s)
        builds = build_robots(s, blu)
        for b in builds:
            # print('build', b)
            ns = b[0]
            nr = b[1]
            collect(ns)
            add_robots(ns, nr)
            if ns["res"]["ore"] < 10 and \
               ns["res"]["clay"] < 50:
                new_sce.append(ns)
    # print('ns', new_sce)
    return new_sce

def clean_scenarios(sces):
    new_sces = []
    for sce in sces:
        if sce not in new_sces:
            new_sces.append(sce)
    return new_sces

def main():
    keys = ["ore", "clay", "obsidian", "geode"]
    blueprints = {}
    lines = read_file()
    for l in lines:
        pre_id, pre_blu = l.split(':')
        id_ = int(pre_id.split()[1])
        blueprints[id_] = {}
        for inst in pre_blu.split('.'):
            if inst == '':
                continue
            robot = inst.split()[1]
            blueprints[id_][robot] = {}
            for cost in inst.split('costs')[1].split('and'):
                n, i = cost.split()
                blueprints[id_][robot][i] = int(n)
    start = {"res": {}, "rob": {}}
    for k in keys:
        start["res"][k] = 0
        start["rob"][k] = 0
    start["rob"]["ore"] = 1
    for blu_id in blueprints.keys():
        scenarios = [start]
        for m in range(20):
            # print('s', scenarios)
            scenarios = build_scenario(blueprints[blu_id], scenarios)
            scenarios = clean_scenarios(scenarios)
            print(len(scenarios))
        break


    # print('Star 1: ', scenarios)

main()
