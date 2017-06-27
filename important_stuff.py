import copy
import random
import fractions

def GWN(n, begin, end):
    #Generate White Noise - return list of random n elements from range from begin to end
    GWN_answer = []
    for i in range(n):
        GWN_answer.append(random.choice(range(begin, end)))
    return copy.deepcopy(GWN_answer)

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

def GPNVM(n, begin, end, difference):
    #Generate Pink Noise using Voss-McCartney algorithm
    space = end - begin
    answer_GPNVM = []
    dices = []
    number_of_full_dices = space // difference
    for i in range(number_of_full_dices):
        dices.append([random.choice(range(difference + 1)), difference])
    last_dice = number_of_full_dices % difference
    if not last_dice == 0:
        dices.append([random.choice(range(last_dice + 1)), last_dice])
        number_of_full_dices += 1
    dice_number = 0
    for i in range(n):
        while i % 2 == 0 and dice_number < (number_of_full_dices - 1):
            i = i // 2
            dice_number += 1
        dices[dice_number][0] = random.choice(range(dices[dice_number][1]))
        answer_GPNVM.append(sum([x[0] for x in dices]))
        dice_number = 0
    return copy.deepcopy(answer_GPNVM)

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
        GRL_answer.append(full_rotations(TrEu(GER(i, metre0[0]), (4.0 / metre0[1]))))
    return copy.deepcopy(GRL_answer)

def piano_range(scale):
    answer_pr = []
    for i in range(2, 8):
        for note in scale:
            answer_pr.append(note + str(i))
    return copy.deepcopy(answer_pr)

