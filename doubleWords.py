#A coding Bat Problem

# Given a string, return a string where for every char in the original, there are two chars.


# double_char('The') → 'TThhee'
# double_char('AAbb') → 'AAAAbbbb'
# double_char('Hi-There') → 'HHii--TThheerree'


def double_char(str):
    double = ""
    sentence = ""
    for char in str:
        double = char + char 
        # Take every word and put it in the sentence
        sentence = sentence + double
    
    return sentence

print(double_char('The'))
print(double_char('AABBCC'))
print(double_char('Hi-There'))
print(double_char('Talha'))
    


