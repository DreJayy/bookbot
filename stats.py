def getNumWords(path_to_file):
    with open(path_to_file) as f:
        contents = f.read().split()

    num_words = len(contents)

    print(f"Found {num_words} total words")

def countCharacter(path_to_file):
    letter_count = {}

    with open(path_to_file) as f:
        word = f.read().split()

    for char in word:
        char_lower = char.lower()

        for letter in char_lower:
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1

    return letter_count

def sortItems(items):
    pairs = list(items.items())
    pairs.sort(reverse=True, key=lambda x: x[1])

    for key, value in pairs:
        print(f"{key}: {value}")
