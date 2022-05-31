#word count

def word_count():
  file = open("paragraph.txt", "rt")
  data = file.read()
  words = data.split()
  print('Number of words in text file :', len(words))

word_count()


