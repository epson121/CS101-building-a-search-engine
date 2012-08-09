def symmetric(l):
    z = len(l);
    for elem in l:
        if len(elem) != z:
            return False;
    x = [];
    z = [];
    i = 0;
    for el in l:
            for elem in l:
                x.append(elem[i]);
            i = i + 1;
            z.append(x);
            x = [];
    if z == l:
        return True;
    return False;
    
print symmetric([[1, 2, 3],
                [2, 3, 4],
                [3, 4, 1]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "fish"],
                ["fish", "fish", "cat"]])
#>>> True

print symmetric([["cat", "dog", "fish"],
                ["dog", "dog", "dog"],
                ["fish","fish","cat"]])
#>>> False

print symmetric([[1, 2],
                [2, 1]])
#>>> True

print symmetric([[1, 2, 3, 4],
                [2, 3, 4, 5],
                 [3, 4, 5, 6]])
#>>> False

print symmetric([[1,2,3],
                 [2,3,1]])
#>>> False

print symmetric([['cricket', 'football', 'tennis'], ['golf']]);
