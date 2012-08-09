# Write a procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' follows 'z', and that n can be positive,
#negative or zero.

def shift_n_letters(letter, n):
    small = 97;
    big =122;
    num = ord(letter);
    num = num + n;
    if num > big:
        return chr(small + (num-big) -1);
    if num < small:
        return chr(big - (small - num)+1);
    return chr(num);


print shift_n_letters('s', 1)
#>>> t
print shift_n_letters('s', 2)
#>>> u
print shift_n_letters('s', 10)
#>>> c
print shift_n_letters('a', -1)
#>>> i
