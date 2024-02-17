def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    word_list = text.split()
    num_words = len(word_list)
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document")
    
    text = text.lower()
    
    characters = {}
    for character in text:
        if character.isalpha():
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1

    character_list = []
    for character, occurences in characters.items():
        character_list.append({'character': character, 'occurrences': occurences})

    def sort_on(dict):
        return dict["occurrences"]
    
    character_list.sort(reverse=True, key=sort_on)

    for character in character_list:
        print(f"The {character['character']} was found {character['occurrences']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()