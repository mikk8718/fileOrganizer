from pathlib import Path
import os
import shutil
import argparse

parser = argparse.ArgumentParser(description="Copy or delete a file based on input.")
parser.add_argument('--delete', action='store_true', help='Delete the file instead of copying it')
args = parser.parse_args()


if not os.path.exists('sortedFiles'):
    os.makedirs('sortedFiles')

destination = Path('sortedFiles')
directory = Path('filesToSort')

knownTypes = list()

for item in directory.iterdir():
    suffix = item.suffix[1:]
    if suffix not in knownTypes:
        (destination / suffix).mkdir(parents=True, exist_ok=True)  
        knownTypes.append(suffix)
    if args.delete:
        shutil.move(item, destination/suffix/item.name)
    else:
        shutil.copy(item, destination/suffix/item.name)




