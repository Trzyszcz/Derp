import copy
import random

def GWN(n, begin, end):
    #Generate White Noise - return table of random n elements from range from begin to end
    GWN_answer = []
    for i in range(n):
        GWN_answer.append(random.choice(range(begin, end)))
    return copy.deepcopy(GWN_answer)

def GBN(n, begin, end, startpoint, difference):
    #Generate Brown Noise - return table of n random elements from range from begin to end, but every adjoining elements can differs at most about difference and startpoint is a first element.
    GBN_answer = [startpoint]
    step = 0
    value = 0
    for i in range(1, n):
        step = random.choice(range(((-1) * difference), difference))
        value = GBN_answer[i - 1] + step
        if value >= begin and value < end:
            GBN_answer.append(value)
        else:
            GBN_answer.append(value - (2 * step))
    return copy.deepcopy(GBN_answer)


