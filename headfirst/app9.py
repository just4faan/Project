def search4vowels(word):
         """Выводит гласные, найденные во введенном слове."""
         vowels = set('aeiou')
         found = vowels.intersection(set(word))
         for vowel in found:
              return vowel
