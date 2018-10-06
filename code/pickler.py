import cPickle as pickle

f = open('brit-a-z.txt')
valid_words = {}
for word in f:
    word = word.strip()
    l = len(word)
    if l < 5 or l > 9 or "'" in word:
        continue
    sorted_word = ''.join(sorted(word))
    if sorted_word not in valid_words:
        valid_words[sorted_word] = [word]
    else:
        valid_words[sorted_word].append(word)
# Improve performance slightly by storing the
# valid words as tuples instead of lists.
for key, value in valid_words.items():
    valid_words[key] = tuple(value)
pickle.dump(valid_words, open('word_dict.p', 'w'), -1)