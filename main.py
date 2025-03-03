import sys
from stats import count_words_in_book, count_characters, get_book_text, sorted_list_of_characters

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    try:

        text = get_book_text(path_to_book)
    except FileNotFoundError:
        print(f"Error: The file '{path_to_book}' was not found.")
        sys.exit(1)

    total_words = count_words_in_book(text)
    dict_of_characters = count_characters(text)
    sorted_list = sorted_list_of_characters(dict_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        print(f"{item['character']}: {item['count']}")    

    print("============= END ===============")

if __name__ == "__main__":
    main()
