import os, time, json

with open("src/letters.json", "r") as letters_file:
    LETTERS_MAP: dict[str, list[str]] = json.load(letters_file)

def clear_terminal() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def animator(filename: str, word_delay: float = 0.5, line_delay: float = 0.5) -> None:
    clear_terminal()
    # line: list[list[str]] = []
    # [
    #   [line1, ...]
    #   [line2, ...]
    #   [line3, ...]
    # ]
    with open(filename, "r", encoding="utf8") as lyrics_file:
        for line in lyrics_file.readlines():
            print_line(line, word_delay)
            time.sleep(line_delay)

def print_line(line: str, word_delay: float) -> None:
    words = line.split(" ")
    print_line : list[str] = []

    for word in words:
        if all(letter.upper() not in LETTERS_MAP for letter in word):
            continue
        for letter in word:
            letter_upper = letter.upper()
            height = len(print_line)
            if letter_upper not in LETTERS_MAP:
                continue
            ascii_letter = LETTERS_MAP[letter_upper]
            if height == 0: # Aka no letters yet
                print_line.extend(ascii_letter)
            else:
                # Add line of new char to each one
                for i in range(height):
                    print_line[i] = "".join((print_line[i], ascii_letter[i]))
        clear_terminal()
        # print(print_line)
        print("\n".join(print_line))
        print_line.clear()
        time.sleep(word_delay)

animator("src/song.txt")