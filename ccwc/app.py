#!.venv/bin/python
import click

from .ccwc import wc

@click.command()
@click.option('-c','--bytes', is_flag = True, help='Print bytes count')
@click.argument('filename')

def cli(filename, bytes):
    """function to start the cli application

    Args:
        filename (str): file to process
        bytes (bool): enable/disable counting bytes
    """
    ccwc = wc()
    ccwc.get_file(filename)
    if bytes:
        ccwc.read_bytes()
