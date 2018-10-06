# PLAN
#
# 1. Read in words
# Each letter maps to the logarithm of a prime number; each word to the sum thereof
#

from math import log
from collections import defaultdict, Counter
from random import randint, sample
from itertools import combinations
import cProfile, pstats, StringIO
#pr = cProfile.Profile()
#pr.enable()

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
PRIMES = [2,3,5,7,11,
              13,17,19,23,29,
              31,37,41,43,47,
              53,59,61,67,71,
              73,79,83,89,97,101]
LOGPRIMES = map(log, PRIMES)
LOOKUP = dict(zip(LETTERS, LOGPRIMES))
RLOOKUP = dict(zip(LOGPRIMES, LETTERS))
global WORDDICT, VOWELS, CONSONANTS
WORDDICT = defaultdict(set)
VOWELS = [LOOKUP[i] for i in 'eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooouuuu']
CONSONANTS = [LOOKUP[i] for i in 'nnnnnnrrrrrrttttttllllssssddddgggbbccmmppffhhvvwwyykjxqz']
COUNTERS = defaultdict(Counter)

N = 1000000

def score_word(x):
    x = x.lower()
    if 5 <= len(x) <= 9:
        try:
            return sum( LOOKUP[i] for i in x )
        except:
            return 0.
    return 0.


def words_dict():
    f = open('brit-a-z.txt')
    W = [w.strip() for w in f]
    s = zip(map(score_word, W), W)
    for i, j in s:
        WORDDICT[i].add(j)

def iterate():
        
    n_vowels = randint(3,5)
    vowels = sample(VOWELS, n_vowels)
    consonants = sample(CONSONANTS, 9 - n_vowels)
    letters = vowels + consonants
    goodwords = set()    
    for i in range(9,4,-1):
        for c in combinations(letters, i):
            if sum(c) in WORDDICT:
                goodwords |= WORDDICT[sum(c)]
                            
        if goodwords:
            orig = "".join([ RLOOKUP[i] for i in letters ])
            return orig, goodwords
    orig = "".join([ RLOOKUP[i] for i in letters ])
    return orig, goodwords
words_dict()

for i in range(N):
    letters, words = iterate()
    if words:
        COUNTERS[len(words.pop())].update(words)

k=COUNTERS.keys()
k.sort()
for i in k:
    print i

    print "\n".join([("%s (%d) " % (s,t)) for (s,t) in COUNTERS[i].most_common(20)])
    
#pr.disable()
#s = StringIO.StringIO()
#sortby = 'cumulative'
#ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
#ps.print_stats()
#print s.getvalue()
