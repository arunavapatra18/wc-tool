#!.venv/bin/python
import click

from .ccwc import wc

@click.command()
@click.option('-c','--bytes', is_flag = True, help='Print byte count')
@click.option('-l','--lines', is_flag = True, help='Print line count')
@click.option('-w','--words', is_flag = True, help='Print word count')
@click.argument('filename')

def cli(filename, bytes, lines, words):
    ccwc = wc()
    ccwc.get_file(filename)
    
    res = ''
    
    if bytes:
        byte_count = ccwc.count_bytes()
        res = res + str(byte_count) + ' '
        
    if lines:
        line_count = ccwc.count_lines()
        res += str(line_count) + ' '

    if words:
        word_count = ccwc.count_words()
        res += str(word_count) + ' '
        
    res += filename
    print(res)
