from stats import get_word_count
from stats import get_characters_dict
from stats import sort_dict
import sys

def get_file_argument():
    if len(sys.argv) <= 1:
        sys.exit(1)
    return sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def format_output(word_count, char_dict):
    print("============ BOOKBOT ============\n"
    + "Analyzing book found at books/frankenstein.txt...\n"
    + "----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for key, val in char_dict.items():
        if key.isalpha():
            print(f"{key}: {val}")

    print("============= END ===============")

def main():
    file_path = get_file_argument()
    text = get_book_text(file_path)
    word_count = get_word_count(text)
    char_dict = get_characters_dict(text)
    sorted_dict = sort_dict(char_dict)
    format_output(word_count, sorted_dict)

main()