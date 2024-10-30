class textfilereader:
    def _init_(self, file_path):
        self.file_path = file_path
        self.content = ""

    def read_file(self):
        """Read the content of the file and store it in the content attribute."""
        try:
            with open(self.file_path, 'r') as file:
                self.content = file.read()
        except FileNotFoundError:
            print("File not found. Please check the file path.")

    def count_lines(self):
        """Return the number of lines in the file."""
        if self.content:
            return len(self.content.splitlines())
        else:
            print("No content found. Please read the file first.")
            return 0

    def count_words(self):
        """Return the number of words in the file."""
        if self.content:
            return len(self.content.split())
        else:
            print("No content found. Please read the file first.")
            return 0

    def count_characters(self):
        """Return the number of characters in the file."""
        if self.content:
            return len(self.content)
        else:
            print("No content found. Please read the file first.")
            return 0

    def display_content(self):
        """Print the content of the file."""
        if self.content:
            print(self.content)
        else:
            print("No content found. Please read the file first.")

# Test the TextFileReader class
file_reader = textfilereader("sample.txt")  # Replace "sample.txt" with a valid file path
file_reader.read_file()
file_reader.display_content()
print("Lines:", file_reader.count_lines())
print("Words:", file_reader.count_words())
print("Characters:", file_reader.count_characters())
