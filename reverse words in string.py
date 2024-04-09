def reverse_words(s):
  words = s.split()
  words.reverse()
  return ' '.join(words)

s = input("Enter a string: ")
print(reverse_words(s))