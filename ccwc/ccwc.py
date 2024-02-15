import os
import re

class wc():
    """
    wc class: Contains methods to process the input file
    """
    file_to_process: str

    def get_file(self, filename):
        """Method to get the filename from cli

        Args:
            filename (str): filename
        """
        self.file_to_process = filename

    def count_bytes(self):
        """Method to find the number of bytes in a file

        Returns:
            int: Number of bytes in the file
        """
        _file = self.file_to_process
        if os.path.exists(os.path.join(os.getcwd(),_file)):
            with open(_file, 'r') as open_file:
                num_bytes = open_file.seek(0,2)
            return num_bytes
        else:
            assert _file == None
            
    def count_lines(self):
        """Method to find the number of lines in a file

        Returns:
            int: Number of lines in the file
        """
        _file = self.file_to_process
        if os.path.exists(os.path.join(os.getcwd(),_file)):
            with open(_file, 'r') as open_file:
                num_lines = 0
                for line in open_file:
                    num_lines = num_lines + 1
            return num_lines
        else:
            assert _file == None

    def count_words(self):
        """Method to find the number of words in a file

        Returns:
            int: Number of words in the file
        """
        _file = self.file_to_process
        if os.path.exists(os.path.join(os.getcwd(),_file)):
            with open(_file, 'r') as open_file:
                num_words = 0
                for line in open_file:
                    words = line.split()
                    num_words += len(words)
            return num_words
        else:
            assert _file == None
