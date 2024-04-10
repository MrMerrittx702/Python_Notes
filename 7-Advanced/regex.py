'''Python regular expressions'''
import re


'''
Regex
. any single char except newline(like a wildcard)
[] char class matches any single character in the brackets.
[^] negated char class matches any char not in the brackets.
* matches 0 or more occurrences of the preceding character or group
+ matches one or more occurences of the preceding char or group
? matches 0 or 1 occurence of the preceding char or group
() groups characters or sub patterns. 
| matches either the expression before or after the symbol "or"
\ escape char to match exact literal
^ matches beginning of a line or string
$ matches the end of a line or string. 

\\ escapes the following char to match it literally
\d matches single digit 0-9
\D matches any single non digit
\w matches any single alphanumeric char including _ 
\W matches any single char that is non alphanumeric
\s matches any single whitespace char including space,tab,newline
\S matches any non whitespace char
{n} matches exactly n occurences of the preceding char or group
{n,m} matches between n and m occurences of the preceding char or group
'''

#For patterns in python us the prefix 'r' for raw string to avoid certain backslash errors
#raw strings are interpreted literally ignoring the backslash special meaning

#Pattern examples
wildcard = r"."
atoz = r"[a-z]"; AtoZ = r"[A-Z]"
digits = r"[0-9]"
not_inbrackets = r"[^aeiou]" #everything but vowels
zero_more = r"a*" #checking for a
zero_more = r"abc*" #checking for abc
one_more = r"a+"
one_more = r"abc+"
zero_one = r"a?"
zero_one = r"abc?"


#              g1      g2       g3          g4          g5       g6
grouping = r"(\w+)\s+(\w+),\s+(\d+)\s+(\w+\s+\w+\.)\s+(\w+),\s+(\w+)"

match_or = r"com|net|org"
literal = r"\.\?" #matches literal . then ?
beginning = r"^starting"
ending = r"$ending"

escape_backslash = r"C:\\" #escapes the \
n = 5
n_occurences = rf"a{n}"
n_occurences = r"a{5}"

#search and match examples

text = "userame@email.com"
pattern = r"(\w+)[@](\w+)[\.](com|net|org)"
match = re.search(pattern,text)

if match.group() == text:
    print("Valid Email : ", match.group())
else:
    print("Invalid Email")







