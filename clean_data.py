#!/usr/bin/env python3
from numpy import NaN
from pandas import read_csv
from pathlib import Path


def clean_data(input_path=Path('f1db_csv'), output_path=Path('clean_f1db')):
    output_path.mkdir(exist_ok=True)
    # For each file in input_dir, replace \N with NaN and save
    for file in input_path.iterdir():
        df = read_csv(file)
        df.replace(r'\N', NaN, inplace=True)
        df.to_csv(output_path / file.name, index=False)
    print("Cleaned data is now stored in", output_path)


if __name__ == '__main__':
    clean_data()
