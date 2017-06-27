#!/usr/bin/env python3

import copy
import random
import music21
import sys
from important_stuff import *

arguments = sys.argv[1:]

standard_arguments = ['16/16', '100', 'C D# F C A#', '4', '2']

for i in range(len(arguments)):
    standard_arguments[i] = arguments[i]

metre = standard_arguments[0]
bars = int(standard_arguments[1])

scale_input = standard_arguments[2].split()

rhythm_step = int(standard_arguments[3])
melody_step = int(standard_arguments[4])

rhythms = GRL(metre)

rhythm_changes = GPNVM(bars, 0, len(rhythms), rhythm_step)

rhythm_line = []

for i in rhythm_changes:
    rhythm_line.append(rhythms[i][random.choice(range(len(rhythms[i])))])

rhythm_line_final = []

for i in rhythm_line:
    for j in i:
        rhythm_line_final.append(j)

scale_1 = [music21.note.Note(x, quarterLength = 0.25) for x in piano_range(scale_input)]

melody = GBN(len(rhythm_line_final), 0, len(scale_1), random.choice(range(len(scale_1))), melody_step)

stream_1 = music21.stream.Stream()

stream_1.append(music21.meter.TimeSignature(metre))

for i in range(len(melody)):
    melody[i] = copy.deepcopy(scale_1[melody[i]])
    melody[i].quarterLength = rhythm_line_final[i]
    stream_1.append(melody[i])

stream_1.show()

