from helpers import sample
import os

sample(
  'Make directory path',
  lambda : os.path.join('usr', 'bin', 'spam')
)

sample(
  'Get current directory',
  lambda : os.getcwd()
)

def chdir(path):
  try:
    os.chdir(path)
  except FileNotFoundError:
    print('Path: {} not found'.format(path))
  except e:
    print('Unknown error: {}'.format(e))

sample(
  'Change directory',
  lambda : chdir('NotValidPath')
)

def mkdir_if_needed(path):
  try:
    os.mkdir(path)
  except:
    None

def rdir(path):
  os.rmdir(path)

def create_and_remove_dir(path):
  mkdir_if_needed(path)
  print('Directory {} created'.format(path))
  rdir(path)
  print('Directory {} removed'.format(path))

sample(
  'Create and remove directory',
  lambda : create_and_remove_dir('./tmp-dir')
)

