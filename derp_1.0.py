import copy
import random
import fractions
import music21

def GBN(n, begin, end, startpoint, difference):
    #Generate Brown Noise - return list of n random elements from range from begin to end, but every adjoining elements can differs at most about difference and startpoint is a first element.
    GBN_answer = [startpoint]
    step = 0
    value = 0
    for i in range(1, n):
        step = random.choice(range(((-1) * difference), (difference + 1)))
        value = GBN_answer[i - 1] + step
        if value >= begin and value < end:
            GBN_answer.append(value)
        else:
            GBN_answer.append(value - (2 * step))
    return copy.deepcopy(GBN_answer)

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

def EuRh(a, b):
    #Function helping with euclidean rhythms generation
    len_b = len(b)
    EuRh_answer = ''
    if len_b == 0:
        for phrase in a:
            EuRh_answer = EuRh_answer + phrase
        return EuRh_answer
    if len_b == 1:
        for phrase in a:
            EuRh_answer = EuRh_answer + phrase
        return EuRh_answer + b[0]
    else:
        for i in range(len_b):
            a[i] = a[i] + b[i]
        b = a[len_b:]
        a = a[0:len_b]
        if len(a) >= len(b):
            return EuRh(a, b)
        else:
            return EuRh(b, a)

def GER(a, b):
    #Generate Euclidean Rhythm, with a beats spread over b places
    if a >= (b - a):
        return EuRh(['1'] * a, ['0'] * (b - a))
    else:
        GER_answer = EuRh(['0'] * (b - a), ['1'] * a)
        while GER_answer[0] == '0':
            GER_answer = GER_answer[1:] + GER_answer[0]
        return GER_answer

def TrEu(rhythm, base_duration):
    #Translate "binary" rhythm scheme to music21 notation
    TrEu_answer = []
    bench = base_duration
    for i in range(1, len(rhythm)):
        if rhythm[i] == '1':
            TrEu_answer.append(bench)
            bench = base_duration
        else:
            bench += base_duration
    TrEu_answer.append(bench)
    return copy.deepcopy(TrEu_answer)

def GRL(metre):
    #Generate Rhyths List - generates list of rhythms in metre
    metre0 = [int(x) for x in metre.split('/')]
    GRL_answer = []
    for i in range(1, metre0[0] + 1):
        GRL_answer = GRL_answer + full_rotations(TrEu(GER(i, metre0[0]), (4.0 / metre0[1])))
    return copy.deepcopy(GRL_answer)

print('metre bars')

metre = input()
bars = int(input())

print('rhythm_step melody_step')

rhythm_step = int(input())
melody_step = int(input())

rhythms = GRL(metre)

rhythm_changes = GBN(bars, 0, len(rhythms), len(rhythms) // 2, rhythm_step)

rhythm_line = []

for i in rhythm_changes:
    rhythm_line.append(rhythms[i])

rhythm_line_final = []

for i in rhythm_line:
    for j in i:
        rhythm_line_final.append(j)

scale_1 = [music21.note.Note(x, quarterLength = 0.25) for x in ["E3", "G3", "A3", "B3", "D4", "E4", "G4", "A4", "B4", "D5", "E5", "G5", "A5", "B5", "D6"]]

melody = GBN(len(rhythm_line_final), 0, len(scale_1), 5, melody_step)

stream_1 = music21.stream.Stream()

stream_1.append(music21.meter.TimeSignature(metre))

for i in range(len(melody)):
    melody[i] = copy.deepcopy(scale_1[melody[i]])
    melody[i].quarterLength = rhythm_line_final[i]
    stream_1.append(melody[i])

stream_1.show()

