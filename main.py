def get_book_text(path):
    # Open the file using a with block
    with open(path) as f:
        # Read the contents and return them
        return f.read()
def get_word_count(text):
    words = text.split()
    return len(words)
def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")
main()
