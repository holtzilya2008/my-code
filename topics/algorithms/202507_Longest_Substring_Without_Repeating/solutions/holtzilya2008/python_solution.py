
def find_longest_substring(input: str) -> int:    
    length = len(input)
    last_index = length - 1
    
    if length == 0:
        return 0
    
    max = 1
    current_substring_length = 1
    
    for index, char in enumerate(input):
        if index == 0:
            continue
    
        if input[index] == input[index - 1]:
            current_substring_length = 1
        else:
            current_substring_length += 1
            if current_substring_length > max: 
                max = current_substring_length
    
    return max        
