import sys
from stats import getNumWords, countCharacter, sortItems

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(get_book_text(book_path))

    counts = countCharacter(book_path)

    print(counts)

    print()
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    getNumWords(book_path)
    print("--------- Character Count -------")
    sortItems(counts)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

main()
