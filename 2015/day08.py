import re

with open('inputs\day08.txt', 'r') as inputs:
    full_input = inputs.read().splitlines()

# Part 1
in_code_len = 0
in_memory_len = 0

for line in full_input:

    # Add whole line length to total length
    in_code_len += len(line)

    # Replace ASCII code \x** with single character
    line = re.sub(r'\\[x][0-9a-fA-F][0-9a-fA-F]', 'D', line)
    # replace double backslash \\ with single character
    line = re.sub(r'\\\\', 'K', line)
    # replace basic escape \* with single character
    line = re.sub(r'(\\).', 'S', line)

    # add in memory text lenght to total in memory length
    in_memory_len += len(line)-2


print(f"In code: {in_code_len}, in memory: {in_memory_len}. Delta: {in_code_len - in_memory_len}")

# Part 2
escaped_in_code_len = 0
excaped_in_memory_len = 0

for line in full_input:

    # Add whole line length to total length

    print(line, len(line))

    # Escape a middle escape, e.g. ...\"... to ...\\\"...
    line = line.replace(r'\"', r'\\\"')

    # escape double backslash \\ with single character
    line = re.sub(r'\\\\', r'\\\\\\\\', line)

    # Escape ASCII symbol. #todo this is bullshit workaround
    line = re.sub(r'\\[x][0-9a-fA-F][0-9a-fA-F]', r'\\\\x27' , line)

    # escape original quotes, e.g. "abc" to "\"abc\""
    line = fr'"\{line[0:len(line)-1]}\""'

    print(line, len(line))
    print(" ")
    escaped_in_code_len += len(line)

print(f"In code: {in_code_len}, in memory: {escaped_in_code_len}. Delta: {escaped_in_code_len - in_code_len}")