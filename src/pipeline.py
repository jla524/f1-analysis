import gzip
import requests

from numpy import NaN
from pandas import read_csv

from f1_analysis import Config


class ETL:
    def extract_data(self) -> None:
        # TODO: get f1db_csv.zip and decompress it
        url = 'http://ergast.com/downloads/f1db_csv.zip'
        data = requests.get(url).content
        with (Config().data_directory() / 'f1db_csv.zip').open('w') as _file:
            _file.write(data)
        print(gzip.decompress(data))

    def transform_data(self) -> None:
        clean_data_dir = Config().clean_data_directory()
        clean_data_dir.mkdir(exist_ok=True)
        # For each file in input_dir, replace \N with NaN and save
        for file in self.__raw_data_dir.iterdir():
            df = read_csv(file)
            df.replace(r'\N', NaN, inplace=True)
            df.to_csv(clean_data_dir / file.name, index=False)
        print("Cleaned data is now stored in", clean_data_dir)
