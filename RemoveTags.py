# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags. 
# You may assume the input does not include any unclosed tags, that is,  
# there will be no '<' without a following '>'.

def remove_tags(string):
    result = "";
    if string.find("<") == -1:
        return string.split(" ");
    else:
        while True:
            first = string.find("<");
            if first > 0:
                result = result + " " + string[0:first];
                string = string[first:];
            elif first == 0:
                second = string.find(">");
                string = string[second+1:];
                if (string.find("<") == -1):
                    result = result + " " + string;
            else:
                break;
        result = result.split(" ");
        res = [];
        for elem in result:
            if "\n" in elem:
                z = [];
                z = elem.split("\n");
                for elem in z:
                    res.append(elem);
            if elem != "":
                res.append(elem);
        k = [];
        for elem in res:
            if elem != "":
                k.append(elem);
        return k;




                
print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

print remove_tags('''<table cellpadding='3'>
                    <tr><td>Hello</td><td>World!</td></tr>
                     </table>''')
#>>> ['Hello','World!']

print remove_tags("<hello><goodbye>")
#>>> []

print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags("This <i>line</i> has <em>lots</em> of <b>tags</b>.");
