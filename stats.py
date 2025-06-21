def get_num_words(file_contents):
    word_count = file_contents.split()
    return len(word_count)


def get_chars_dict(file_contents):
    chars = {}
    lowercase_file_contents = file_contents.lower()

    for character in lowercase_file_contents:
        if character not in chars:
            chars[character] = 1
        else:
            chars[character] += 1
    return chars
