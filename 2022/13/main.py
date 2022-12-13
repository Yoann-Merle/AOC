#!/bin/python3
import sys

def read_file():
    filename = 'input.txt'
    if len(sys.argv) == 2 and sys.argv[1] == '-t':
        filename = 'input-test.txt'
    with open(filename) as f:
        lines = f.read().splitlines()

    return lines

def is_ordered(packet1, packet2):
    if isinstance(packet1, int) and isinstance(packet2, int):
        if packet1 < packet2:
            return 1
        elif packet1 == packet2:
            return 0
        else:
            return -1
    if isinstance(packet1, int):
        return is_ordered([packet1], packet2)
    if isinstance(packet2, int):
        return is_ordered(packet1, [packet2])
    l_packet1 = len(packet1)
    l_packet2 = len(packet2)
    for i in range(l_packet1):
        if i >= l_packet2:
            break
        io = is_ordered(packet1[i], packet2[i])
        if io != 0:
            return io
    if l_packet1 == l_packet2:
        return 0
    elif l_packet1 < l_packet2:
        return 1
    else:
        return -1


def main():
    lines = read_file()
    pairs = []
    for i in range(0, len(lines), 3):
        packet_one = eval(lines[i])
        packet_two = eval(lines[i+1])
        pairs.append([packet_one, packet_two])
    right_order_pairs = 0
    for i in range(len(pairs)):
        if 1 == is_ordered(pairs[i][0], pairs[i][1]):
            right_order_pairs += i + 1
    print('Star 1: ', right_order_pairs)

    packets = []
    for l in lines:
        if l != '':
            packets.append(eval(l))
    divider_packets = [[[2]], [[6]]]
    organize_packets = divider_packets
    for packet in packets:
        packet_inserted = False
        for i in range(len(organize_packets)):
            if is_ordered(packet, organize_packets[i]) != -1:
                organize_packets = organize_packets[:i] + [packet] + organize_packets[i:]
                packet_inserted = True
                break
        if not packet_inserted:
            organize_packets.append(packet)

    decoder_key = 1
    for i in range(len(organize_packets)):
        if organize_packets[i] == divider_packets[0] or \
            organize_packets[i] == divider_packets[1]:
            decoder_key *= i+1
    print('Star 2: ', decoder_key)




main()
