# Write a program that prints the temperature closest to 0 among input data. If two numbers are equally close to zero, positive integer has 
# to be considered closest to zero (for instance, if the temperatures are -5 and 5, then display 5).



import sys
import math

tempsPos = []
tempsNeg = []

# conditions
both_same_abs = False
neg_is_closer = False
pos_is_closer = False

n = int(input())
for i in input().split():
    t = int(i)

    if t > 0:
        tempsPos.append(t)
    else:
        tempsNeg.append(t)

def temp_checker(n, tP, tN):
    if n == 0:
        print(0)
    else:

        # we sort the negative and positive data
        sortedPos = sorted(tempsPos)
        sortedNeg = sorted(tempsNeg)

        # we check which number from the lists is closer to zero
        # first with the positives
        counterPos = 0

        if len(tempsPos) < 1:
            counterPos = False
        else:
            positive_non_converted = sortedPos[0]
            for i in range(positive_non_converted):
                counterPos += 1

        # then with the negatives
        counterNeg = 0

        if len(tempsNeg) < 1:
            counterNeg = False
        else:
            positive_conversion = abs(sortedNeg[-1])
            for i in range(positive_conversion):
                counterNeg += 1

        # final checks
        if counterNeg == False and counterPos > 0:
            print(counterPos)
        elif counterPos == False and counterNeg > 0:
            print(sortedNeg[-1])
        elif sortedPos[0] == abs(sortedNeg[-1]):
            both_same_abs = sortedPos[0]
            print(both_same_abs)
        elif counterNeg < counterPos:
            neg_is_closer = counterNeg
            print(neg_is_closer)
        elif counterPos < counterNeg:
            pos_is_closer = counterPos
            print(pos_is_closer)


temp_checker(n, tempsNeg, tempsPos)
