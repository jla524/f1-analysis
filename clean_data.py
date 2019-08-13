import sys, pickle, itertools
import numpy as np
import pandas as pd
from os import listdir, makedirs
from os.path import isfile, isdir, join
from create_columns import create_columns


def load_columns(path):
	# Load the text files containing tables and column names
	# Or create them if they do not exist
	if not isfile('tables.txt') or not isfile('columns.txt'):
		create_columns()

	with open('tables.txt', 'rb') as file:
		tables =  pickle.load(file)

	with open('columns.txt', 'rb') as file:
		column_names =  pickle.load(file)

	# Make sure that number of files == number of lists in columns.txt
	assert len(tables) == len(column_names)

	return tables, column_names


def clean_data(input='f1db_csv/', output='clean_f1db/'):
	# Load file names and columns names
	tables, column_names = load_columns(input)

	# Create the output directory is it does not exist
	if not isdir(output):
		makedirs(output)

	# For each table, add the column names and replace NaN values
	for (table, names) in zip(tables, column_names):
		filename = table + '.csv'
		df = pd.read_csv(input + filename, header=None, names=names)
		df = df.replace(r'\N', np.NaN)
		df.to_csv(output + filename, index=False)


if __name__ == '__main__':
	num_inputs = len(sys.argv)

	if (num_inputs == 1):
		clean_data()	
	elif (num_inputs == 3):
		clean_data(sys.argv[0], sys.argv[1])
	else:
		print("Expected zero or two input arguments.")
