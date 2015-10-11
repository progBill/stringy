from math import sqrt
from collections import Counter

def cosineDistance(str1, str2):
    
    # turn the strings into vectors as dict('word': wordcount)
    str_vect1 = Counter(str1.split(' '))
    str_vect2 = Counter(str2.split(' '))

    # make a set of the intersection of both string vectors
    common = [x for x in str_vect1 if x in str_vect2]
    
    # numerator is the sum of products of words shared between strings
    numerator = sum(str_vect1[x] * str_vect2[x] for x in common)

    # denom.. product of sum of abs vals 
    vect1_sum = sqrt(sum([str_vect1[x]**2 for x in str_vect1.keys()]))
    vect2_sum = sqrt(sum([str_vect2[x]**2 for x in str_vect2.keys()]))
    denom = vect1_sum * vect2_sum

    if not denom: 
        return 0.0
    else: 
        return numerator * 1.0 / denom


def sp(*txt):
    print "{}".format(txt)

if __name__ == '__main__':

    txts = (
        "The sky is blue",
        "The sun is bright",
        "The sun in the sky is bright",
        "We can see the shining sun, the bright sun"
    )
    
    print "{} :: {}: {}".format(txts[0],txts[0],cosineDistance(txts[0], txts[0]))
    print "{} :: {}: {}".format(txts[1],txts[2],cosineDistance(txts[1],txts[2]))
    print "{} :: {}: {}".format(txts[1],txts[3],cosineDistance(txts[1],txts[3]))
    print "{} :: {}: {}".format(txts[0],txts[3],cosineDistance(txts[0],txts[3]))



