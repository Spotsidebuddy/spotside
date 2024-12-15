def filter_string(string, letter):
    index = 0
    result = ''
    while index < len(string):
        if letter != string[index]:
            result = result + string[index]
    return result


print(filter_string('gbgbcmrf', 'b'))
