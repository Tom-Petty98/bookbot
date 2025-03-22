def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    word_list = text.split()
    return len(word_list)

def main():
    text = get_book_text()
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()