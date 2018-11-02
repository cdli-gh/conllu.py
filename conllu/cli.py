import os
import click
from stat import ST_MODE, S_ISREG

from convert import convert


def file_process(conllUFile, verbose=False):
    try:
        convert(conllUFile, "output")
    except Exception:
        click.echo('\nError: Error in processing {0}.'.format(conllUFile))


def check_and_process(pathname, verbose=False):
    mode = os.stat(pathname)[ST_MODE]

    if S_ISREG(mode) and pathname.lower().endswith('.conll'):
        # It's a file, call the callback function
        if verbose:
            click.echo('\nInfo: Processing {0}.'.format(pathname))

        conllUFile = pathname

        t = pathname.split('.')
        # conllFilePath = str(t[0]) + '.conll'

        # if not os.path.exists(conllFilePath):
        #     click.echo("Error: CoNLL file doesn't exist")

        file_process(conllUFile, verbose)


@click.command()
@click.option('--input_path', '-i', type=click.Path(exists=True, writable=True), prompt=True, required=True,
              help='Input the file/folder name.')
@click.option('--verbose', '-v', default=False, required=False, is_flag=True, help='Enables verbose mode')
@click.version_option()
def main(input_path, verbose):
    if os.path.isdir(input_path):
        with click.progressbar(os.listdir(input_path), label='Info: Converting the files') as bar:
            for f in bar:
                pathname = os.path.join(input_path, f)

                check_and_process(pathname, verbose)
    else:
        check_and_process(input_path, verbose)
