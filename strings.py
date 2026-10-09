# Methods

s =" Hello World "

print(s.lower()) # all lowercase
print(s.upper()) # all uppercase
print(s.title()) # first letter of each word capitalized
print(s.strip()) #removes begnning and ending white spaces but spaces in the middle
print(s.replace('World', 'Mate')) # replaces the selected word
print(s.split()) #splits on whitespace by default
print("-" .join(['m', 'a', 't', 'e'])) #joins the list with given separator
print('123'.isdigit()) # checks if its a difit or special digit character
print('1 / 2'.isdigit())
print('①'.isdigit())
print('123'.isdecimal())
print('Ⅵ'.isnumeric()) # digits + fractions + romans
print('abc'.isalpha())  # checks if they are letters
print(" ".isspace())
print('hello'.startswith('he'))
print('hllo'.endswith('lo'))
