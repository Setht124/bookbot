from stats import get_num_words
from stats import sort_characters
import sys
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_num_words(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {text} total words")
    print("--------- Character Count -------")
    for item in sort_characters(sys.argv[1]):
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ==============")
    return 

main()
