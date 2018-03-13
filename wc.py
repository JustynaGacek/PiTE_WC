#!/usr/bin/python3

import argparse
import sys


parser = argparse.ArgumentParser(description="count lines/characters in text file\n" +
                                             "default behaviour is to print:\n"
                                             "Characters\tLines\tMax line\tWords in that order")

parser.add_argument('-c', '--bytes', help='print the byte counts', action='store_true')
parser.add_argument('-m', '--chars', help='print the character counts', action='store_true')
parser.add_argument('-l', '--lines', help='print the newline counts', action='store_true')
parser.add_argument('-L', '--max-line-length', help='print the length of the longest line', action='store_true')
parser.add_argument('-w', '--words', help='print the word counts', action='store_true')
parser.add_argument('FILE', type=argparse.FileType('r'), nargs='?', default=sys.stdin,
                    help='if no file given, data is read form stdin')

args = parser.parse_args()

byte_count = 0

data = ''
with args.FILE as f:
    while True:
        buffer = f.read(1024)
        byte_count += len(buffer)
        if buffer == '':
            break
        data += str(buffer)

lines = data.split(sep='\n')

char_count = 0
word_counter = 0
max_line = 0
line_count = len(lines)

for line in lines:
    if max_line < len(line):
        max_line = len(line)
    char_count += len(line)
    word_counter += len(line.split())

flag = 0  # if no argument was called, then print all

if args.bytes:
    print(byte_count)
    flag += 1

if args.chars:
    print(char_count)
    flag += 1

if args.lines:
    print(line_count)
    flag += 1

if args.max_line_length:
    print(max_line-1)
    flag += 1

if args.words:
    print(word_counter)
    flag += 1


if flag == 0:
    print(char_count, line_count, max_line-1, word_counter, sep="\t")




