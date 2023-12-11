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