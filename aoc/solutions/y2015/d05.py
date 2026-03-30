from aoc.puzzles import register

@register(2015, 5, 1)
def part1(input_data):

    vowels = ["a", "e", "i", "o", "u"]
    bad_sub_strings = ["ab", "cd", "pq", "xy"]

    nice_strings_count = 0

    for check_string in input_data.splitlines():

        # Check for bad sub strings
        has_bad_sub_string = False

        for sub_string in bad_sub_strings:
            if sub_string in check_string:
                has_bad_sub_string = True
                break
        
        if has_bad_sub_string:
            continue

        # Check for vowels
        vowel_count = 0
        has_double_char = False
        previous_char = ""
        has_correct_vowels = False

        for c in check_string:
            if c in vowels:
                vowel_count += 1
            
            if previous_char == c:
                has_double_char = True
            
            if vowel_count >= 3 and has_double_char:
                has_correct_vowels = True
                break

            previous_char = c

        if has_correct_vowels:
            nice_strings_count += 1

    return str(nice_strings_count)


@register(2015, 5, 2)
def part2(input_data):

    nice_strings_count = 0

    for check_string in input_data.splitlines():

        # Check for pairs
        has_pair = False

        for i in range(len(check_string)-3):

            sub_string_pair = check_string[i:i+2]

            if sub_string_pair in check_string[i+2:]:
                has_pair = True
                break
        
        if not has_pair:
            continue

        # Check for repeat
        has_repeat = False

        for i in range(len(check_string)-2):
            if check_string[i] == check_string[i+2]:
                has_repeat = True
                break
        
        if has_repeat and has_pair:
            nice_strings_count += 1

    return str(nice_strings_count)


