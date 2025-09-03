def get_book_text(book):
    with open(f"books/{book}") as f:
        contents = f.read()
        return contents

def get_words(book):
    with open(f"books/{book}") as b:
        text = b.read()
        words = text.split()
        word_count = len(words)
        return word_count

def main():
    text = get_words("frankenstein.txt")
    print(f"{text} words found in the document")
    return 

main()
