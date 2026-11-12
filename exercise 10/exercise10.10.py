from pathlib import Path

def count_common_words(filename, word):
    path = Path(r'C:\Users\LENOVO\nexen\exercise 10\alice.txt')
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        word_count = contents.lower().count(word)
        print(f"'{word}' appears in {filename} about {word_count} times.")

count_common_words('alice.txt', 'the')