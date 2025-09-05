def get_num_words(book):
    with open(f"{book}") as b:
        text = b.read()
        words = text.split()
        word_count = len(words)
        return word_count
def get_book_text(book):
    with open(f"{book}") as f:
        contents = f.read()
        return contents
def character_count(book):
    text = get_book_text(book).lower()
    counts = {
        "a" : text.count("a"),
        "b" : text.count("b"),
        "c" : text.count("c"),
        "d" : text.count("d"),
        "e" : text.count("e"),
        "f" : text.count("f"),
        "g" : text.count("g"),
        "h" : text.count("h"),
        "i" : text.count("i"),
        "j" : text.count("j"),
        "k" : text.count("k"),
        "l" : text.count("l"),
        "m" : text.count("m"),
        "n" : text.count("n"),
        "o" : text.count("o"),
        "p" : text.count("p"),
        "q" : text.count("q"),
        "r" : text.count("r"),
        "s" : text.count("s"),
        "t" : text.count("t"),
        "u" : text.count("u"),
        "v" : text.count("v"),
        "w" : text.count("w"),
        "x" : text.count("x"),
        "y" : text.count("y"),
        "z" : text.count("z"),
        "æ" : text.count("æ"),
        "â" : text.count("â"),
        "ê" : text.count("ê"),
        "ë" : text.count("ë"),
        "ô" : text.count("ô")
    }

    return counts

def sort_on(item):
    return item["num"]

def sort_characters(book):
    count = character_count(book)
    counts_list = []
    for ch, num in count.items():
        if not ch.isalpha():
            continue
        else:   
            counts_list.append({"char": ch, "num": num})
    counts_list.sort(reverse= True, key= sort_on)
    return counts_list