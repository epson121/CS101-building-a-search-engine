# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    h = [];
    while nbuckets > 0:
        z = [];
        h.append(z);
        nbuckets -= 1;
    return h;

print make_hashtable(5);
