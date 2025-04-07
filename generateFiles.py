from pathlib import Path
import pandas as pd
import fileTypes
import os
import argparse

parser = argparse.ArgumentParser(description="enter amount of files to genereate")
parser.add_argument('--value', type=int, default=10, help='Enter a value (defaults to "default_value" if not provided)')

args = parser.parse_args()

if not os.path.exists('filesToSort'):
    os.makedirs('filesToSort')

df = pd.read_csv('fileTypes.csv')
for index, row in df.iterrows():
    for i in range(args.value):
        Path("filesToSort/{}.{}".format(i, row["fileType"])).touch()
