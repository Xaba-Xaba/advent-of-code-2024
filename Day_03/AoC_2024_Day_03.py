import re

FILE_NAME = 'data/day03.txt'

f = open(FILE_NAME, "r")
text = f.read()
f.close()

text = text.replace('\n', '')

pattern_mul = r"""
    mul            # matches the literal string 'mul'
    \(             # \( escapes the ( to match it as a literal opening parenthesis. 
    (\d{1,3})      # \d{1,3}: matches 1 to 3 digits
    ,              # matches the comma
    (\d{1,3})
    \)

"""
pattern_mul = re.compile(pattern_mul, re.VERBOSE)

matches = []

matches += re.findall(pattern_mul, text)

print(len(matches))

sum = 0

for a, b in matches:
    sum += int(a) * int(b)
    
print('Results of the multiplications: ', sum)

text = "do()" + text + "don't()"

pattern_do_dont = r"""
    do\(\)
    .*?
    don't\(\)

"""
pattern_do_dont = re.compile(pattern_do_dont, re.VERBOSE)

matches_do_dont = re.findall(pattern_do_dont, text)
print(len(matches_do_dont))

sum2 = 0

for item in matches_do_dont:
    for a,b in re.findall(pattern_mul, item):
        sum2 += int(a)*int(b)

print('Results of the multiplications: ', sum2)