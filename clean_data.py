import sys
import pickle
import itertools
import numpy as np
import pandas as pd
from os import listdir, makedirs
from os.path import isfile, isdir, join


def clean_data(input='f1db_csv', output='clean_f1db'):
  if not isdir(output):
    makedirs(output)

  # For each file, set column names and handle missing values
  for filename in listdir('f1db_csv'):
    df = pd.read_csv(join(input, filename))
    df = df.replace(r'\N', np.NaN)
    df.to_csv(join(output, filename), index=False)


if __name__ == '__main__':
  num_inputs = len(sys.argv)

  if num_inputs == 1:
    clean_data()
    print("Cleaned data is now stored in clean_f1db/")
  elif num_inputs == 3:
    clean_data(sys.argv[1], sys.argv[2])
    print("Cleaned data is now stored in " + sys.argv[2] + '/')
  else:
    print("Expected either zero or two input arguments")
