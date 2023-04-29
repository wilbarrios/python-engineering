from utils import sample
import csv

def rcsv():    
  example_file = open('example.csv')
  reader = csv.reader(example_file)
  return list(reader)

sample(
  'Read all csv file',
  lambda : rcsv()
)

def rlcsv():
  example_file = open('example.csv')
  reader = csv.reader(example_file)
  for row in reader:
    print('Row #: {} {}'.format(reader.line_num, str(row)))

sample(
  'Read csv file line by line',
  lambda : rlcsv()
)
