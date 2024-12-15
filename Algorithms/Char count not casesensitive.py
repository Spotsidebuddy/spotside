# мое решение
def filter_string(string, char):
    index = 0
    result = ''
    for current_char in string:
        if current_char.lower() != char.lower():
            result = result + string[index]
        index += 1
    return result


# РЕШЕНИЕ УЧИТЕЛЯ
# 
# def filter_string(text, char):
#     result = ''
#     for current_char in text:
#         if current_char.upper() != char.upper():
#             result += current_char
#     return result
