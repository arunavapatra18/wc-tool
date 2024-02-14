import os

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

    def read_bytes(self):
        """Method to find the number of bytes in a file

        Returns:
            int: Number of bytes in the file
        """
        _file = self.file_to_process
        if os.path.exists(os.path.join(os.getcwd(),_file)):
            with open(_file, 'rb') as open_file:
                num_bytes = open_file.seek(0,2)
                print(num_bytes, _file)
            return num_bytes
        else:
            assert _file == None
