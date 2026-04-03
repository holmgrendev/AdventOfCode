from aoc.puzzles import register

@register(2015, 11, 1)
def part1(input_data):

    return new_password(input_data, 1)

@register(2015, 11, 2)
def part2(input_data):

    return new_password(input_data, 2)



def increment_password(input_data):
    password = ""
    password_chars = list(input_data)
    i = len(password_chars) -1

    while i >= 0:
        
        if password_chars[i] == "z":
            password_chars[i] = "a"
            i -= 1
        
        else:
            password_chars[i] = chr(ord(password_chars[i]) +1)
            password = "".join(password_chars)
            break
            
    return password

def new_password(input_data, iterations):

    password = input_data.strip()
    illegal_chars = ["i", "o", "l"]

    for _ in range(iterations):
        while True:
            password = increment_password(password)

            # Check illegal characters
            if any(illegal_char in password for illegal_char in illegal_chars):
                continue


            # Check if three chars in line has
            valid_increment = False

            for i, char in enumerate(password):
                if i == 0 or i == 1:
                    continue

                if ord(password[i-2]) == (ord(password[i-1])-1) and ord(password[i-2]) == (ord(char)-2):
                    valid_increment = True
                    break
            
            if not valid_increment:
                continue


            # Look for two different, non-overlapping pairs of characters
            previous_pair = ""
            valid_pairs = False

            for i, char in enumerate(password):
                if i == 0:
                    continue

                if char == password[i-1]:
                    if not previous_pair:
                        previous_pair = char
                        continue
                
                    if previous_pair != char:
                        valid_pairs = True
                        break
            
            if not valid_pairs:
                continue

            break

    return password