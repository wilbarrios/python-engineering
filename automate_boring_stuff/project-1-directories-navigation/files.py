from helpers import sample

def rfile():
  hello_file = open('hello.txt')
  return hello_file.read()

sample(
  'Reading a file',
  lambda : rfile()
)

def rfile_multiline():
  hello_file = open('hellomultilines.txt')
  return hello_file.readlines()

sample(
  'Readign a file as list of lines',
  lambda : rfile_multiline()
)

def wsample():
  print('Write mode')
  file = open('bacon.txt', 'w')
  file.write('Hello bacon file!\n')
  file.close()
  print('Append mode')
  file = open('bacon.txt', 'a')
  file.write('Bacon was appended! 🥓')
  file.close()
  print('Read mode')
  file = open('bacon.txt', 'r') # default
  return file.read()

sample(
  'Write and append to file',
  lambda : wsample()
)
  
