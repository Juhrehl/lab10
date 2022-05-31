#modified word count (with user input)

def word_count():
  search_word_count = input("Enter a word (word doesn't have to be in the file): ")
  file = open("paragraph.txt", "r")
  read_data = file.read()
  word_count = read_data.lower().count(search_word_count)
  print(f"The word '{search_word_count}' appeared {word_count} time(s) in the file.")

word_count()