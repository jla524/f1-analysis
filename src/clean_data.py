#!/usr/bin/env python3
from pathlib import Path

from numpy import NaN
from pandas import read_csv


def clean_data(input_path: Path, output_path: Path) -> None:
    output_path.mkdir(exist_ok=True)
    # For each file in input_dir, replace \N with NaN and save
    for file in input_path.iterdir():
        df = read_csv(file)
        df.replace(r'\N', NaN, inplace=True)
        df.to_csv(output_path / file.name, index=False)
    print("Cleaned data is now stored in", output_path)


if __name__ == '__main__':
    clean_data()
