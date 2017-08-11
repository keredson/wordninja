import gzip, os, re
from math import log



__version__ = '0.1.3'


# I did not author this code, only tweaked it from:
# http://stackoverflow.com/a/11642687/2449774
# Thanks Generic Human!



# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
with gzip.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'wordninja','wordninja_words.txt.gz')) as f:
  words = f.read().decode().split()
_wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
_maxword = max(len(x) for x in words)
_SPLIT_RE = re.compile("[^a-zA-Z0-9]+")



def split(s):
  """Uses dynamic programming to infer the location of spaces in a string without spaces."""
  l = [_split(x) for x in _SPLIT_RE.split(s)]
  return [item for sublist in l for item in sublist]



def _split(s):
    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-_maxword):i]))
        return min((c + _wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return reversed(out)

