# Make a function that takes a string and returns the most common letter lowercased 
# in the string regardless of capitalization.
# ignore spaces
# assume only one letter will have the most occurences
#ex) "John Loves to Play Baseball and Joanie Loves to Play Basketball, but Jenny Likes To Dance"
#output: l

def solution(string):
    letter_count = {}
    for letter in string.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        elif letter != ' ':
            letter_count[letter] = 1
    most = 0
    common_letter = ''
    for letter, count in letter_count.items():
        if count > most:
            most = count
            common_letter = letter
    return common_letter

