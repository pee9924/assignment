from abc import ABC, abstractmethod


# Abstract base class FileHandler
class FileHandler(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


# Concrete class TextFileHandler
class TextFileHandler(FileHandler):
    def read(self):
        return "Reading text file."

    def write(self, data):
        return f"Writing text: {data}"


# Concrete class BinaryFileHandler
class BinaryFileHandler(FileHandler):
    def read(self):
        return "Reading binary file."

    def write(self, data):
        return f"Writing binary data: {data}"


# Creating instances of file handlers
text_handler = TextFileHandler()
binary_handler = BinaryFileHandler()

# Using file handlers
print(text_handler.read())  # Output: Reading text file.
print(text_handler.write("Hello"))  # Output: Writing text: Hello
print(binary_handler.read())  # Output: Reading binary file.
print(binary_handler.write("101010"))  # Output: Writing binary data: 101010
