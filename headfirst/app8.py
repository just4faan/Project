#! python3
vowels = set('aeiou')
word = input('Write something: ')

u = vowels.intersection(set(word))

for k in sorted(u):
    print(k)
