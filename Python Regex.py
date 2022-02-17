import re
"""""""""
test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"
match = re.search(r'tinitiate',test_string)

if match:
    print("The word 'tinitiate' is found in the string:", "\n", test_string)
else:
    print("The word 'tinitiate' is NOT found in the string:", "\n", test_string)

match = re.search(r'12*',test_string)

if match:
    print("The word '12*' is found in the string:", "\n", test_string)
else:
    print("The word '12*' is NOT found in the string:", "\n", test_string)

test_string = "The Test string 123 121212 tinitiate TINITIATE a1b2c3"
all_t = re.findall(r'\w+t\w+|\w+t|t\w+',test_string)
for lpr in all_t:
    print(lpr)

import re

# This is used to replace parts of strings, with a pattern
string = "Tinitiate good python examples"

# Replace "good" with "great"
new_string = re.sub("good", "great", string)
print(string)
print(new_string)
"""""""""""
import re

words2list = re.split(r's','Tinitiate good python examples')
print(words2list)

# Split a Comma Separated String

csv2list = re.split(r',','1,AAA,2000')
print(csv2list)



