#!.venv/bin/python
import click
import os

from .ccwc import wc

@click.command()
@click.option('-c','--bytes', is_flag = True, help='Print byte count')
@click.option('-l','--lines', is_flag = True, help='Print line count')
@click.option('-w','--words', is_flag = True, help='Print word count')
@click.option('-m','--chars', is_flag = True, help='Print char count')
@click.argument('filename')

def cli(filename, bytes, lines, words, chars):
    _file = filename
    res = ''

    if os.path.exists(os.path.join(os.getcwd(),_file)):
        with open(filename, 'rb') as open_file:
            byte_count, line_count, word_count, char_count = wc.extract_info(open_file=open_file)
            if bytes:
                res = res + str(byte_count) + ' '
            if lines:
                res += str(line_count) + ' '
            if words:
                res += str(word_count) + ' '
            if chars:
                res += str(char_count) + ' '
            if not bytes and not lines and not words and not chars:
                res = str(byte_count) + ' ' + str(line_count) + ' ' + str(word_count) + ' ' + str(char_count) + ' '
        res += filename
        print(res)    

    else:
        assert _file == None
