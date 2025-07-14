import sys
from stats import get_num_words, get_char_frequency, get_sorted_char_counts

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)  # Exit with status code 1
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    with open(book_path) as f:
        file_contents = f.read()

    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")

    print("--------- Character Count -------")
    my_dict = get_char_frequency(file_contents)
    sorted_chars = get_sorted_char_counts(my_dict)
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")

main()