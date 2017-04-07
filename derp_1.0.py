import copy
import random
import music21
from important_stuff import *

print('metre bars')

metre = input()
bars = int(input())

print('scale')

scale_input = input().split()

print('rhythm_step melody_step')

rhythm_step = int(input())
melody_step = int(input())

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

melody = GPNVM(len(rhythm_line_final), 0, len(scale_1), melody_step)

stream_1 = music21.stream.Stream()

stream_1.append(music21.meter.TimeSignature(metre))

for i in range(len(melody)):
    melody[i] = copy.deepcopy(scale_1[melody[i]])
    melody[i].quarterLength = rhythm_line_final[i]
    stream_1.append(melody[i])

stream_1.show()

