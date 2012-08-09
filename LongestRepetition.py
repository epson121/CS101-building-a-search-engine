# Question 8: Longest Repetition

# Define a procedure, longest_repetition, that takes as input a 
# list, and returns the element in the list that has the most 
# consecutive repetitions. If there are multiple elements that 
# have the same number of longest repetitions, the result should 
# be the one that appears first. If the input list is empty, 
# it should return None.

def longest_repetition(l):
    if len(l) == 0:
        return;
    i = 0;
    maximum = 1;
    current = l[0];
    maxelem = l[0];
    i = 0;
    for elem in l:
        if elem == current:
            i = i+1;
        else:
            if i > maximum:
                maximum = i;
                maxelem = current;
            i = 1;
            current = elem;
    if i > maximum:
        maximum = i;
        maxelem = current;
    return maxelem;




#For example,

#print longest_repetition([1, 2, 2, 3, 3, 3, 2, 2, 1])
# 3

#print longest_repetition(['a', 'b', 'b', 'b', 'c', 'd', 'd', 'd'])
# b

print longest_repetition([2, 2, 3, 3, 3])
# 3

#print longest_repetition([])
# None

