def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_freq = count_letter_frequency(text)
    list_dict = dict_to_list(letter_freq)
    list_dict.sort(reverse=True, key=sort_key)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")

    for char_count_dict in list_dict:
        if char_count_dict["letter"].isalpha():
            print(f"The {char_count_dict["letter"]} character was found {char_count_dict["count"]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    return len(text.split())

def count_letter_frequency(text):
    freq_dict = {}
    text_lower = text.lower()

    for char in text_lower:
        if char in freq_dict.keys():
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1

    return freq_dict

def dict_to_list(dict):
    new_list = []
    for key, value in dict.items():
        new_list.append({"letter": key, "count": value})
    return new_list


def sort_key(dict):
    return dict["count"]

if __name__ == "__main__":
    main()