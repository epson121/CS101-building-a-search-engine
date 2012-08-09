# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    num = ord(letter);
    if num == 122:
        return chr(97);
    return chr(num+1);



print shift('a')
#>>> b
print shift('n')
#>>> o
print shift('z')
#>>> a
