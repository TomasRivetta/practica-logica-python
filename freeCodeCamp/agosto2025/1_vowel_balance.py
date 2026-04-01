'''
Vowel Balance

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.
Tests:
    Waiting:1. is_balanced("racecar") should return True.
    Waiting:2. is_balanced("Lorem Ipsum") should return True.
    Waiting:3. is_balanced("Kitty Ipsum") should return False.
    Waiting:4. is_balanced("string") should return False.
    Waiting:5. is_balanced(" ") should return True.
    Waiting:6. is_balanced("abcdefghijklmnopqrstuvwxyz") should return False.
    Waiting:7. is_balanced("123A#b!E&*456-o.U") should return True.
'''

VOCALES = "aeiouAEIOU"

def is_balanced(s : str) -> bool:
    
    cant_vocales_primer_mitad = 0
    cant_vocales_segunda_mitad = 0
    
    lower_string = s.lower()
    
    cant_string = len(lower_string)
    
    if cant_string == 1:
        return True
    elif cant_string % 2 == 0:
        return False
    elif cant_string % 2 != 0:
        primer_mitad = lower_string[:cant_string//2]
        segunda_mitad = lower_string[cant_string//2+1:]
        
        for vocal in VOCALES:
            cant_vocales_primer_mitad += primer_mitad.count(vocal)
            cant_vocales_segunda_mitad += segunda_mitad.count(vocal)

    return cant_vocales_primer_mitad == cant_vocales_segunda_mitad

print(f'is_balanced("racecar"): {is_balanced("racecar")}') # should return True.
print(f'is_balanced("Lorem Ipsum"): {is_balanced("Lorem Ipsum")}') # should return True.
print(f'is_balanced("Kitty Ipsum"): {is_balanced("Kitty Ipsum")}') # should return False.
print(f'is_balanced("string"): {is_balanced("string")}') # should return False.
print(f'is_balanced(" "): {is_balanced(" ")}') # should return True.
print(f'is_balanced("abcdefghijklmnopqrstuvwxyz"): {is_balanced("abcdefghijklmnopqrstuvwxyz")}') # should return False.
print(f'is_balanced("123A#b!E&*456-o.U"): {is_balanced("123A#b!E&*456-o.U")}') # should return True.