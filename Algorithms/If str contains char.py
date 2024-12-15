def is_contains_char(phrase, char):
    index = 0
    result = False

    while index < len(phrase):
        if char == phrase[index]:
            result = True
        index += 1

    return result

print(is_contains_char('Gbgbcmrf!', 'F'))
