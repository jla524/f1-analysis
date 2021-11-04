"""
Define function to get dataset
"""
from io import BytesIO
from zipfile import ZipFile
from pathlib import Path

import click
from numpy import NaN
from pandas import read_csv
from urllib.request import urlopen


def download_data(data_dir):
    """
    @description: download the F1 dataset if it is not in the data/ directory
    """
    if data_dir.is_dir():
        return

    url = 'http://ergast.com/downloads/f1db_csv.zip'

    with urlopen(url) as response:
        with ZipFile(BytesIO(response.read())) as zip_file:
            zip_file.extractall(data_dir)


@click.command()
@click.argument('input_dir', type=click.Path())
@click.argument('output_dir', type=click.Path())
def main(input_dir, output_dir):
    """
    description: runs data processing scripts to turn raw data from (data/raw)
      into cleaned data ready to be analyzed (saved in data/processed).
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    download_data(input_path)
    output_path.mkdir(exist_ok=True)

    # For each file in input_filepath, replace \N with NaN and save
    for file in input_path.iterdir():
        data = read_csv(file)
        data.replace(r'\N', NaN, inplace=True)
        data.to_csv(output_path / file.name, index=False)


if __name__ == '__main__':
    main()
