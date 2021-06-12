#!/usr/bin/env python3
from numpy import NaN
from pandas import read_csv
from os import listdir, makedirs
from os.path import isdir, join


INPUT_DIR = 'f1db_csv'
OUTPUT_DIR = 'clean_f1db'

if __name__ == '__main__':
    # Create output directory if it does not exist
    if not isdir(OUTPUT_DIR):
        makedirs(OUTPUT_DIR)

    # For each file in INPUT_DIR, replace \N with NaN and save
    for fn in listdir(INPUT_DIR):
        df = read_csv(join(INPUT_DIR, fn))
        df.replace(r'\N', NaN, inplace=True)
        df.to_csv(join(OUTPUT_DIR, fn), index=False)

    print(f"Cleaned data is now stored in {OUTPUT_DIR}/")

