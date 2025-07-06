from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    bookpath = sys.argv[1]
    book_text = get_book_text(bookpath)
    num_words = word_count(book_text)
    characters_sorted = sort_dictionary(character_count(book_text))
    
    message = (
    "============ BOOKBOT ============\n"

    f"Analyzing book found at {bookpath}\n"
    "----------- Word Count ----------\n"
    f"Found {num_words} total words\n"
    "--------- Character Count -------"
)
    print(message)
    for dictionaries in characters_sorted:
        if dictionaries["char"].isalpha():
            print(f"{dictionaries["char"]}: {dictionaries["num"]}")

        
main()