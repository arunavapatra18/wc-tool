#!.venv/bin/python
import click

from .ccwc import wc

@click.command()
@click.option('-c','--bytes', is_flag = True, help='Print byte count')
@click.option('-l','--lines', is_flag = True, help='Print line count')
@click.argument('filename')

def cli(filename, bytes, lines):
    ccwc = wc()
    ccwc.get_file(filename)
    
    res = ''
    
    if bytes:
        byte_count = ccwc.count_bytes()
        res = res + str(byte_count) + ' '
        
    if lines:
        line_count = ccwc.count_lines()
        res += str(line_count) + ' '
        
    res += filename
    print(res)
