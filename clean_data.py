#!/usr/bin/env python
import sys
import numpy as np
import pandas as pd
from os import listdir, makedirs
from os.path import isfile, isdir, join


def clean_data(input_dir='f1db_csv/', output_dir='clean_f1db/'):
    """For each file in input_dir, replace \\N with NaN and save"""
    if not isdir(output_dir):
        makedirs(output_dir)

    # For each file, set column names and handle missing values
    for filename in listdir(input_dir):
        df = pd.read_csv(join(input_dir, filename))
        df.replace(r'\N', np.NaN, inplace=True)
        df.to_csv(join(output_dir, filename), index=False)

    print("Cleaned data is now stored in " + output_dir)


if __name__ == '__main__':
    clean_data()
