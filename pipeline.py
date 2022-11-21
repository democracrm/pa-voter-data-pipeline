from argparse import ArgumentParser
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile, BadZipfile

# Not yet functional
def load_archive(path):
    archive_path = Path('data/archives/PA_SURE_2022-10-27.zip')
    output_path = Path('data/output')

    try:
        archive = ZipFile(archive_path)
    except BadZipfile:
        print('Loading file failed.')

    # Inspect file and report out
    print(archive.printdir())

    # Create temporary directory and process archive
    with TemporaryDirectory() as tmpdirname:
        print('created temporary directory', tmpdirname)
        archive.extractall(tmpdirname)
        tmpdir = Path(tmpdirname)
        for f in tmpdir.iterdir():
            print(f)

# Not yet functional
def load_directory(path):
    directory = Path(args.path)

    for f in directory.iterdir():
        print(f)


parser = ArgumentParser()
subparsers = parser.add_subparsers()

archive_parser = subparsers.add_parser('archive')
directory_parser = subparsers.add_parser('directory')

directory_parser.add_argument('path')
directory_parser.set_defaults(func=load_directory)

if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
