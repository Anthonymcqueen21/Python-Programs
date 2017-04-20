 #!/bin/python


import sys


# Print 'Yes' if the word is beautiful or 'No' if it is not.

word=raw_input().strip()

v=["a","e","i","o","u","y"]

def check_beauty(w):
    current=w[0]
    for letter in range(1,len(w)):
        if current == w[letter]:
            return "No"
        
        elif current in v and w[letter] in v:
            return "No"
        else:
            current=w[letter]
    
