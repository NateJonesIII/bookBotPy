# Book Bot

## Table of Contents

- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Methodologies](#methodologies)
- [Code Sample](#code)
- [Creator](#creator)

## Project Description

"Book Bot" - a Python program that can analyze an entire book and print out an insightful statistical report. A few of the learning goals are:

- Python Development: Gain hands-on experience in developing Python scripts to perform specific tasks, such as reading file contents, analyzing text data, and generating reports.

- Version Control with Git: Learn how to use Git for version control, including committing changes, creating branches, and pushing code to GitHub.

- Professional Development Environment: Set up a professional development environment on your local computer, including configuring a code editor like VS Code and installing necessary dependencies.

- Real-World Application: Apply your Python programming skills to solve a real-world problem by developing a useful tool that can analyze and extract insights from textual data.

## Installation

1. Clone the repository to your local machine.
2. Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
3. Open a terminal or command prompt and navigate to the project directory.
4. Run `python book_bot.py` to execute the program.

## Usage

- The `book_bot.py` script analyzes a book and prints out a statistical report.
- Currently, it is configured to analyze the book "Frankenstein". You can replace the book with any other text file by updating the `book_path` variable in the `main()` function.

## Technologies Used

- Python: The primary programming language used for developing the "Book Bot" program, leveraging its rich set of libraries for text processing and analysis.

- Git: Version control system used for managing project changes, tracking revisions, and collaborating with other developers.

- GitHub: Hosting platform for the project repository, allowing you to share your code with others, receive feedback, and showcase your work.

- VS Code: Professional code editor used for writing, debugging, and organizing Python code, providing features such as syntax highlighting, code completion, and integrated Git support.

## Methodologies

- Function-Based Programming: Utilize functions to modularize code, improve readability, and encapsulate specific tasks, such as file reading, text processing, and report generation.

- Iterative Development: Follow an iterative development approach by implementing features incrementally, testing each component, and gradually refining the program's functionality.

- Test-Driven Development (TDD): Emphasize writing tests to validate the correctness of individual functions and ensure robustness and reliability throughout the development process.

- Continuous Integration (CI): Set up automated CI pipelines to run tests automatically whenever changes are made to the codebase, ensuring early detection of bugs and errors.

## Code Sample

```python
def main():
    book_path = "books/frankenstein.txt"
    # store read file contents to variable
    file_contents = get_book_text(book_path)
    # store the length of words from file to variable
    num_words = get_num_words(file_contents)
    # store dict values in variable
    charDict = get_letter_count(file_contents)

    #
    #print(f"The count of letters {charsCount}")
    print_report(book_path,num_words,charDict)

# returns the number of words
def get_num_words(file_contents):
    words = file_contents.split()
    return len(words)

# add path to document to open file
def get_book_text(path):
    with open(path) as f:
        # return file contents
        return  f.read()

def get_letter_count(text):
    # create empty dict
    charCount = {}

    # loop through text; lower each char found in text
    for char in text.lower():
        # check if a string only contains characters from the alphabet
        if char.isalpha():
            # increment the count for the current char found in text
            charCount[char] = charCount.get(char, 0) + 1
    # return dictionary
    return charCount

def print_report(book_path, num_words, charDict):
    # initialize list to store charDict
    charList = list(charDict.items())
    # sort the list
    charList.sort()
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    print()
    for char in charList:
        temp = []
        temp = print(f"The '{char[0]}' character was found {char[1]} times")

    return temp
    #print(f"The {charList[0][0]} character was found {charList[1]} times")
    print("--- End report ---")


main()
```

## Creator

- [Profile](https://github.com/NateJonesIII/ "Nathaniel Jones") - [LinkedIn](https://www.linkedin.com/in/nathaniel-jones/) - [Email](mailto:15nate.jones@gmail.com?subject=Hello "Hello Nate!")
