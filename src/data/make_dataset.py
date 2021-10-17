# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path

from numpy import NaN
from pandas import read_csv


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath: str, output_filepath: str):
    """
    description: runs data processing scripts to turn raw data from (../raw)
      into cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info("Making final data set from raw data")
    input_filepath = Path(input_filepath)
    output_filepath = Path(output_filepath)

    # For each file in input_filepath, replace \N with NaN and save
    for _file in input_filepath.iterdir():
        df = read_csv(_file)
        df.replace(r'\N', NaN, inplace=True)
        df.to_csv(output_filepath / _file.name, index=False)
    logger.info("Done")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    main()
