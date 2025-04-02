import sys;
from stats import get_word_count;
from stats import count_chars;
from stats import sort_dict;

# retrieves and returns file contents
def get_book_text(filepath):
    contents = ''
    with open(filepath) as f:
        contents = f.read()
    return contents;

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    # Get contents of the book
    contents = get_book_text(path_to_book)
    
    # Get word and char count of the book
    count = get_word_count(contents)
    chars = count_chars(contents)
    
    # Sort the characters
    sorted_chars = sort_dict(chars)

    # Print report to terminal
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        if entry["character"].isalpha() == True:
            print(f"{entry["character"]}: {entry["count"]}")
    print("============= END ===============")

main();