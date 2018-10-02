found = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
print(found)

for k in found:
        print(k)
print('------------')

for k in found:
        print(k, 'was found', found[k], 'time(s).')
print('------------')

for k in sorted(found):
        print(k, 'was found', found[k], 'time(s).')
print('------------')

for k,v in sorted(found.items()):
        print(k, 'was found',v, 'time(s).')
