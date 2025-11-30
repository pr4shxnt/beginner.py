a = int(input('Enter a number: '))

i = 0

while i <= a:
    if i % 2 == 0 and i != 0:
        print(f"{i} is an even number")
    i += 1



## args and kwargs



'''
to take multiple parameters


fun 1 par many


args - variable length positional argument


* - args
** - kwargs

args stores in tuples


kwargs - variable length keyword argument

kwargs stores in dict
'''