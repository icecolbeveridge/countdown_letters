from random import sample, randint
from sys import argv
from itertools import combinations
import cPickle as pickle

def solve(letters):
    '''
    Function to return the 'winning' countdown words
    for a given string of letters.
    '''
    valid_words = pickle.load( open('word_dict.p') )
    letters = sorted(letters)
    for i in xrange(5, 10):
        print '\nLooking for %s letter words...\n'%(i)
        log = set()
        for combined_letters in combinations(letters, i):
            sorted_word = ''.join(combined_letters)
            if sorted_word in valid_words:
                for word in valid_words[sorted_word]:
                    log.add(word)
        found_words = ', '.join(
            sorted(word for word in log))
        print found_words
    

# Allow the option for the user to pass their own letters.
# If none are given, generate nine random letters
try:
    letters = argv[1]
except IndexError:
    VOWELS = 'eeeeeeeeeeeeaaaaaaaaaiiiiiiiiioooooooouuuu'
    CONSONANTS = 'nnnnnnrrrrrrttttttllllssssddddgggbbccmmppffhhvvwwyykjxqz'
    n_vowels = randint(2,4)
    vowels = sample(VOWELS, n_vowels)
    consonants = sample(CONSONANTS, 9 - n_vowels)
    letters = vowels + consonants
# Pass these letters to 'solve' function.
solve(letters)