"""
The Check Alphabet for Vowel or Consonant
"""

charecter = input('Enter Your charecter:')
if charecter in ('a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U'):
    print("it a vowel")

elif charecter in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print("it a consonant")


else:
    print("nothing")