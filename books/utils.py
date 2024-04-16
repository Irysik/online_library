from typing import BinaryIO


def next_char(file: BinaryIO, encoding: str = 'utf-8', max_len: int = 8):
    b_char = b""
    while True:
        b_char += file.read(1)
        try:
            char = b_char.decode(encoding=encoding)
        except UnicodeDecodeError:
            if len(b_char) > max_len:
                raise
            continue

        return char, len(b_char)


def read_book_page(
    book_path: str,
    start_byte: int,
    page_size: int = 5000,
):
    last_byte = start_byte
    characters = ""
    with open(book_path, 'rb') as file:
        file.seek(start_byte)
        while True:
            try:
                char, char_num = next_char(file)
            except UnicodeDecodeError:
                file.seek(start_byte - 1)
                continue

            last_byte += char_num

            characters += char

            if char == "":
                break

            if len(characters) >= page_size:
                break
            # if len(characters) >= page_size and char in (" ", "\n"):
            #     break

    return characters, last_byte


if __name__ == "__main__":
    book_path = "test.txt"
    # with open(book_path, 'w', encoding='utf-8') as file:
    #     file.write("Lorem ipsum dolor sit")

    start_char = 0
    last_char = 0
    while True:
        chars, last_char = read_book_page(
            book_path=book_path,
            start_byte=start_char,
            page_size=50,
        )
        print(chars)
        if start_char == last_char:
            break

        start_char = last_char
