class wc():
    """
    wc class: Contains methods to process the input file
    """
    def extract_info(open_file):
        """Method to extract count of byte, line, word and char.

        Args:
            open_file (BufferedReader): The file to process

        Returns:
            int, int, int, int: byte count, line count, word count, char count
        """
        byte_count = 0
        line_count = 0
        word_count = 0
        char_count = 0

        for line in open_file:
            byte_count += len(line)
            line_count += 1
            word_count += len(line.split())
            char_count += len(line.decode())
        
        return byte_count, line_count, word_count, char_count
