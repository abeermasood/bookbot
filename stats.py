def count_words_in_book(text):
    words = len(text.split())
    return words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_characters(text):
    text = text.lower()
    count = {}

    for char in text:
        if char.isalpha():
            count[char] = count.get(char, 0) + 1

    return count

def sort_on(item):
    return item["count"]

def sorted_list_of_characters(character_dict):
    sorted_list = [{"character": char, "count": count} for char, count in character_dict.items()]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list