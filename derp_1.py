import random
import music21
import copy
n = int(input())
a = [5]

rotator = []

def rotate(lst):
    rotator = []
    n = len(lst)
    rotator.append(lst[n - 1])
    for i in range(n - 1):
        rotator.append(lst[i])
    return copy.deepcopy(rotator) 

def full_rotations(lst):
    x = [lst]
    bench = rotate(lst)
    while not bench == x[0]:
        x.append(bench)
        bench = rotate(bench)
    return copy.deepcopy(x)

rhythms = [ [2.0],
          [1.0, 1.0]]

rhythms = rhythms + full_rotations([0.75, 0.75, 0.5]) + [[0.5, 0.5, 0.5, 0.5]] + full_rotations([0.5, 0.25, 0.5, 0.25, 0.5]) + full_rotations([0.25, 0.25, 0.5] * 2)

rhythms = rhythms + full_rotations(([0.25] * 6) + [0.5]) + [[0.25] * 8] 

x = random.choice(range(22))
rhythm_line = [x]
number_of_notes = len(rhythms[x])
r_len = len(rhythms)

while number_of_notes < (n + 2):
    bench = random.choice(range(-5, 5))
    value = rhythm_line[-1] + bench
    if value >= 0 and value <= (r_len - 1):
        rhythm_line.append(value)
        number_of_notes += len(rhythms[value])
    else:
        rhythm_line.append(value - (2 * bench))
        number_of_notes += len(rhythms[value - (2 * bench)])

for i in range(len(rhythm_line)):
    rhythm_line[i] = rhythms[rhythm_line[i]]

rhythm_line_final = []

for i in rhythm_line:
    for j in i:
        rhythm_line_final.append(j)
#print(rhythm_line_final)
stream_1 = music21.stream.Stream()

scale_1 = [music21.note.Note(x, quarterLength = 0.25) for x in ["E3", "G3", "A3", "B3", "D4", "E4", "G4", "A4", "B4", "D5", "E5", "G5", "A5", "B5", "D6"]]

bench = 0
value = 0
for i in range(n):
    bench = random.choice(range(-3, 3))
    value = a[i] + bench
    if value >= 0 and value <= 14:
        a.append(value)
    else:
        a.append(value - (2 * bench))

for i in range(n + 1):
    a[i] = copy.deepcopy(scale_1[a[i]])
    a[i].quarterLength = rhythm_line_final[i]

for i in a:
    stream_1.append(i)

stream_1.show()
