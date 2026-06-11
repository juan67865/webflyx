from stats import word_count, count_char, char_count_list
import sys

def get_book_text(file_name: str):
    with open(file_name) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    text = get_book_text(path)

    result = word_count(text)

    chars = count_char(text)

    listed_dict = char_count_list(chars)

    print(f"{result}")
    #print(chars)

    for item in listed_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")


    
    


if __name__ == "__main__":
    main()
