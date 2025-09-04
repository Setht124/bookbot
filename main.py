from stats import get_num_words
from stats import character_count
from stats import sort_characters
    
def main():
    text = get_num_words("frankenstein.txt")
    counts = sort_characters("frankenstein.txt")
    print("============ BOOKBOT ============")
    print("analyzing book found at book/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{text} words found in the document")
    print("--------- Character Count -------")
    print(counts)
    return 

main()
